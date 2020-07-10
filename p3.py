n = int(input())
sets = set()
sum_list = 0
for i in input().split():
    l = int(i)
    sets.add(l)
    sum_list += l
print(sum_list)
print(sum(sets))
print((sum(sets)*n - sum_list)//(n-1))
