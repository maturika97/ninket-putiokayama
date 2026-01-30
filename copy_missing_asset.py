import shutil
import os

source_dir = "/Users/homepc/.gemini/antigravity/brain/d8a199da-b677-4ee1-9a55-6425764e2a8c/"
dest_dir = "assets/"

files_map = {
    "uploaded_media_1769751756847.jpg": "participants-header.jpg"
}

if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)

for src_name, dest_name in files_map.items():
    src_path = os.path.join(source_dir, src_name)
    dest_path = os.path.join(dest_dir, dest_name)
    try:
        shutil.copy2(src_path, dest_path)
        print(f"Copied {src_name} to {dest_name}")
    except Exception as e:
        print(f"Error copying {src_name}: {e}")
