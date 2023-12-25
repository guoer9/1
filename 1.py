#艾尔登法环自动保存 就是玩游戏每一次存档都要手动退出来 复制粘贴保存存档，以便回档。正好我学了python，
#就编写了一个自动复制粘贴回档的小小程序，正所谓“人生苦短，我学python” 打怪我不行，回档还是快
import os
import shutil
import subprocess
from datetime import datetime

def copy_(source_folder):
    # Check if the source folder exists
    if not os.path.exists(source_folder):
        return "Source folder does not exist."

    # Determine the parent folder and the new folder path with a timestamp
    parent_folder = os.path.dirname(source_folder)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    new_folder_name = os.path.basename(source_folder) + "_" + timestamp
    new_folder_path = os.path.join(parent_folder, new_folder_name)

    # Create the new folder if it does not exist
    if not os.path.exists(new_folder_path):
        os.makedirs(new_folder_path)

    # Copy all files from the source folder to the new folder
    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)
        if os.path.isfile(file_path):
            # Generate a new filename with timestamp
            new_filename = timestamp + "_" + filename
            new_file_path = os.path.join(new_folder_path, new_filename)
            shutil.copy(file_path, new_file_path)

    return f"All files copied to {new_folder_path}"

def open_folder(folder_path):
    # Check if the folder exists
    if not os.path.exists(folder_path):
        return "Folder does not exist."

    # Open the folder in the default file explorer
    subprocess.Popen(f'explorer "{folder_path}"')
    return f"Folder '{folder_path}' opened."

# Example usage
folder_path = "C:\\Users\\果儿\\AppData\\Roaming\\EldenRing"
result = open_folder(folder_path)
result