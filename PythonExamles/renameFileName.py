import os
def rename_file():
    file_list = os.listdir(r"E:/1MAC/FullStack_S/PythonExamles/prank")
    print file_list
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "0123456789"))
