import logging
import os
import yaml

def load_config(config_file="config.yaml"):
    """
    Load the configuration settings from a YAML file.

    Args:
        config_file (str): Path to the YAML configuration file.
    
    Returns:
        dict: The configuration settings as a dictionary.
    """
    with open(config_file, 'r') as file:
        config = yaml.safe_load(file)
    return config

def setup_logging(config):
    """
    Set up the logging configuration based on the settings in the config file.

    Args:
        config (dict): Configuration settings loaded from the YAML file.
    
    Returns:
        logging.Logger: Configured logger instance.
    """
    # Extract logging settings from the configuration
    log_level = config['logging'].get('level', 'INFO').upper()
    log_file = config['logging'].get('log_file', 'refactor_earth.log')
    console_output = config['logging'].get('console_output', True)

    # Create log directory if it doesn't exist
    log_dir = os.path.dirname(log_file)
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Configure logging
    logging.basicConfig(
        level=getattr(logging, log_level),
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler() if console_output else logging.NullHandler()
        ]
    )

    # Create a logger instance
    logger = logging.getLogger('RefactorEarth')
    logger.info('Logging setup complete.')
    
    return logger

# Example usage within another script
if __name__ == "__main__":
    # Load configuration from the config.yaml file
    config = load_config()

    # Set up logging based on the configuration
    logger = setup_logging(config)

    # Example logging messages
    logger.debug("This is a debug message.")
    logger.info("This is an info message.")
    logger.warning("This is a warning message.")
    logger.error("This is an error message.")
    logger.critical("This is a critical message.")

