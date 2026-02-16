# dbt Python Boilerplate

This is a sample repository for building data pipelines in Python, heavily inspired by the dbt (data build tool) core platform structure, but leveraging Python's flexibility and Streamlit for the UI.

## How to use

### Installation

1.  Clone the repository and remove the git tracking to start your project fresh. Then, initialize your own git repository:

    ```bash
    git clone https://github.com/educifuentes/dbt-boilerplate-edu.git
    cd dbt-boilerplate-edu
    rm -rf .git
    git init
    ```

2.  Create virtual environment

    ```bash
    python -m venv .venv
    source .venv/bin/activate
    ```

3.  Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4.  Run the application:
    ```bash
    streamlit run app.py
    ```

## Project Structure

The project follows a dbt-like structure to organize data transformations and the application logic.

```
dbt-boilerplate-edu
├── README.md              # Project documentation
├── app.py                 # Main Streamlit application entry point
├── models                 # Data transformation logic (dbt-like)
│   ├── staging            # Raw data processing (1:1 with source)
│   ├── intermediate       # intermediate transformations
│   ├── marts              # Business logic and final tables
│   └── metrics            # Key performance indicators
├── pages                  # Streamlit multipage app structure
│   ├── 1_views            # Frontend views for data consumption
│   ├── 2_tools            # Utility tools for the user
│   └── 3_dev              # Development and debugging pages
├── seeds                  # Static data files (CSV, etc.)
└── utilities              # Helper functions and shared logic
    ├── data_transformations # Shared data processing functions
    └── ui_components      # Reusable Streamlit UI components
        ├── icons.py       # Icon mappings from google material icons
        ├── render_docs.py # Documentation renderer from YAML
        ├── render_model.py # Model summary UI component
        └── yaml_loader.py # YAML configuration loader
        dataframe_column_display.py # format columns for user display
        ├── yaml_loader.py # YAML configuration loader
        └── dataframe_column_display.py # format columns for user display

```

### Key Directories

- **`models/`**: Contains the core logic for your data pipeline.
  - `staging/`: Initial cleaning and standardization of raw data.
  - `intermediate/`: Complex transformations and joins.
  - `marts/`: Final, business-ready datasets.
- **`pages/`**: Defines the structure of the Streamlit web application.
- **`utilities/`**: Python modules for reusable code, separating logic from the UI.

## Key Concepts

### dbt-inspired Workflow

This project adopts the philosophy of dbt but implements it in pure Python. Use the `models` directory to structure your data transformations in layers (staging -> intermediate -> marts), ensuring modular and testable code.

### Streamlit UI

The UI is built with Streamlit, providing an interactive way to run pipelines, visualize data, and debug models. The `pages` directory maps directly to the sidebar navigation in the app.

### Prebuilt Utilities

The `utilities` folder contains helper modules to speed up development:

- **`ui_components/icons.py`**: Centralized dictionary of Streamlit/Material icons for consistent UI.
- **`ui_components/render_docs.py`**: Functions to render professional documentation from dbt-style YAML files.
- **`ui_components/render_model.py`**: Standard UI component to display data model summaries (shape, columns, types).
- **`ui_components/yaml_loader.py`**: Safe loading of YAML configuration files, handling relative paths.

## Development

- **Adding a new model**: Create a new Python file in the appropriate `models` subdirectory.
- **Adding a new page**: Create a new Python file in the `pages` directory. Streamlit sorts pages numerically/alphabetically.
