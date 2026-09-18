# WatchDog - Mini Monitoring Stack

A simple containerized system monitoring stack that collects CPU, memory, and disk usage and displays the metrics through a web dashboard and CLI.

## Features

* CPU, memory, and disk monitoring
* Real-time metrics dashboard
* Redis for storing metrics
* Background worker for collecting metrics
* Flask API
* Nginx reverse proxy
* Docker Compose
* Health check for Redis
* Application logging
* CLI for checking system status

## Architecture

```text
                    ┌──────────────┐
                    │   Dashboard  │
                    │   (Nginx)    │
                    └──────┬───────┘
                           │
                           ↓
                    ┌──────────────┐
                    │ Flask API    │
                    └──────┬───────┘
                           │
                           ↓
                    ┌──────────────┐
                    │    Redis     │
                    └──────▲───────┘
                           │
                    ┌──────┴───────┐
                    │    Worker    │
                    │   psutil     │
                    └──────────────┘
```

## Components

### Flask API

Provides endpoints for retrieving system metrics and checking Redis status.

```text
GET /metrics
GET /status
```

### Worker

Collects system metrics using `psutil` and stores them in Redis.

Metrics include:

* CPU usage
* Memory usage
* Disk usage

### Redis

Stores the latest system metrics for the Flask API.

### Nginx

Serves the dashboard and acts as a reverse proxy for the Flask API.

### Dashboard

A simple HTML/CSS/JavaScript dashboard displaying:

* CPU
* Memory
* Disk
* Backend status
* Last update time

### CLI

The `watchcli.py` script can be used to check the monitoring stack from the terminal.

```bash
python3 watchcli.py status
```

Example:

```text
=============
System Status
=============
APi     :Running
REDIS   :Connected
=============
CPU     :25.4%
DISK    :42.1%
MEMORY  :63.7%
```

## Requirements

* Docker
* Docker Compose

## Run the Project

Clone the repository:

```bash
git clone <your-repository-url>
cd WatchDog
```

Start the stack:

```bash
docker compose up --build
```

The dashboard will be available at:

```text
http://localhost
```

## CLI

Check the status:

```bash
python3 watchcli.py status
```

Show available commands:

```bash
python3 watchcli.py help
```

## Project Structure

```text
WatchDog/
│
├── app.py
├── watchdog.py
├── monitor.py
├── watchcli.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
│
├── dashboard/
│   ├── index.html
│   ├── script.js
│   └── style.css
│
├── nginx/
│   └── nginx.conf
│
└── README.md
```

## Technologies

* Python
* Flask
* Redis
* Nginx
* Docker
* Docker Compose
* JavaScript
* HTML/CSS
* psutil
* REST API

## What I Practiced

* Building REST APIs with Flask
* Redis integration
* Background workers
* Docker containerization
* Docker Compose networking
* Nginx reverse proxy
* Health checks
* Application logging
* Basic monitoring and observability
* Building a CLI tool
