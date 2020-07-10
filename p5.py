num = int(input("Enter the number of rows: "))
for i in range(num):
    print(' ' * (num - i - 1) + "*" * (2 * i + 1))

for j in range(num):
    print(' ' * j + "*" * (2 * num - 2 * j - 1))
