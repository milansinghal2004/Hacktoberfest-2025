"""
Test cases:
- Rename one file
- Rename multiple files
- Rename files with extension filter
- Skip directories
"""

from scripts.file_renamer import rename_files
import os


def test_rename_one_file(tmp_path):
    folder = tmp_path / "test_folder"
    folder.mkdir()
    old_file = folder / "old_file.txt"
    with open(old_file, "w") as f:
        f.write("old content")

    rename_files(str(folder), prefix="new")

    assert not old_file.exists()

    assert os.listdir(folder) == ["new_1.txt"]

    with open(folder / "new_1.txt", "r") as f:
        assert f.read() == "old content"


def test_rename_multiple_files(tmp_path):
    folder = tmp_path / "test_folder"
    folder.mkdir()
    filenames = ["a.txt", "b.txt", "c.txt"]
    for name in filenames:
        with open(folder / name, "w") as f:
            f.write("test")

    rename_files(str(folder), prefix="renamed")

    # Check if all files have been renamed
    for name in filenames:
        assert not os.path.exists(folder / name)

    # Check if the new file exists
    assert os.listdir(folder) == [
        "renamed_1.txt",
        "renamed_2.txt",
        "renamed_3.txt",
    ]

    for new_name in os.listdir(folder):
        with open(folder / new_name) as f:
            assert f.read() == "test"


def test_rename_files_with_extension_filter(tmp_path):
    """
    Test that only files with a specific extension are renamed.
    """
    folder = tmp_path / "test_folder"
    folder.mkdir()
    files = {
        "file1.txt": "content1",
        "file2.jpg": "content2",
        "file3.ext": "content3",
        "file4.jpg": "content4",
    }

    for name, content in files.items():
        with open(folder / name, "w") as f:
            f.write(content)

    rename_files(str(folder), prefix="img", extension=".jpg")

    assert os.listdir(folder) == [
        "file1.txt",
        "file3.ext",
        "img_1.jpg",
        "img_2.jpg",
    ]

    for name in os.listdir(folder):
        if name.endswith(".jpg"):

            # Check if new file is exist
            assert os.path.exists(folder / name)

            with open(folder / name, "r") as f:
                if name == "img_2.jpg":
                    assert f.read() == "content4"
                elif name == "img_1.jpg":
                    assert f.read() == "content2"
        else:
            assert os.path.exists(folder / name)


def test_skip_derectories(tmp_path):
    folder = tmp_path / "test_folder"
    folder.mkdir()
    subfolder = folder / "subdir"
    subfolder.mkdir()
    file = folder / "file.txt"
    with open(file, "w") as f:
        f.write("Test")

    rename_files(str(folder), prefix="new")

    assert subfolder.exists()
    assert subfolder.is_dir()
    assert not file.exists()
    assert (folder / "new_1.txt").exists()
