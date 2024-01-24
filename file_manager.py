import os

def cst_get_folder_size(folder_path:str, unit="MB", loud=True):
    size = 0
    for path, dirs, files in os.walk(folder_path):
        for f in files:
            fp = os.path.join(path, f)
            size += os.path.getsize(fp)
    if unit == "KB": show_size = size / (1024)
    elif unit == "MB": show_size = size / (1024 * 1024)
    elif unit == "GB": show_size = size / (1024 * 1024 * 1024)
    else: raise("Not valid unit, pleas choose ('KB', 'MB', 'GB')")

    if loud: print(f"{folder_path}: {round(show_size, 2)} {unit}")
    return size


def cst_get_subfolder_size(folder_path:str, unit="MB", loud=True):
    subfolders = [obj.path for obj in os.scandir(folder_path) if obj.is_dir()]
    sizes = []
    for folder in subfolders:
        sizes.append({"folder": folder, "size": cst_get_folder_size(folder, unit, loud)})
    return sizes

def cst_multirename_manager():

    while True:
        folder_path = input("\n------ PYTHON FILE RENAMER ------\n\nInsert doc folder path: ")
        os.chdir(folder_path)
        print(f"Setted work directory: {folder_path}")

        recursive = input("\nDo you want contents of folders? (TRUE, FALSE)\n")
        if recursive.upper() in ("T", "TRUE"): recursive = True
        elif recursive.upper() in ("F", "FALSE"): recursive = False
        else:
            print("Command not recognized")
            break

        # Finding files
        if recursive:
            old_file_list = []
            for root, dirs, files in os.walk(os.getcwd()):
                for file in files:
                    old_file_list.append(os.path.join(root, file))
        else:
            old_file_list = os.listdir()

        # Generate a text file with the file names
        with open('FILE_RENAME.txt', 'w') as file:
            file.write('\n'.join(old_file_list))

        # Wait for the user to modify the file
        input("Please modify the 'FILE_RENAME.txt' file with the new names. Press Enter to continue...\n")

        # Read the modified names from the file
        with open('FILE_RENAME.txt', 'r') as file:
            new_file_list = file.read().splitlines()

        if len(old_file_list) != len(new_file_list):
            print("File not correctly modified! Number of elements unaligned")

        # Rename the files based on the modified names
        for old_name, new_name in zip(old_file_list, new_file_list):
            if old_name != new_name:
                os.rename(old_name, new_name)
                print(f"Renamed '{old_name}' to '{new_name}'")
        print("\nFile renaming completed.\n\n\n")


