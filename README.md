# 📡 Advanced Bluetooth LE Scanner

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey)
![License](https://img.shields.io/badge/license-MIT-green)

A professional, asynchronous Command Line Interface (CLI) tool designed to scan for Bluetooth Low Energy (BLE) devices nearby. It features a modern, color-coded UI, real-time signal sorting, and robust error handling for Windows environments.

---

## 📸 Demo

![Scanner Screenshot](screenshot.png)
*(Note: Replace this image with a screenshot of your actual terminal output)*

---

## 🚀 Key Features

* **Modern UI:** Utilizes the `rich` library to display results in a beautiful, readable table format.
* **Smart Sorting:** Automatically sorts devices by Signal Strength (RSSI), showing the closest devices first.
* **Visual Feedback:**
    * Real-time progress bar with percentage.
    * Color-coded signal strength (Green/Yellow/Red) based on connection quality.
* **Windows Optimized:** Includes specific event loop policies to prevent common `asyncio` crashes on Windows 10/11.
* **Crash-Proof:** Implements robust error handling to manage incomplete device data without stopping the execution.

---

## 🛠️ Prerequisites

Before you begin, ensure you have the following installed:
* **Python 3.8** or higher.
* A device with **Bluetooth** capability (enabled).

---

## 📦 Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Nawafalzanbaqi/Bluetooth-LE-Scanner.git](https://github.com/Nawafalzanbaqi/Bluetooth-LE-Scanner.git)
    cd Bluetooth-LE-Scanner
    ```

2.  **Install the required dependencies:**
    It is recommended to use a virtual environment.
    ```bash
    pip install bleak rich
    ```
    *Or if you have a requirements file:*
    ```bash
    pip install -r requirements.txt
    ```

---

## 💻 Usage

To start the scanner, simply run the Python script:

```bash
python scanner.py
```
---

## What happens next?

The tool will initialize and show a loading bar for 5 seconds.

- It scans for all nearby BLE devices.

- A detailed table will be displayed with:

- Signal Strength (dBm)

- Device Name

- MAC Address

- Manufacturer ID

Press Enter to exit the program safely.

---

## 🧩 Code Structure
asyncio: Manages asynchronous scanning without freezing the UI.

BleakScanner: Handles the low-level Bluetooth discovery.

Rich: Powers the terminal formatting, tables, and progress bars.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

---
<p align="center"> Made with ❤️ and Python </p>
