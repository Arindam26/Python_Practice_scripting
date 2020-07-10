import os
import datetime
import sys

req_path = input("Please enter the required path")
age = 3

if not os.path.exists(req_path):
    print("Please enter a valid path")
    sys.exit(1)

elif os.path.isfile(req_path):
    print("Please provide a directory path: ")
    sys.exit(2)

today = datetime.datetime.now()
for each_file in os.listdir(req_path):
    each_file_path = os.path.join(req_path, each_file)
    if os.path.isfile(each_file_path):
        file_creation_date = datetime.datetime.fromtimestamp(os.path.getctime(each_file_path))
        dif_day = (today - file_creation_date).days
        if dif_day > 3:
            print(each_file_path, dif_day)



