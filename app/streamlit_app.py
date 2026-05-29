import os 
import streamlit as st

def get_environment_config(env_name: str) -> dict:
    configs = {
        "dev": {
            "title": "Dev Environment",
            "background": "#0ab131"
        },
        "qa": {
            "title": "QA Environment",
            "background": "#92730e"
        },
        "prod": {
            "title": "Production Environment",
            "background": "#8b222b"
        }
    }

    return configs.get(env_name.lower(), configs["dev"])

APP_ENV = os.getenv("APP_ENV", "dev")
config = get_environment_config(APP_ENV)

st.set_page_config(page_title=config["title"])

st.markdown(f"""
    <style>
        .stApp {{
            background-color: {config["background"]};
        }}
    </style>
""", unsafe_allow_html=True)

st.title(config["title"])
st.write(f"You are currently in the {APP_ENV.upper()} environment.")