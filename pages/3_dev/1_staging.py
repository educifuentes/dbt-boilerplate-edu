import streamlit as st

from models.staging._stg_schema__table import stg_censo_2024__personas

from utilities.ui_components import render_model_ui

# Page settings and header
st.title("Staging")
st.markdown("Tablas staging 1:1 con fuentes - Bases CCU, Contratos, Locales y Censos.")

# Create tabs for organization
tab1, tab2 = st.tabs([
    ":material/person: table_1_name",
    ":material/map: table_2_name",
    ":material/home: table_3_name",

])

with tab1:
    censo_2024__personas_df = stg_reportes_ccu_base_2026_q1()
    render_model_ui(censo_2024__personas_df)

with tab2:
    censo_2024__hogares_df = stg_censo_2024__personas()
    render_model_ui(censo_2024__hogares_df)
    
with tab3:
    censo_2024__hogares_df = stg_censo_2024__personas()
    render_model_ui(censo_2024__hogares_df)