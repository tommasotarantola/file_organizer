import file_manager

while True:
    print("\n")
    print("--------------------------------")
    print("-------- PYTHON TOOLBOX --------\n")
    print("1:\tMultirename manager")
    print("2:\tFolder size exitimator")
    print("3:\tImage type conversion (JPG, PNG, ICO..)")
    print("4:\tImage size conversion (width, height)")
    print("5:\tPDF from JPG generator")
    print("6:\tPDF from JPG generator")
    print("ENTER:\tto exit")
    action = input("Define action:")
    if action == "": break
    elif action == "1": file_manager.cst_multirename_manager()
    elif action == "2": file_manager.cst_subfolder_size_manager()
    elif action == "3": file_manager.cst_image_type_converter_manager()
    elif action == "4": file_manager.cst_image_size_converter_manager()
    elif action == "5": file_manager.cst_pdf_generator_manager()
    elif action == "6": file_manager.cst_pdf_merger_manager()
    else: print("Not a valid action.")
