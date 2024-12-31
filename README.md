# Port Scanner

## Description
A Python-based port scanning tool that allows users to check for open ports on a given IP address or hostname. The tool supports features such as silent mode, verbose mode, and custom timeout settings. It also provides the option to save scan results and display timestamps for each scanned port.

This version includes host-based scanning, enabling users to scan ports using a hostname instead of an IP address.

---

## Features
- **Scan Open Ports:** Check for open ports on a given IP or hostname.
- **Silent Mode:** Suppress output during scanning.
- **Verbose Mode:** Display detailed error messages during scanning.
- **Custom Port Range:** Specify a range of ports to scan.
- **Timeout Setting:** Define a timeout duration for each port scan.
- **Save Results:** Save the scan results to a file (`results.txt`).
- **Display Timestamps:** Show the date and time for each scanned port.
- **Hostname Support:** Scan ports using a hostname instead of an IP address.


---

## Usage
### 1. Run the Program
Execute the program using the following command:
```bash
make && make run
```

### 2. Menu Options
- **1:** Scan for open ports.
- **2:** Silent scan for open ports (suppresses output).
- **3:** Verbose scan for open ports (provides detailed error messages).
- **4:** Scan given IP for known hosts like http, ssh, etc.
- **5:** Set IP or hostname.
- **6:** Set port range.
- **7:** Set timeout duration.
- **8:** Display scanned port results (if available).
- **9:** Save scanned port results to `results.txt`.
- **0:** Exit the program.

### 3. Example Workflow
1. **Set IP/Hostname:** Enter an IP address or hostname.
2. **Set Port Range:** Define a range of ports (e.g., `20 100`).
3. **Set Timeout:** Specify a timeout duration (e.g., `1` second).
4. **Scan Ports:** Choose a scanning option (e.g., `1` for a regular scan).
5. **View Results:** Select option `7` to display results or option `8` to save them.

---

## File Structure
- **port_scanner.py**: Main program file.
- **menuOptions.py**: Contains utility functions for user input and result management.
- **results.txt**: Output file where scan results are saved.

---

## Example Output
```
           _    _ _   ___      ____  __   _______ ____   ____  _       _____
     /\   | |  | | \ | \ \    / /  \/  | |__   __/ __ \ / __ \| |     / ____|
    /  \  | |__| |  \| |\ \  / /| \  / |    | | | |  | | |  | | |    | (___  
   / /\ \ |  __  | . ` | \ \/ / | |\/| |    | | | |  | | |  | | |     \___ \
  / ____ \| |  | | |\  |  \  /  | |  | |    | | | |__| | |__| | |____ ____) |
 /_/    \_\_|  |_|_| \_|   \/   |_|  |_|    |_|  \____/ \____/|______|_____/
                                                                              
                                                by https://github.com/ahnvm

1. Scan Ip For Open Ports
2. Scan Ip For Open Ports (Silent)
3. Scan Ip For Open Ports (Verbose)
4. Scan Known Ports (Ports like shh, http, https, etc.)
5. Set IP (Current IP: 0.0.0.(0-65535))
6. Set Port Range (Current Port Range: 0-65535)
7. Set Timeout (Current Timeout: 1)
Enter option: 1
```

---

## Notes
- Ensure that you have the necessary permissions to perform a port scan.
- Use this tool responsibly and only on networks you own or have explicit permission to scan.

---

## Contributing
Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss your ideas.

---

## Contact
Author: https://github.com/ahnvm

