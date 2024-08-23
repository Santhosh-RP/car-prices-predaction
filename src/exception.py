import logging
import os
import sys

# Setup basic configuration for logging
logging.basicConfig(
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("logs/error.log"),  # Ensure the logs directory exists
        logging.StreamHandler(sys.stdout)       # Logs to console as well
    ]
)

class CustomException(Exception):
    """
    A base class for all custom exceptions in this project.
    Provides enhanced logging for exceptions.
    """
    def __init__(self, message, error_details: sys = None):
        super().__init__(message)
        self.error_details = error_details
        self.log_exception(message)

    def log_exception(self, message):
        """
        Logs the exception details including the type, message, and stack trace if available.
        """
        if self.error_details:
            _, _, exc_tb = self.error_details.exc_info()

            if exc_tb:
                file_name = exc_tb.tb_frame.f_code.co_filename
                line_number = exc_tb.tb_lineno
                logging.error(f"Exception occurred in file [{file_name}] at line [{line_number}]: {message}")
            else:
                logging.error(f"Exception occurred: {message} (No traceback available)")
        else:
            logging.error(f"Exception occurred: {message} (No error details provided)")

# Example of custom exceptions
class DataProcessingError(CustomException):
    """
    Raised when an error occurs during data processing.
    """
    def __init__(self, message, error_details: sys = None):
        super().__init__(message, error_details)

class ModelTrainingError(CustomException):
    """
    Raised when an error occurs during model training.
    """
    def __init__(self, message, error_details: sys = None):
        super().__init__(message, error_details)


# Utility function to log exceptions without re-raising
def handle_exception(exception: Exception, error_details: sys = None):
    """
    Handles the logging of exceptions without re-raising them.

    Args:
    - exception (Exception): The exception instance to be handled.
    - error_details (sys): The sys module to fetch exception information.
    """
    if isinstance(exception, CustomException):
        exception.log_exception(str(exception))
    else:
        logging.error(f"An error occurred: {str(exception)}", exc_info=error_details)


# Example Usage
if __name__ == "__main__":
    try:
        # Simulate an error in data processing
        raise ValueError("Simulated error!")
    except ValueError as e:
        # Now capture the real error details without re-raising
        handle_exception(DataProcessingError("Failed to process the data due to incorrect format.", sys), sys)
