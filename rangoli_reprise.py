"""Sample Input

5
Sample Output

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
"""

import string

n = int(input())
char = string.ascii_lowercase
L = []

for i in range(n):
    s = '-'.join(char[i:n])
    L.append((s[::-1] + s[1:]).center(4 * n - 3, '-'))
print('\n'.join(L[:0:-1] + L))
print('\n'.join(L[:0:-1] + L))
