import os
import string

# for r, d, f in os.walk("c:\\"):
#     for each_file in f:
#         if each_file == req_file:
#             print(os.path.join(r,each_file))
#
import platform

req_file = input("Please enter the file name to be searched: ")
if platform.system() == "Windows":
    pd_names = string.ascii_uppercase
    vd_names = []
    for each_drive in pd_names:
        if os.path.exists(each_drive + ":\\"):
            vd_names.append(each_drive + ":\\")
    print(vd_names)
    for each_drive in vd_names:
        for r, d, f in os.walk(each_drive):
            for each_file in f:
                if each_file == req_file:
                    print(os.path.join(r, each_file))
else:
    for r, d, f in os.walk("/"):
        for each_file in f:
            if each_file == req_file:
                print(os.path.join(r, each_file))
