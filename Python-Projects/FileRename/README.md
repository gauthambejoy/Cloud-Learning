# File Renamer

A simple Python script that renames all files in a directory using a sequential naming format.

## Features

* Renames files automatically
* Uses sequential numbering
* Allows the user to provide the directory path
* Uses Python's built-in `os` module

## Example

Before:

```text
Downloads/
├── photo.jpg
├── document.pdf
├── notes.txt
└── image.png
```

After:

```text
Downloads/
├── File.0.txt
├── File.1.txt
├── File.2.txt
└── File.3.txt
```

## Requirements

* Python 3.x
* No external libraries required

## Usage

Run the script:

```bash
python rename.py
```

Enter the directory path:

```text
Enter the directory path: /home/user/Downloads
```

The files will be renamed automatically.

## Technologies

* Python
* OS/File Handling
* File Renaming

Make sure to run it on a test directory first.
