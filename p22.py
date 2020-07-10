import re

my_list = list()

for i in range(int(input())):
    my_list.append(input())
print(sorted(list(filter(lambda x: re.search(r'[\w\d-]+@[A-Za-z0-9]+\.\w?\w?\w$', x), my_list))))
