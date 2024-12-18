import os

def organize_files_by_extension(directory):
    """
    Organize files in the given directory into subdirectories based on file extensions.

    :param directory: Path to the directory to organize
    """
    if not os.path.exists(directory):
        print(f"The directory {directory} does not exist.")
        return

    # List all items in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Extract file extension
        file_extension = os.path.splitext(filename)[1].lower()

        # Handle files without extensions
        folder_name = file_extension[1:] if file_extension else "no_extension"

        # Create the folder if it doesn't exist
        folder_path = os.path.join(directory, folder_name)
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)

        # Move the file to the corresponding folder
        new_path = os.path.join(folder_path, filename)
        os.rename(file_path, new_path)
        print(f"Moved: {filename} -> {folder_name}/")

if __name__ == "__main__":
    # Specify the directory to organize
    directory_to_organize = input("Enter the directory path to organize: ").strip()
    organize_files_by_extension(directory_to_organize)
