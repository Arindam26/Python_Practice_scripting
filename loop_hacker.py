def loop(n):
    if n > 0:
        for i in range(n):
            print(i*i, sep='')

    else:
        print("Enter a positive number")


a = int(input())
loop(a)
