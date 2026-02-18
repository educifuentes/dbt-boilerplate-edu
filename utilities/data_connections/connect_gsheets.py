import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

from utilities.data_connection_config import TTL_VALUE
from utilities.transformations.date_parsing import parse_spanish_month_year
from utilities.transformations.yes_no_to_boolean import yes_no_to_boolean
from utilities.transformations.add_row_number import add_row_number



@st.cache_data
def load_data_gsheets(worksheets: list[str]) -> dict[str, pd.DataFrame]:
    """
    Return a dictionary of DataFrames for given worksheet names.
    
    Args:
        worksheets (list[str]): List of worksheet names to load.
        
    Returns:
        dict[str, pd.DataFrame]: Dictionary with worksheet names as keys and DataFrames as values.
    """
    
    conn = st.connection("gsheets", type=GSheetsConnection, ttl=TTL_VALUE)
    
    dataframes = {}
    for w in worksheets:
        df = conn.read(worksheet=w)
        # Check if add_row_number is generic enough to always apply, 
        # or if it should be optional. For now, we'll keep it as per instruction 
        # to just genericize the inputs/outputs.
        df = add_row_number(df)
        dataframes[w] = df

    return dataframes

