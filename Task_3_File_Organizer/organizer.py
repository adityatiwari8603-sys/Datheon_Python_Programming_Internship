"""
DATHEON PYTHON PROGRAMMING INTERNSHIP

Task 3: File Organizer

Description:
Organizes files into folders based on their extensions.
Handles duplicate filenames and generates a summary.
"""

import os
import shutil
from pathlib import Path


FILE_CATEGORIES = {
    "Documents": {".pdf", ".doc", ".docx", ".txt", ".xlsx", ".xls", ".ppt", ".pptx", ".csv"},
    "Images": {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"},
    "Videos": {".mp4", ".avi", ".mkv", ".mov", ".wmv"},
    "Audio": {".mp3", ".wav", ".aac", ".flac"},
    "Archives": {".zip", ".rar", ".7z", ".tar", ".gz"},
    "Code": {".py", ".js", ".html", ".css", ".java", ".cpp", ".c", ".json"},
}


def get_category(extension):
    """Return the folder category for a file extension."""
    for category, extensions in FILE_CATEGORIES.items():
        if extension in extensions:
            return category

    return "Others"


def get_unique_destination(destination):
    """Prevent overwriting an existing file."""

    if not destination.exists():
        return destination

    counter = 1

    while True:
        new_name = (
            f"{destination.stem}_{counter}{destination.suffix}"
        )

        new_destination = destination.with_name(new_name)

        if not new_destination.exists():
            return new_destination

        counter += 1


def organize_files(folder_path):
    """Organize files into category folders."""

    folder = Path(folder_path).expanduser().resolve()

    if not folder.exists():
        print("\nError: The selected folder does not exist.")
        return

    if not folder.is_dir():
        print("\nError: The selected path is not a folder.")
        return

    summary = {}
    moved_count = 0
    skipped_count = 0
    error_count = 0

    print(f"\nOrganizing folder: {folder}")
    print("-" * 60)

    try:
        with os.scandir(folder) as entries:
            for entry in entries:

                try:
                    if not entry.is_file(follow_symlinks=False):
                        skipped_count += 1
                        continue

                    source = Path(entry.path)
                    extension = source.suffix.lower()
                    category = get_category(extension)

                    destination_folder = folder / category
                    destination_folder.mkdir(exist_ok=True)

                    destination = destination_folder / source.name
                    destination = get_unique_destination(destination)

                    shutil.move(str(source), str(destination))

                    summary[category] = summary.get(category, 0) + 1
                    moved_count += 1

                    print(f"[MOVED] {source.name} -> {category}/{destination.name}")

                except (PermissionError, OSError) as error:
                    error_count += 1
                    print(f"[ERROR] {entry.name}: {error}")

    except (PermissionError, OSError) as error:
        print(f"\nUnable to read folder: {error}")
        return

    print("\n" + "=" * 60)
    print("FILE ORGANIZATION SUMMARY")
    print("=" * 60)

    for category, count in sorted(summary.items()):
        print(f"{category:<15}: {count} file(s)")

    print("-" * 60)
    print(f"Files moved   : {moved_count}")
    print(f"Items skipped : {skipped_count}")
    print(f"Errors        : {error_count}")
    print("=" * 60)


def main():
    """Run the File Organizer."""

    print("=" * 60)
    print("                 FILE ORGANIZER")
    print("=" * 60)

    folder_path = input(
        "\nEnter the folder path to organize: "
    ).strip().strip('"')

    if not folder_path:
        print("\nError: Folder path cannot be empty.")
        return

    organize_files(folder_path)


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n\nProgram interrupted. Goodbye!")