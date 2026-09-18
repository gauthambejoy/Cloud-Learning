# Log Monitoring API with Redis

A simple Flask application that analyzes uploaded log files and uses Redis to cache the results for faster responses.

## Features

* Upload log files through an API
* Counts:

  * Total lines
  * INFO messages
  * ERROR messages
  * WARNING messages
* Redis caching
* Cache expires after 60 seconds
* Docker support
* Docker Compose for Flask and Redis

## API Endpoint

### `POST /upload`

Upload a log file for analysis.

Example using `curl`:

```bash
curl -X POST -F "file=@application.log" http://localhost:5000/upload
```

Example response:

```json
{
  "source": "system",
  "result": {
    "TOTAL LINES": 100,
    "INFO": 60,
    "ERROR": 20,
    "WARNING": 20
  }
}
```

If the result is already cached:

```json
{
  "source": "cache",
  "result": {
    "TOTAL LINES": 100,
    "INFO": 60,
    "ERROR": 20,
    "WARNING": 20
  }
}
```

## Requirements

* Python 3.x
* Flask
* Redis
* Docker
* Docker Compose

## Run with Docker Compose

Start the application:

```bash
docker compose up --build
```

The Flask API will be available at:

```text
http://localhost:5000
```

Redis runs as a separate container and is connected to the Flask application through Docker Compose.

## How It Works

```text
Log File
   ↓
Flask API
   ↓
Analyze Log
   ↓
Check Redis Cache
   ↓
Store Result for 60 seconds
   ↓
Return Response
```

## Technologies

* Python
* Flask
* Redis
* Docker
* Docker Compose
* REST API
* JSON
