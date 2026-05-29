from app.streamlit_app import get_environment_config


def test_dev_environment_config():
    config = get_environment_config("dev")
    assert config["title"] == "Dev Environment"


def test_qa_environment_config():
    config = get_environment_config("qa")
    assert config["title"] == "QA Environment"


def test_prod_environment_config():
    config = get_environment_config("prod")
    assert config["title"] == "Production Environment"
