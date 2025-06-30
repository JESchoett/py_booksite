import os
import shutil
import time

# Save the uploaded cover image to a temporary file
# This is done, to be able to keep the image in case of an error
def save_cover(cover_img_flaskobject):
    try:
        if os.path.exists("booksite/static/tempCover.png"):
            os.remove("booksite/static/tempCover.png")

        cover_img_flaskobject.save(os.path.join("booksite/static/tempCover.png"))
        return 0

    except Exception as e:
        print("Error when saving the Cover:", e)
        return str(e)

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
        # If the file already exists, rename it with a timestamp
        dest_path = os.path.join(dest_dir, f"{new_name}_{int(time.time())}.png")

    # Move and rename the file
    if os.path.isfile(src_path):
        try:
            shutil.move(src_path, dest_path)
            return 0
        except Exception as e:
            return str(e)
    return "no file to move"

# Remove the file from the /booksite/static/cover folder
def remove_file(file_name):
    # Define paths
    src_dir = os.path.join('booksite', 'static', 'cover')
    src_path = os.path.join(src_dir, file_name)

    # Move and rename the file
    if os.path.isfile(src_path):
        try:
            os.remove(src_path)
        except Exception as e:
            return str(e)
    return 'no file to "remove"'
