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
    new_name = new_name.replace(" ", "_")

    if new_name[-4:] not in ['.jpg', 'jpeg', '.png']:
        new_name += ".png"

    # Define paths
    src_path = os.path.join('booksite', 'static', 'tempCover.png')
    dest_dir = os.path.join('booksite', 'static', 'cover')
    # Ensure the destination directory exists
    os.makedirs(dest_dir, exist_ok=True)

    dest_path = os.path.join(dest_dir, new_name)
    if os.path.isfile(dest_path):
        # If the file already exists, rename it with a timestamp
        new_name = f"{new_name[:-4]}_{int(time.time())}{new_name[-4:]}"
        new_name = new_name.replace(" ", "_")

    dest_path = os.path.join(dest_dir, new_name)

    # Move and rename the file
    if os.path.isfile(src_path):
        try:
            shutil.move(src_path, dest_path)
            return 0, new_name
        except Exception as e:
            return str(e)
    return 400, "no file to move"

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
