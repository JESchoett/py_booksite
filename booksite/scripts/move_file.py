import os
import shutil

# Move the scraped img to the /booksite/static/cover folder
def move_file(new_name):
    # Define paths
    src_path = os.path.join('booksite', 'static', 'tempCover.png')
    dest_dir = os.path.join('booksite', 'static', 'cover')
    dest_path = os.path.join(dest_dir, new_name)

    if not dest_path.endswith(".png"):
        dest_path += ".png"

    # Ensure the destination directory exists
    os.makedirs(dest_dir, exist_ok=True)
    if os.path.isfile(dest_path):
        return "file name already exists"

    # Move and rename the file
    if os.path.isfile(src_path):
        try:
            shutil.move(src_path, dest_path)
            return 0
        except Exception as e:
            return str(e)
    return "no file to move"