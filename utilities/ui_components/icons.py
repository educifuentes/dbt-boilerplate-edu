ICONS = {
    # branding
    "logo": "energy_program_saving",
    
    # tables
    "person": "person",
    "hogares": "family_group",
    "bases_ccu": "assignment",
    "contratos": "contract",
    
    # VALIDATIONS   
    "check": "check_box",
    "warning": "warning",
    "close": "close",
    
    # otros
    "documentation": "article",
    "metrics": "calculate",
    "not_apply": "circle"
}

def render_icon(icon_key: str) -> str:
    """
    Returns the streamlit material icon format for a given key.
    """
    icon_name = ICONS.get(icon_key, "help")
    return f":material/{icon_name}:"