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


def cst_subfolder_size_manager(unit="MB", loud=True):
    while True:
        print("\n--- SIZE MANAGER\n")
        folder_path = input("Insert doc folder path (ENTER to exit): ")
        if folder_path == "": break
        else :
            try:
                subfolders = [obj.path for obj in os.scandir(folder_path) if obj.is_dir()]
                sizes = []
                for folder in subfolders:
                    sizes.append({"folder": folder, "size": cst_get_folder_size(folder, unit, loud)})
            except Exception as err:
                print(err)
                continue

def cst_multirename_manager():
    while True:
        print("\n--- FILE RENAMER\n")
        folder_path = input("Insert doc folder path (ENTER to exit): ")
        if folder_path == "": break
        else :
            try: os.chdir(folder_path)
            except Exception as err:
                print(err)
                continue

        print(f"Setted work directory: {folder_path}")

        recursive = input("\nDo you want contents of folders? (TRUE, FALSE)\n")
        if recursive.upper() in ("T", "TRUE"): recursive = True
        elif recursive.upper() in ("F", "FALSE"): recursive = False
        else:
            print("Command not recognized")
            continue

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


def cst_jpg_converter_manager():
    from PIL import Image
    img_formats = (
        ".jpg", ".jpeg", ".png", ".gif", ".webp", ".tiff", ".bmp", ".svg",
        ".psd", ".ai", ".eps", ".raw", ".cr2", ".nef", ".orf", ".sr2",
        ".heif", ".avif", ".ico", ".tif", ".indd", ".jp2", ".j2k", ".jpf",
        ".jpx", ".jpm", ".mj2", ".svgz", ".dwg", ".dxf", ".xcf", ".wmf",
        ".emf", ".pdf"
    )
    while True:
        print("\n--- JPEG CONVERTER\n")
        folder_path = input("Insert doc folder path (ENTER to exit): ")
        if folder_path == "": break
        else:
            try: os.chdir(folder_path)
            except Exception as err:
                print(err)
                continue
        print(f"Setted work directory: {folder_path}")

        recursive = input("\nDo you want contents of folders? (TRUE, FALSE)\n")
        if recursive.upper() in ("T", "TRUE"):
            recursive = True
        elif recursive.upper() in ("F", "FALSE"):
            recursive = False
        else:
            print("Command not recognized")
            continue

        # Finding files
        if recursive:
            file_list = []
            for root, dirs, files in os.walk(os.getcwd()):
                for file in files:
                    img_list.append(os.path.join(root, file))
        else:
            file_list = os.listdir()
        img_list = [file for file in file_list if os.path.splitext(file)[1] in img_formats]

        for image_path in img_list:
            name, extension = os.path.splitext(image_path)
            try:
                with Image.open(image_path) as img:
                    img = img.convert('RGB')
                    img.save(f'{name}.jpg', 'JPEG')
            except Exception as err:
                print(err)
        print("\nJPEG conversion completed.\n\n\n")
