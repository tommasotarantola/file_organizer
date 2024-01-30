import file_manager

while True:
    print("\n---------------------------------")
    print("------ PYTHON FILE MANAGER ------\n")
    print("1:\tMultirename manager\n2:\tFolder size exitimator\nENTER:\tto exit")
    action = input("Define action:")
    if action == "": break
    elif action == "1" : file_manager.cst_multirename_manager()
    elif action == "2" : file_manager.cst_subfolder_size_manager()
    else : print("Not a valid action.")


file_manager.cst_subfolder_size_manager()