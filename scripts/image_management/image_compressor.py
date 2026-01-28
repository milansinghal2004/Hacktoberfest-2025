from PIL import Image
import os

def compress_image(input_path, output_path, quality=70):
    """
    Compress a single image and save it.

    Args:
        input_path (str): Path to the original image.
        output_path (str): Path to save the compressed image.
        quality (int, optional): Compression quality (1-95). Lower means smaller file. Defaults to 70.
    
    Example:
        >>> compress_image("input.jpg", "compressed.jpg", quality=60)
    """
    try:
        with Image.open(input_path) as img:
            img.save(output_path, "JPEG", optimize=True, quality=quality)
            print(f"Compressed: {input_path} -> {output_path}")
    except Exception as e:
        print(f"Error compressing {input_path}: {e}")

def compress_folder(folder_path, output_folder, quality=70):
    """
    Compress all images in a folder and save them to the specified output folder.

    Args:
        folder_path (str): Path to the input folder containing images.
        output_folder (str): Path to save compressed images.
        quality (int, optional): Compression quality (1-95). Defaults to 70.
    
    Example:
        >>> compress_folder("images", "compressed_images", quality=60)
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for filename in os.listdir(folder_path):
        input_file = os.path.join(folder_path, filename)
        output_file = os.path.join(output_folder, filename)

        # Only process files that are images (JPEG or PNG)
        if os.path.isfile(input_file):
            if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
                compress_image(input_file, output_file, quality)

if __name__ == "__main__":
   # Example usage:

    # Compress a single image
    # compress_image("input.jpg", "compressed.jpg", quality=70)
    
    # Compress all images in a folder
    compress_folder("images", "compressed_images", quality=60)
