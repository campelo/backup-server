import os

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
def ensure_folder_exists(folder_name):
    if not os.path.exists(folder_name)
        os.makedirs(folder_name)
