import os

folder_path = "path/to/your/folder"
output_file = "merged.txt"

with open(output_file, 'w') as outfile:
    for filename in os.listdir(folder_path):
        path = os.path.join(folder_path, filename)
        if os.path.isfile(path) and filename.endswith('.txt'):
            with open(path, 'r') as infile:
                outfile.write(infile.read() + "\n")
            print(f"Merged: {filename}")
