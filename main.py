from app.streamlit_app import get_environment_config, APP_ENV, config

def main():
    config = get_environment_config("dev")
    print(config["title"])


if __name__ == "__main__":    
    main()