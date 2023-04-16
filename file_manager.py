import os
import sys
import datetime
import exifread
import shutil

# save file to a specific folder
def save_file(file_folder, file_name, file_data):
    file_path = os.path.join(file_folder, file_name)
    with open(file_path, 'wb') as f:
        f.write(file_data)

# save file using config folder's name
def save_file(file_name, file_data):
    ensure_folder_exists(config.UPLOAD_FOLDER)
    save_file(config.UPLOAD_FOLDER, file_name, file_data)

# create folder if not exists
def ensure_folder_exists(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# will retrieve all files and move them for a correct folder
def process_folder(folder_path):
    if not os.path.exists(folder_path):
        print(f"{folder_path} not exists.")
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            # Open the file in binary mode and read the EXIF tags
            with open(file_path, 'rb') as f:
                tags = exifread.process_file(f)
                print(tags.keys())
                # Get the original creation date from the EXIF tags
                if 'EXIF DateTimeOriginal' in tags:
                    creation_date = tags['EXIF DateTimeOriginal']
                    creation_date_str = str(creation_date)
                    new_folder = f"{creation_date_str[0:4]}/{creation_date_str[5:7]}/{creation_date_str[8:10]}"
                    new_folder_path = os.path.join(dirpath, new_folder);
                    ensure_folder_exists(new_folder_path)
                    # Use the move() function to move the file
                    shutil.move(file_path, new_folder_path)
                else:
                    # If the creation date is not available in the EXIF tags,
                    # fall back to the file's metadata creation time
                    creation_date = datetime.datetime.fromtimestamp(os.path.getctime(file_path))
                print(f"The original creation date of {file_path}: {creation_date}")

if __name__ == "__main__":
    arg1 = sys.argv[1]
    process_folder(arg1)