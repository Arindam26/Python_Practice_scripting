import re

# # import csv
# #
# # req_file = "info.csv"
# # with open(req_file, 'r') as fo:
# #     data = csv.reader(fo, delimiter="|")
# #     for each in data:
# #         print(each)
#
#
# # print(round(10/3))
# def display(a=1):
#     print("The value of a is : ", a)
#     return None
#
# display(4)
# display(5)
# display()

text = '244.666.888.999'
my_pat = '\d\d\d'
test = re.findall(my_pat, text)
print(str(test).upper())
