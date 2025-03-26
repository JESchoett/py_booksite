import os

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
