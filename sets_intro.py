"""Output Format

Output the average height value on a single line.

Sample Input

10
161 182 161 154 176 170 167 171 170 174
Sample Output

169.375
"""

n = int(input())
k = set(map(int, input().split()[:n]))
print(sum(k)/len(k))



