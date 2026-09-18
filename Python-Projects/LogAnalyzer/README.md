# Log Analyzer

A simple Flask application that displays Linux system logs using `journalctl` and allows filtering logs by severity.

## Features

* Displays system logs
* Filters logs by:

  * ERROR
  * WARNING
  * INFO
* Uses environment variables for configuration
* Flask-based web API
* Uses Linux `journalctl`

## API Endpoints

| Endpoint   | Description              |
| ---------- | ------------------------ |
| `/`        | Shows all available logs |
| `/error`   | Shows ERROR logs         |
| `/warning` | Shows WARNING logs       |
| `/info`    | Shows INFO logs          |

## Example

Open:

```text
http://localhost:5000/error
```

The application will display logs containing `ERROR`.

## Requirements

* Python 3.x
* Flask
* python-dotenv
* Linux system with `journalctl`

Install dependencies:

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file:

```env
LOG_COMMAND=journalctl
PORT=5000
DEBUG=False
```

The application uses `journalctl` by default if `LOG_COMMAND` is not specified.

## Usage

Run the application:

```bash
python app.py
```

The API will be available at:

```text
http://localhost:5000
```

## Technologies

* Python
* Flask
* Linux
* journalctl
* Environment Variables
* python-dotenv
