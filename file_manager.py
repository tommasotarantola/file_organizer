import os
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

img_formats = (
    ".jpg", ".jpeg", ".png", ".gif", ".webp", ".tiff", ".bmp", ".svg",
    ".psd", ".ai", ".eps", ".raw", ".cr2", ".nef", ".orf", ".sr2",
    ".heif", ".avif", ".ico", ".tif", ".indd", ".jp2", ".j2k", ".jpf",
    ".jpx", ".jpm", ".mj2", ".svgz", ".dwg", ".dxf", ".xcf", ".wmf",
    ".emf"
)

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
        print("\n------ SIZE MANAGER\n")
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
        print("\n------ FILE RENAMER\n")
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
    while True:
        print("\n------ JPEG CONVERTER\n")
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


def cst_pdf_generator_manager():
    while True:
        print("\n------ PDF GENERATOR\n")
        folder_path = input("Insert images folder path (ENTER to exit): ")
        if folder_path == "":
            break
        else:
            try:
                os.chdir(folder_path)
            except Exception as err:
                print(err)
                continue
        print(f"Setted work directory: {folder_path}")

        file_list = os.listdir()
        img_list = [file for file in file_list if os.path.splitext(file)[1] in img_formats]
        file_out = folder_path + '\\' + "output.pdf"
        pdf_width, pdf_height = A4
        paper = canvas.Canvas(file_out, pagesize=A4)

        for image_file in img_list:
            with Image.open(image_file) as img:
                img_width, img_height = img.size
                scale = min(pdf_width / img_width, pdf_height / img_height)  # scale to A4 dimension
                new_img_width = img_width * scale
                new_img_height = img_height * scale
                x = (pdf_width - new_img_width) / 2
                y = (pdf_height - new_img_height) / 2

                paper.drawImage(image_file, x, y, width=new_img_width, height=new_img_height)
                paper.showPage()
        try:
            paper.save()
            print("PDF generated.")
        except Exception as err:
            print("Impossible to write pdf file.")
            print(err)

