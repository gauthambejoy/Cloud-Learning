# Log Parser

A simple Python script that collects recent Linux system logs using `journalctl` and counts log messages by severity.

## Features

* Fetches recent logs using `journalctl`
* Allows the user to choose the number of log lines
* Counts:

  * ERROR
  * WARNING
  * INFO
* Uses separate functions for log collection and parsing

## Requirements

* Python 3.x
* Linux
* `journalctl`

## Usage

Run the main program:

```bash
python main.py
```

Enter the number of log lines:

```text
Enter the number of lines: 100
```

Example output:

```text
{'ERROR': 5, 'WARNING': 12, 'INFO': 43}
```

## Project Structure

```text
journal-log-parser/
├── main.py
├── LogParser.py
└── README.md
```

## How It Works

```text
User Input
    ↓
journalctl
    ↓
Collect Log Lines
    ↓
Parse Logs
    ↓
Count ERROR / WARNING / INFO
    ↓
Display Results
```

## Technologies

* Python
* Linux
* journalctl
* subprocess
