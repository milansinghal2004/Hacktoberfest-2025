# Duplicate File Finder

A Python utility to identify and manage duplicate files based on their content (MD5 hash).

## Features
- **Efficiency**: Compares file sizes first to avoid unnecessary hashing.
- **Recursive**: Scans through all subdirectories.
- **Interactive**: Allows you to delete specific duplicates or keep only one copy via a CLI menu.
- **Safe**: Reads files in blocks to handle large files efficiently.

## Directory Structure
- `duplicate_finder.py`: The main script.
- `demo_files/`: Sample files to test the script.

## Usage
1. Open a terminal in this directory.
2. Run the script:
   ```bash
   python duplicate_finder.py demo_files
   ```
3. Follow the interactive prompts:
   - `d index1,index2`: Delete specific files by their index.
   - `k`: Keep the first file and delete all others in the group.
   - `s`: Skip the group.
   - `q`: Quit.

## Example
```text
Found 1 groups of duplicate files.

Group 1 (MD5: ...):
  [1] demo_files\file1.txt
  [2] demo_files\file2.txt
  [3] demo_files\sub\file4.txt

Options: [d index1,index2] Delete specific, [k] Keep first & delete rest, [s] Skip, [q] Quit
Action: k
```
