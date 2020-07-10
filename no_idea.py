"""
Input Format

The first line contains integers  and  separated by a space.
The second line contains  integers, the elements of the array.
The third and fourth lines contain  integers,  and , respectively.

Output Format

Output a single integer, your total happiness.

Sample Input

3 2
1 5 3
3 1
5 7
Sample Output

1
"""

n, m, =input().split()
my_array = input().split()
A = set(input().split())
B = set(input().split())

print(sum((i in A) - (i in B) for i in my_array))
