import argparse  # module lets scripts accept options from the terminal.
import shutil  # Python standard-library module that lets us move files between folders.
from pathlib import Path

parser = argparse.ArgumentParser(description="Organize files by type")
parser.add_argument(
    "--live",  # switches to actual file moving
    action="store_true",
    help="Actually move files instead of previewing changes",
)

args = parser.parse_args()
DRY_RUN = not args.live  # dry-run is enabled unless you explicitly pass --live
# uv run organizer.py --live --> to desable dry-run and actually move files


SOURCE_DIR = Path("to_organize")
SOURCE_DIR.mkdir(exist_ok=True)


FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".svg"],
    "Documents": [".pdf", ".docx", ".doc", ".txt"],
    "Spreadsheets": [".csv", ".xlsx", ".xls"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Audio": [".mp3", ".wav", ".m4a"],
    "Archives": [".zip", ".rar", ".7z"],
}


def get_category(file):
    extension = file.suffix.lower()

    for category, extensions in FILE_TYPES.items():
        if extension in extensions:
            return category

    return "Others"


category_counts = {}
planned_counts = {}

for file in (
    SOURCE_DIR.iterdir()
):  # .iterdir() gives you the items directly inside that folder.
    if not file.is_file():  # returns True if the item is a file.
        continue  # Executes continue and doesn't try to organize the folder as if it were a file

    category = get_category(file)

    destination_folder = SOURCE_DIR / category

    if not DRY_RUN:
        destination_folder.mkdir(
            exist_ok=True
        )  # creates the destination folder if it doesn't exist.

    destination = destination_folder / file.name  # the full path to the intended file.

    counter = 1

    while destination.exists():  # Check if the destination file already exists
        new_name = f"{file.stem}_{counter}{file.suffix}"
        # Ex. for holiday.jpg: file.stem is "holiday", file.suffix is ".jpg".
        destination = destination_folder / new_name
        counter += 1

    if DRY_RUN:
        print(f"[DRY RUN] Would move: {file.name} -> {destination}")
        planned_counts[category] = planned_counts.get(category, 0) + 1
    else:
        shutil.move(str(file), str(destination))
        print(f"Moved: {file.name} -> {destination}")
        category_counts[category] = category_counts.get(category, 0) + 1

    print("\n========== ORGANIZATION SUMMARY ==========")

    if DRY_RUN:
        print("Mode: DRY RUN (preview only)")
        counts = planned_counts
    else:
        print("Mode: LIVE (files moved)")
        counts = category_counts

    for category, count in sorted(counts.items()):
        print(f"{category}: {count} files")

    print("------------------------------------------")
    print(f"Total files: {sum(counts.values())}")
    print("==========================================")


""" +++++++++++++++++ 1. Checking sample files +++++++++++++++++
from pathlib import Path

source_dir = Path("to_organize")

print("Checking sample files...\n")

if not source_dir.exists():
    print("The to_organize folder was not found.")
else:
    for file in source_dir.iterdir():
        if file.is_file():
            print(file.name)

    print("\nCheck complete!") """
