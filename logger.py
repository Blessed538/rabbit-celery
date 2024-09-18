import logging
from datetime import datetime

# Logging setup for the messaging system
logging.basicConfig(filename='/var/log/messaging_system.log', level=logging.INFO)

# Logging the current time to the log file
def log_message():
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    logging.info(f"Talk to me: {current_time}")
    print(f"Logged time: {current_time}")
