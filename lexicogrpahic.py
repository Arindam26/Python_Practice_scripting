"""Let's learn about list comprehensions! You are given three integers x, y and z
 representing the dimensions of a cuboid along with an integer .
 Print a list of all possible coordinates given by (i,j,k) on a 3D grid where the sum of i + j +k  is not equal to  n.
 Please use list comprehensions rather than multiple loops"""

x, y, z, n = (int(input()) for _ in range(4))
print([[a, b, c] for a in range(0, x + 1) for b in range(0, y + 1) for c in range(0, z + 1) if a + b + c != n])
