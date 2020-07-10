"""Sample Input 0

12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
Sample Output 0

[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]"""

n = int(input())
lists = []
newList = []
for i in range(n):
    x = input().split()
    lists.append(x)

for i in range(len(lists)):
    if lists[i][0] == 'insert':
        x = int(lists[i][1])
        y = int(lists[i][2])

        newList.insert(x, y)
    elif lists[i][0] == 'print':
        print(newList)
    elif lists[i][0] == 'remove':
        newList.remove(int(lists[i][1]))
    elif lists[i][0] == 'append':
        newList.append(int(lists[i][1]))
    elif lists[i][0] == 'sort':
        newList.sort()
    elif lists[i][0] == 'pop':
        newList.pop()
    elif lists[i][0] == 'reverse':
        newList.reverse()
