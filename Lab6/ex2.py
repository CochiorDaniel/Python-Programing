import os
import sys


def rename_files(directory):
    try:
        if not os.path.isdir(directory):
            print(f"Error: The directory {directory} does not exist.")
            return

        files = os.listdir(directory)

        for i, filename in enumerate(files, start=1):

            base, ext = os.path.splitext(filename)
            new_filename = f"file{i}{ext}"

            old_file = os.path.join(directory, filename)
            new_file = os.path.join(directory, new_filename)

            try:
                os.rename(old_file, new_file)
            except Exception as e:
                print(f"Error renaming file {filename}: {str(e)}")

    except Exception as e:
        print(f"Error: {str(e)}")


if len(sys.argv) != 2:
    print("2 args required: python script.py <directory>")
else:
    rename_files(sys.argv[1])
