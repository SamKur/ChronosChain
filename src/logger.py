import logging
from pathlib import Path
from datetime import datetime

# Set up logging directory and file
log_dir = Path("logs")
log_dir.mkdir(exist_ok=True)

# Where to save .log file
log_file = log_dir / f"{datetime.now():%Y-%m-%d_%H-%M-%S}.log"

# Configure logging
logging.basicConfig(
    handlers=[logging.FileHandler(log_file, 'a')],
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)


# the below line for checking logger functionality
# if __name__=="__main__":
#     logging.info("Logging has started")

# This will create a logfile logs/timestamp.log -> [2024-09-24 13:20:01,386] 22 root - INFO - Logging has started