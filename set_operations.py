n = int(input())
s = set(map(int, input().split()))
for i in range(int(input())):
    c, b = input().split()
    if c == 'intersection_update':
        s &= set(map(int, input().split()))
    elif c == 'update':
        s |= set(map(int, input().split()))
    elif c == 'symmetric_difference_update':
        s ^= set(map(int, input().split()))
    elif c == 'difference_update':
        s -= set(map(int, input().split()))
    else:
        print("Enter proper command")
print(sum(s))
