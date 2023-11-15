import os
import sys


def calculate_total_size(directory):
    try:
        if not os.path.isdir(directory):
            print(f"Error: The directory {directory} does not exist.")
            return

        if not os.path.isdir(directory):
            print(f"{directory} is not a directory.")
            return

        total_size = 0
        for root, dirs, files in os.walk(directory):
            for f in files:
                fp = os.path.join(root, f)
                if not os.path.islink(fp):
                    total_size += os.path.getsize(fp)

        print(f"Total size of {directory} is {total_size} bytes")

    except Exception as e:
        print(f"Error: {str(e)}")


if len(sys.argv) != 2:
    print("Usage: python script.py <directory_path>")
else:
    calculate_total_size(sys.argv[1])

