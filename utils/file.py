
import os
import json
import toml

def load_credential(logger, file_path):
    if not os.path.exists(file_path):
        logger.error(f"The file '{file_path}' does not exist.")
        return {}
    
    try:
        with open(file_path , "r") as json_file:
            data = json.load(json_file)

            # Check for required fields
            required_fields = ["zone_identifier", "email_account", "api_token"]
            for field in required_fields:
                if field not in data:
                    raise ValueError(f"Missing required field: {field}")
            
        return data
    
    except Exception as e:
        logger.error(f"Error loading credential: {str(e)}")
        return {}


def load_config(config_file):
    try:
        with open(config_file, "r") as file:
            config = toml.load(file)
            return config
    except FileNotFoundError:
        print(f"Config file '{config_file}' not found. Please create it.")
        return None
    except Exception as e:
        print(f"Error loading config file '{config_file}': {str(e)}")
        return None