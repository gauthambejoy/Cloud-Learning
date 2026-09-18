# Multi Server Ping

A simple Python script that checks the connectivity of multiple hosts concurrently using `ping` and `ThreadPoolExecutor`.

## Features

* Checks multiple hosts
* Runs ping checks concurrently
* Shows whether each host is:

  * UP
  * DOWN
  * INVALID
* Uses Python's `ThreadPoolExecutor` for parallel execution

## Requirements

* Python 3.x
* Linux/macOS
* `ping` command

## Usage

Run the script:

```bash
python ping_monitor.py
```

Enter the number of hosts:

```text
Enter the number of hosts: 3
Enter the hostname: google.com
Enter the hostname: 8.8.8.8
Enter the hostname: example.com
```

Example output:

```text
google.com is UP
8.8.8.8 is UP
example.com is UP
```

If a host cannot be reached:

```text
192.168.1.100 is DOWN (unreachable)
```

## How It Works

```text
User enters hosts
       ↓
ThreadPoolExecutor
       ↓
Ping hosts concurrently
       ↓
Check return code
       ↓
Display status
```

## Technologies

* Python
* subprocess
* ThreadPoolExecutor
* Linux networking
* ICMP Ping
