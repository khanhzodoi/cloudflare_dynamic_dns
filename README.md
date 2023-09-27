# DNS Management Script

A Python script for managing DNS records using the Cloudflare API.

## Overview

This script provides a convenient way to manage DNS records hosted on Cloudflare. It allows you to add, update, and remove DNS records programmatically, making it useful for various DNS management tasks.

## Features

- **DNS Record Management**: Add, update, and remove DNS records on Cloudflare.
- **Configuration File**: Use a configuration file (`config.toml`) to specify settings such as API credentials and file paths.
- **Logging**: Log script activities and errors to a specified log file for monitoring and debugging.
- **Error Handling**: Gracefully handle errors and exceptions during script execution.
- **Modular Design**: Organize code into modules for IP retrieval, file handling, and logging.
- **Security**: Implement security best practices, such as securing API tokens and validating input data.
- **Configuration Management**: Manage configuration settings separately from the code.
- **Structured Documentation**: Include comments and documentation for clear understanding.

## Prerequisites

- Python 3.x
- Required Python packages (specified in `requirements.txt`)
- Cloudflare API token and account email

## Usage

1. Install the required Python packages:
    ```
    pip install -r requirements.txt
    ```

2. Create a `config.toml` file with your configuration settings. See `config_example.toml` for an example.

3. Run the script:
    ```
    python main.py
    ```

4. Follow the on-screen prompts and monitor the log file for updates.
