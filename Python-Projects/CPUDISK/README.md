System Threshold Monitor

A simple Python application that monitors CPU and Disk usage and generates alerts when their usage exceeds the predefined thresholds.

This project is mainly built to practice **Python, Docker, and containerized monitoring**.

Features

- Monitors CPU usage
- Monitors disk usage
- Configurable CPU and disk thresholds
- Prints alerts when thresholds are exceeded
- Logs threshold violations to `threshold.log`
- Runs continuously and checks system usage every 5 seconds

Tech Stack

- Python 3.12
- psutil
- Docker
