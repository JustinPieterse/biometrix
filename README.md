# Biometrix Clock-In/Clock-Out System

A Raspberry Pi-based clock-in/clock-out system designed to track employee attendance using a fingerprint sensor, LCD display, and RGB LED. The system stores attendance logs in a SQLite database and supports exporting to CSV for payroll processing.

---

## Features

- **Fingerprint-Based Attendance**: Employees clock in and out using their fingerprint.
- **Visual Feedback**:
  - RGB LED indicates success (green), error (red), or standby (blue).
  - LCD screen displays clock-in/out status and error messages.
- **Data Management**:
  - Logs attendance in a SQLite database.
  - Exports timesheets to CSV files.
- **Error Handling**: Displays error codes on the LCD and logs errors in a system log file.

---

## Hardware Requirements

- Raspberry Pi Zero 2 W (or compatible model)
- AS608 Optical Fingerprint Sensor
- Nokia 5110 LCD Screen
- RGB LED (Common Anode)
- 64GB SD Card
- Jumper wires, resistors, and connectors
- 3D-printed enclosure (optional)

---

## Software Requirements

- **Operating System**: Raspberry Pi OS Lite (CLI)
- **Python**: Version 3.7 or higher
- **Libraries**:
  - `gpiozero`
  - `pyserial`
  - `sqlite3` (built-in)
  - `Pillow` (for LCD graphics)

---

## Setup Instructions

### 1. Install Required Libraries

Update the Raspberry Pi and install the necessary libraries:
```bash
sudo apt update
sudo apt upgrade
sudo apt install python3-serial python3-gpiozero python3-pil
