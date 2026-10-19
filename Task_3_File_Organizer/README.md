
# File Organizer

## Datheon Python Programming Internship — Task 3

### Project Overview

The File Organizer is a Python command-line application that automatically organizes files into folders based on their extensions.

It helps users keep directories organized by moving different types of files into appropriate categories.

### Features

* Organizes files based on their extensions.
* Supports Documents, Images, Videos, Audio, Archives, and Code.
* Places unrecognized file types in an Others folder.
* Prevents overwriting existing files by automatically renaming duplicates.
* Skips existing directories.
* Handles file access errors.
* Displays a summary after organizing files.

### Technologies Used

* Python 3
* os module
* shutil module
* pathlib module

### How to Run

Open a terminal in the main internship project folder and execute:

```powershell
python .\Task_3_File_Organizer\organizer.py
```

When prompted, enter the path of the folder you want to organize.

For testing, use:

```text
.\Task_3_File_Organizer\sample_files
```

### Example

**Before organizing:**

```text
sample_files/
├── report.pdf
├── photo.jpg
├── notes.txt
├── video.mp4
└── program.py
```

**After organizing:**

```text
sample_files/
├── Documents/
│   ├── report.pdf
│   └── notes.txt
├── Images/
│   └── photo.jpg
├── Videos/
│   └── video.mp4
└── Code/
    └── program.py
```

### Duplicate File Handling

If a file with the same name already exists in the destination folder, the application adds a number to the new filename.

Example:

`notes.txt` → `notes_1.txt`

This prevents the existing file from being overwritten.

### Testing Results

* Five sample files organized successfully.
* Duplicate filename handling verified.
* No errors encountered during testing.

### Safety Note

The application moves files rather than copying them. Test it on a sample directory before using it on important personal files.

### Author

Developed as part of the Datheon Python Programming Internship.
