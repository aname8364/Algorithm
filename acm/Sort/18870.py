import sys
from collections import Counter, defaultdict
input = sys.stdin.readline
input()
m = list(map(int, input().split()))
index_map = defaultdict(int)
for i, num in enumerate(sorted(Counter(m))):
    index_map[num] = i
v = [index_map[n] for n in m]
print(*v)