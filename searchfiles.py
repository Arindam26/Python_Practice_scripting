import os
import platform
import string

req_file = input("Enter the file name to be searched: ")

if platform.system() == "Windows":
    pd_names = string.ascii_uppercase
    vd_names = []
    for drives in pd_names:
        if os.path.exists(drives + ":\\"):
            vd_names.append(drives + ":\\")
    for each_drive in vd_names:
        for r, d, f in os.walk(each_drive):
            for each_file in f:
                if each_file == req_file:
                    print(os.path.join(r, each_file))
