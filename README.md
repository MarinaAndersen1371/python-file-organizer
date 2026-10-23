# Python File Organizer

A Python script that automatically organizes files into folders based on their file extensions.

## Features

- Organizes files into categories such as Images, Documents, Spreadsheets, Videos, Audio, and Archives.
- Places unrecognized file types into an `Others` category.
- Prevents filename collisions by adding a number to duplicate filenames.
- Supports a dry-run mode to preview changes without moving files.
- Supports live mode to move files automatically.
- Creates the `to_organize` source folder if it doesn't exist.
- Displays a summary of organized or planned files by category.

## Requirements

- Python
- [uv](https://docs.astral.sh/uv/) for running the script

## Usage

Run these commands from the project directory.

### 1. Preview changes (dry-run mode)

```bash
uv run organizer.py
```

By default, the script previews the planned moves without moving files.

### 2. Organize files (live mode)

```bash
uv run organizer.py --live
```

This moves files into category folders inside `to_organize`.

**Warning:** Live mode changes the locations of files. Review the dry-run output before running it.

## Supported File Types

| Category | Extensions |
|---|---|
| Images | `.jpg`, `.jpeg`, `.png`, `.gif`, `.svg` |
| Documents | `.pdf`, `.docx`, `.doc`, `.txt` |
| Spreadsheets | `.csv`, `.xlsx`, `.xls` |
| Videos | `.mp4`, `.mov`, `.avi` |
| Audio | `.mp3`, `.wav`, `.m4a` |
| Archives | `.zip`, `.rar`, `.7z` |
| Others | Any unsupported extension |

## Project Structure

```text
file_organizer/
├── organizer.py
├── README.md
├── .gitignore
└── to_organize/
    ├── example.jpg
    └── Images/
```

The `to_organize` folder is created automatically when the script runs. Files placed there are organized into category subfolders when live mode is enabled.

## Learning Goals

This project practices Python fundamentals, including:

- `pathlib` for file and folder paths
- Dictionaries and loops
- Functions
- Conditional statements
- File operations with `shutil`
- Command-line arguments with `argparse`
- Safe preview mode and filename collision handling