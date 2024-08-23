import logging
import os
from datetime import datetime

# Generate the log file name with timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define the path to the 'logs' directory
logs_directory = os.path.join(os.getcwd(), "logs")

# Ensure the 'logs' directory exists
os.makedirs(logs_directory, exist_ok=True)

# Define the full path to the log file
LOG_FILE_PATH = os.path.join(logs_directory, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# Optional: Log a test message to confirm configuration
logging.info("Logging setup complete.")
