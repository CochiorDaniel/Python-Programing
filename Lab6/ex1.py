import os
import sys


def read_files(directory, extension):
    try:
        if not os.path.isdir(directory):
            print(f"Error: The directory {directory} does not exist.")
            return

        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith(extension):
                    try:
                        with open(os.path.join(root, file), 'r') as f:
                            print(f.read())
                    except Exception as e:
                        print(f"Error reading file {file}: {str(e)}")

    except Exception as e:
        print(f"Error: {str(e)}")


if len(sys.argv) != 3:
    print("3 args required: python script.py <directory> <extension>")
else:
    read_files(sys.argv[1], sys.argv[2])
