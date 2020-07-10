"""Sample Input

chris alan
Sample Output

Chris Alan
"""

n = input().split()

print(' '.join(i.capitalize() for i in n))
