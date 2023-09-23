import sys
input = sys.stdin.readline

n = int(input())

arr = {}

# wow i hate mobile backjoon

for i in range(n):

    v = list(map(int, input().split()))

    if v[0] == 1:

        x, w = v[1], v[2]

        arr[w] = x

    elif v[0] == 2:

        w = v[1]

        print(arr[w])