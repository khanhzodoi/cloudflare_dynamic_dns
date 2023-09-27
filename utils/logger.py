import logging
import os


def get_logger(log_file_path):

    # Generate log file 
    if not generate_log_file(log_file_path):
        return None

    # Create a logger with the desired name
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    # Create a file handler to write log messages to a file
    file_handler = logging.FileHandler(log_file_path)
    file_handler.setLevel(logging.INFO)

    # Create a stream handler to print log messages to the console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Create a formatter for log messages
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add both handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    return logger


def generate_log_file(log_file_path):
    try:
        if not os.path.exists(log_file_path):
            directory_path = os.path.dirname(log_file_path)
            # Create the log directory if it doesn't exist
            if not os.path.exists(directory_path):
                os.makedirs(directory_path)

            # Create an empty log file 
            with open(log_file_path, 'w') as file:
                pass
        
        return True

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False