# CPU Process

A simple Bash script that displays the top processes using CPU and memory on a Linux system.

## Features

* Shows top CPU-consuming processes
* Shows top memory-consuming processes
* Allows the number of processes to be specified
* Default output shows the top 10 processes
* Supports `--help` and `-h`
* Uses standard Linux commands

## Requirements

* Linux
* Bash
* `ps`
* `awk`
* `sort`

## Usage

Make the script executable:

```bash
chmod +x process_monitor.sh
```

Run with the default number of processes:

```bash
./process_monitor.sh
```

This shows the top 10 processes.

To show a specific number:

```bash
./process_monitor.sh 5
```

To display help:

```bash
./process_monitor.sh --help
```

or:

```bash
./process_monitor.sh -h
```

## Example

```text
Top 5 by CPU
--------------------------------------------
PID      USER         CPU%   MEM%   COMMAND
1234     user         25.4   2.1    python app.py
...

Top 5 by MEM
--------------------------------------------
PID      USER         CPU%   MEM%   COMMAND
5678     user         5.2    12.4   java application
...
```

## How It Works

The script uses:

```text
ps → Get running processes
awk → Format and filter output
sort → Sort by CPU/MEM usage
```

## Technologies

* Bash
* Linux
* ps
* awk
* sort
* Process Monitoring
