# Docker Container Watchdog

A simple Bash script that checks the status of a Docker container and automatically restarts it if it is not running.

## Features

* Checks Docker container status
* Detects invalid container names
* Automatically restarts stopped containers
* Logs container status and actions
* Adds timestamps to log entries

## Requirements

* Linux
* Bash
* Docker

## Usage

Make the script executable:

```bash
chmod +x watchdog.sh
```

Run the script:

```bash
./watchdog.sh
```

Enter the container name when prompted:

```text
Enter the container name:
redis
```

If the container is running:

```text
Up 5 minutes
redis - Container is running
```

If the container is stopped:

```text
redis - Container is not running, restarting ...
```

The script will restart the container automatically.

## Logging

Container status and actions are recorded in the log file:

```text
watchdog.log
```

Each log entry includes a timestamp.

Example:

```text
2026-09-18 08:30:15 - Up 10 minutes
2026-09-18 08:30:15 - redis - Container is running
```

## How It Works

```text
Enter Container Name
        ↓
Check Container Status
        ↓
Is Container Valid?
   ↓             ↓
  No             Yes
   ↓              ↓
Log Error     Is it Running?
                  ↓
            ┌─────┴─────┐
           Yes           No
            ↓             ↓
        Log Status    Restart Container
                          ↓
                      Log Result
```

## Technologies

* Bash
* Docker CLI
* Linux
* Shell Scripting
* Logging
