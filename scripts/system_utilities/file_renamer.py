import os

def rename_files(folder_path, prefix="file", extension=None):
    """
    Rename all files in a folder with a given prefix and optional extension filter.

    Args:
        folder_path (str): Path to the folder containing files to rename.
        prefix (str, optional): New prefix for renamed files. Defaults to "file".
        extension (str, optional): If provided, only rename files with this extension (e.g., ".txt").
    
    Example:
        >>> rename_files("my_folder", prefix="image", extension=".jpg")
        # Renames all .jpg files in "my_folder" to image_1.jpg, image_2.jpg, etc.
    """
    files = os.listdir(folder_path)
    count = 1
    
    for filename in files:
        old_path = os.path.join(folder_path, filename)
        
        # Skip if not a file
        if os.path.isfile(old_path):
            # If extension filter is enabled, skip unmatched files
            if extension and not filename.endswith(extension):
                continue
            
            # Extract original file extension
            file_ext = os.path.splitext(filename)[1]
            
            # Construct new filename with prefix and count
            new_name = f"{prefix}_{count}{file_ext}"
            new_path = os.path.join(folder_path, new_name)
            
            os.rename(old_path, new_path)
            print(f"Renamed: {filename} -> {new_name}")
            
            count += 1
