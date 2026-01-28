import os
import hashlib
import argparse
from collections import defaultdict
from pathlib import Path

def calculate_hash(file_path, block_size=65536):
    """Calculate the MD5 hash of a file in chunks to handle large files."""
    hasher = hashlib.md5()
    try:
        with open(file_path, 'rb') as f:
            for chunk in iter(lambda: f.read(block_size), b''):
                hasher.update(chunk)
        return hasher.hexdigest()
    except (OSError, PermissionError) as e:
        print(f"Error reading {file_path}: {e}")
        return None

def find_duplicates(directory):
    """Find duplicate files in the given directory and its subdirectories."""
    size_groups = defaultdict(list)
    
    print(f"Scanning directory: {directory}")
    
    # First pass: Group files by size to avoid hashing unique files
    for root, _, files in os.walk(directory):
        for filename in files:
            path = Path(root) / filename
            try:
                if path.is_file():
                    size = path.stat().st_size
                    size_groups[size].append(str(path))
            except (OSError, PermissionError):
                continue

    # Second pass: Hash only files that share the same size
    hash_groups = defaultdict(list)
    potential_duplicates = [paths for size, paths in size_groups.items() if len(paths) > 1]
    
    total_potential = sum(len(p) for p in potential_duplicates)
    if total_potential == 0:
        print("No duplicates found (all files have unique sizes).")
        return {}

    print(f"Checking {total_potential} files with common sizes for content matches...")
    
    for paths in potential_duplicates:
        for path in paths:
            file_hash = calculate_hash(path)
            if file_hash:
                hash_groups[file_hash].append(path)

    # Filter out groups with only one path (not real duplicates)
    duplicates = {h: paths for h, paths in hash_groups.items() if len(paths) > 1}
    return duplicates

def handle_duplicates(duplicates):
    """Interactively manage duplicate files."""
    if not duplicates:
        print("No duplicate files found.")
        return

    print(f"\nFound {len(duplicates)} groups of duplicate files.")
    
    for i, (file_hash, paths) in enumerate(duplicates.items(), 1):
        print(f"\nGroup {i} (MD5: {file_hash}):")
        for idx, path in enumerate(paths, 1):
            print(f"  [{idx}] {path}")
        
        while True:
            cmd = input("\nOptions: [d index1,index2] Delete specific, [k] Keep first & delete rest, [s] Skip, [q] Quit\nAction: ").strip().lower()
            
            if cmd == 'q':
                print("Exiting interactive mode.")
                return
            elif cmd == 's':
                print("Skipping this group.")
                break
            elif cmd == 'k':
                # Keep first, delete others
                to_delete = paths[1:]
                for p in to_delete:
                    try:
                        os.remove(p)
                        print(f"Deleted: {p}")
                    except OSError as e:
                        print(f"Error deleting {p}: {e}")
                break
            elif cmd.startswith('d'):
                try:
                    indices_str = cmd[1:].strip()
                    indices = [int(x.strip()) for x in indices_str.replace(',', ' ').split()]
                    
                    # Validate indices
                    if any(idx < 1 or idx > len(paths) for idx in indices):
                        print(f"Invalid indices. Please choose between 1 and {len(paths)}.")
                        continue
                    
                    # Sort indices in reverse to avoid shifting problems if we used list indices, 
                    # but here we use paths directly.
                    for idx in sorted(indices, reverse=True):
                        p = paths[idx-1]
                        try:
                            os.remove(p)
                            print(f"Deleted: {p}")
                        except OSError as e:
                            print(f"Error deleting {p}: {e}")
                    break
                except ValueError:
                    print("Error: Please provide numeric indices (e.g., 'd 2,3').")
            else:
                print("Unknown command. Try again.")

def main():
    parser = argparse.ArgumentParser(description="Find and manage duplicate files in a directory.")
    parser.add_argument("directory", help="The directory to scan for duplicates.")
    args = parser.parse_args()

    target_dir = os.path.abspath(args.directory)
    if not os.path.isdir(target_dir):
        print(f"Error: {target_dir} is not a valid directory.")
        return

    duplicates = find_duplicates(target_dir)
    handle_duplicates(duplicates)

if __name__ == "__main__":
    main()
