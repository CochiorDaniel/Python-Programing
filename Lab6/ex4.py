import os
import sys
from collections import defaultdict


def count_files(directory):
    try:
        if not os.path.exists(directory):
            print(f"The directory {directory} does not exist.")
            return

        if not os.path.isdir(directory):
            print(f"{directory} is not a directory.")
            return

        extension_counts = defaultdict(int)

        file_exists = False
        for root, dirs, files in os.walk(directory):
            for file in files:
                extension = os.path.splitext(file)[1]
                extension_counts[extension] += 1
                file_exists = True

        if not file_exists:
            print(f"The directory {directory} is empty.")
            return

        for extension, count in extension_counts.items():
            print(f"{extension}: {count}")

    except PermissionError:
        print(f"No permission to read the directory {directory}")
    except Exception as e:
        print(f"An error occurred: {e}")


if len(sys.argv) != 2:
    print("Usage: python script.py <directory>")
else:
    count_files(sys.argv[1])
