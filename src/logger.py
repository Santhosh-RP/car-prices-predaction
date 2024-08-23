import logging
import os

# Ensure that the logs directory exists
if not os.path.exists('logs'):
    os.makedirs('logs')

# Set up basic configuration for logging
LOG_FORMAT = '%(asctime)s - %(levelname)s - %(name)s - %(message)s'
logging.basicConfig(
    level=logging.DEBUG,  # Change to DEBUG, INFO, WARNING, ERROR, CRITICAL as needed
    format=LOG_FORMAT,
    handlers=[
        logging.FileHandler('logs/application.log'),  # Log to file
        logging.StreamHandler()  # Log to console
    ]
)

# Create a custom logger
def get_logger(logger_name: str) -> logging.Logger:
    """
    Function to create and return a logger instance with a specified name.

    Args:
    - logger_name (str): The name of the logger.

    Returns:
    - logging.Logger: Configured logger instance.
    """
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)  # Set the logging level to DEBUG; can be customized

    return logger

# Example Usage
if __name__ == "__main__":
    logger = get_logger(__name__)
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.critical("This is a critical message")
