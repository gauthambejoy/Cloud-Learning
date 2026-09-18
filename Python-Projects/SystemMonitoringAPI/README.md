# System Monitoring API

A simple Flask REST API that provides basic system health and resource usage information.

## Features

* Health check endpoint
* CPU usage monitoring
* Memory usage monitoring
* Disk usage monitoring
* Request logging
* HTTP error handling
* JSON responses
* Docker support

## API Endpoints

| Endpoint  | Description           |
| --------- | --------------------- |
| `/health` | Checks service health |
| `/cpu`    | Shows CPU usage       |
| `/memory` | Shows memory usage    |
| `/disk`   | Shows disk usage      |

## Example

Check system health:

```bash
curl http://localhost:5000/health
```

Example response:

```json
{
  "data": {
    "services": "healthy"
  },
  "message": "success",
  "status": 200
}
```

Check CPU usage:

```bash
curl http://localhost:5000/cpu
```

## Requirements

* Python 3.x
* Flask
* psutil
* Docker (optional)

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run Locally

```bash
python SystemMonitoringAPI.py
```

The API will be available at:

```text
http://localhost:5000
```

## Run with Docker

Build the image:

```bash
docker build -t system-monitoring-api .
```

Run the container:

```bash
docker run -p 5000:5000 system-monitoring-api
```

## Logging

Application and request logs are stored in:

```text
SystemMonitoring.log
```

The application also logs HTTP errors and unexpected exceptions.

## Technologies

* Python
* Flask
* psutil
* REST API
* Docker
* Logging
