import streamlit as st
import yaml
import os

def render_model_docs(yaml_path, kind="table"):
    """
    Lee un archivo YAML de documentación (formato dbt) y lo renderiza
    con un diseño limpio y profesional en Streamlit.
    """
    if not os.path.exists(yaml_path):
        st.error(f"⚠️ Archivo no encontrado: `{yaml_path}`")
        return

    try:
        with open(yaml_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
    except Exception as e:
        st.error(f"❌ Error al cargar el archivo YAML: {e}")
        return

    if not data or ('models' not in data and 'metrics' not in data):
        st.warning("No se encontró información de modelos o métricas en el archivo.")
        return

    items = data.get('models', []) + data.get('metrics', [])

    for model in items:
        model_name = model.get('name', 'Sin Nombre')
        description = model.get('description', 'Sin descripción disponible.')
        
        with st.container():
            if kind == "metrics":
                st.subheader(f"{model_name}")
            else:
                st.subheader(f"Tabla: {model_name}")
            st.info(description)
            
            if 'columns' in model:                
                # Preparar datos para la tabla
                if kind == "metrics":
                    table_content = "| Columna | Descripción |\n| :--- | :--- |\n"
                else:
                    table_content = "| Columna | Descripción | Tipo |\n| :--- | :--- | :--- |\n"
                
                def get_simple_type(t):
                    if not t: return "---"
                    t = str(t).lower()
                    if any(x in t for x in ["str", "varchar", "text", "string"]): return "Texto"
                    if any(x in t for x in ["int", "float", "number", "numeric", "decimal"]): return "Número"
                    if "bool" in t: return "Booleano"
                    if any(x in t for x in ["date", "time", "stamp"]): return "Fecha"
                    return "Otro"

                for col in model['columns']:
                    name = f"`{col.get('name', '')}`"
                    desc = col.get('description', '---')
                    
                    if kind == "metrics":
                        table_content += f"| {name} | {desc} |\n"
                    else:
                        raw_type = col.get('data_type') or col.get('type', '')
                        tipo = get_simple_type(raw_type)
                        table_content += f"| {name} | {desc} | {tipo} |\n"
                
                st.markdown(table_content)
            
            if 'table' in model:
                st.markdown(model['table'])
            
            st.divider()
