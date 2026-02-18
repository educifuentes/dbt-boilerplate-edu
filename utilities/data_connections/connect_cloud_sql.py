import streamlit as st
import pandas as pd
from google.cloud.sql.connector import Connector
import sqlalchemy

# Initialize Connector object
connector = Connector()

def getconn():
    conn = connector.connect(
        st.secrets["gcp_cloud_sql"]["INSTANCE_CONNECTION_NAME"],
        "pg8000",
        user=st.secrets["gcp_cloud_sql"]["DB_USER"],
        password=st.secrets["gcp_cloud_sql"]["DB_PASS"],
        db=st.secrets["gcp_cloud_sql"]["DB_NAME"],
    )
    return conn

@st.cache_resource
def get_engine():
    pool = sqlalchemy.create_engine(
        "postgresql+pg8000://",
        creator=getconn,
    )
    return pool

@st.cache_data(ttl=600)
def load_data_cloud_sql(table_name: str):
    """
    Loads all data from a specified Cloud SQL table into a pandas DataFrame.
    """
    pool = get_engine()
    
    with pool.connect() as db_conn:
        # Use pandas read_sql for convenience
        # Note: Using f-string for table name in SQL is generally unsafe if input is untrusted.
        # However, for an internal utility where table_name comes from code, it's acceptable for this scope.
        # Ideally, we would validate table_name against a whitelist or use sqlalchemy.Table.
        df = pd.read_sql(sqlalchemy.text(f"SELECT * FROM {table_name}"), db_conn)
    
    return df

def update_record(table_name: str, record_id: int, changes: dict, id_column: str = "id"):
    """
    Update a record in Cloud SQL.
    
    Args:
        table_name: Name of the table.
        record_id: ID of the record to update.
        changes: dict of column name -> new value
        id_column: Name of the ID column (default "id")
    """
    pool = get_engine()
    with pool.connect() as conn:
        set_clauses = []
        params = {"id": record_id}
        
        for i, (col, val) in enumerate(changes.items()):
            param_name = f"val_{i}"
            set_clauses.append(f"{col} = :{param_name}")
            params[param_name] = val
            
        if not set_clauses:
            return

        stmt = sqlalchemy.text(f"UPDATE {table_name} SET {', '.join(set_clauses)} WHERE {id_column} = :id")
        conn.execute(stmt, params)
        conn.commit()

def delete_record(table_name: str, record_id: int, id_column: str = "id"):
    """
    Delete a record from Cloud SQL.
    """
    pool = get_engine()
    with pool.connect() as conn:
        stmt = sqlalchemy.text(f"DELETE FROM {table_name} WHERE {id_column} = :id")
        conn.execute(stmt, {"id": record_id})
        conn.commit()
