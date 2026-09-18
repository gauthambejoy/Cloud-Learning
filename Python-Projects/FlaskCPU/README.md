# System Monitoring API

A simple Flask-based REST API that provides basic system resource information such as CPU, memory, and disk usage.

The application is also containerized using Docker.

## Features

* CPU usage monitoring
* Memory usage monitoring
* Disk usage monitoring
* Request logging
* Error handling
* JSON API responses
* Docker support

## API Endpoints

| Endpoint  | Description        |
| --------- | ------------------ |
| `/cpu`    | Shows CPU usage    |
| `/memory` | Shows memory usage |
| `/disk`   | Shows disk usage   |

### Example

```bash
curl http://localhost:5000/cpu
```

Response:

```json
{
  "status": 200,
  "message": "success",
  "data": {
    "cpu": 25.4
  }
}
```

## Requirements

* Python 3.x
* Flask
* psutil
* Docker (optional)

## Run Locally

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python FlaskCPU.py
```

The API will be available at:

```text
http://localhost:5000
```

## Run with Docker

Build the Docker image:

```bash
docker build -t system-monitoring-api .
```

Run the container:

```bash
docker run -p 5000:5000 system-monitoring-api
```

Then access the API:

```bash
curl http://localhost:5000/cpu
```

## Technologies

* Python
* Flask
* psutil
* REST API
* Docker
* Logging
