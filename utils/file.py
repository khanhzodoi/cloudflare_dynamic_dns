"""Module File to handle file stuffs"""
import os
import json
import toml

def load_credential(logger, file_path):
    """Load credential file"""
    if not os.path.exists(file_path):
        logger.error(f"The file '{file_path}' does not exist.")
        return {}

    try:
        with open(file_path , "r", encoding="utf-8") as json_file:
            data = json.load(json_file)

            # Check for required fields
            required_fields = ["zone_identifier", "email_account", "api_token"]
            for field in required_fields:
                if field not in data:
                    raise ValueError(f"Missing required field: {field}")

        return data

    except FileNotFoundError as error:
        logger.error(f"File not found: {str(error)}")
        return {}
    except json.JSONDecodeError as error:
        logger.error(f"Error decoding JSON: {str(error)}")
        return {}

def load_config(config_file):
    """Load config file"""
    try:
        with open(config_file, "r", encoding="utf-8") as file:
            config = toml.load(file)
            return config
    except FileNotFoundError:
        print(f"Config file '{config_file}' not found. Please create it.")
        return None
