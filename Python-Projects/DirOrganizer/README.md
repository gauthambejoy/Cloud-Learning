Directory Organizer

A simple Python script that automatically organizes files into folders based on their file extensions.

Features

* Organizes files by extension
* Creates folders automatically
* Checks the directory every 5 seconds
* Logs file operations
* Handles invalid directories
* Can be stopped using `Ctrl+C`

Example

Before:

Downloads/
├── photo.jpg
├── resume.pdf
├── notes.txt
└── script.py

After:

Downloads/
├── jpg/
│   └── photo.jpg
├── pdf/
│   └── resume.pdf
├── txt/
│   └── notes.txt
└── py/
    └── script.py

Requirements

* Python 3.x
* No external libraries required

Usage

Run the script:

python organizer.py

Enter the directory path when prompted:

Enter the path of the directory: /home/user/Downloads

The script will continuously organize new files.

Press `Ctrl+C` to stop it.

Logging

File operations are recorded in:

DirOrganizer.log

Technologies

* Python
* OS/File Handling
* Logging
* Exception Handling

Future Improvements

* Add command-line arguments
* Add duplicate file handling
* Use `watchdog` for real-time file monitoring
* Run as a Linux `systemd` service
