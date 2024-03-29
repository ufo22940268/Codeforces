import sys
from itertools import product

file = sys.stdin
#file = open("test", "r")

n, m  = map(int, file.readline().rstrip().split())
matrix = [[0 for _ in range(1005)] for _ in range(1005)]
p = []

for i in range(1, m + 1):
    x, y  = map(int, file.readline().rstrip().split())
    matrix[x][y] = i
    p.append((x, y))


def isOk(x, y):
    global matrix
    for lx, ly in [(lx, ly) for lx in range(x, x + 3) for ly in range(y, y + 3)]:
        if matrix[lx][ly] == 0: return False
    else:
        return True

def maxIndex(x, y):
    global matrix
    maxV = 0
    for lx, ly in [(lx, ly) for lx in range(x, x + 3) for ly in range(y, y + 3)]:
        maxV = max(maxV, matrix[lx][ly])
    return maxV



ans = 1 << 31
for x, y in [(t[0], t[1]) for t in p]:
    if isOk(x, y):
        ans = min(ans, maxIndex(x, y))
    if matrix[x][y] > ans:
        break


if ans == 1 << 31:
    print "-1"
else:
    print ans
