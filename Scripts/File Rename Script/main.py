import os
import re


def main():
    path = r'D:\\Spy x Family'
    for filename in os.listdir(path):
        old_path = os.path.join(path, filename)
        if os.path.isfile(old_path):
            new_filename = re.sub(r'\([^)]*\)', '', filename)
            new_filename = re.sub(r'\s+(\.[^.]+)$', r'\1', new_filename)
            new_path = os.path.join(path, new_filename)
            os.rename(old_path, new_path)
            print(f"Renamed '{filename}' to '{new_filename}'")


if __name__ == "__main__":
    main()
