# https://www.acmicpc.net/problem/1920

"""
5
4 1 5 2 3
5
1 3 7 9 5
"""

"""
	51852 kb 200 ms
"""
n = int(input())
x = list(map(int, input().split()))

z = {i:True for i in x}

m = int(input())
v = list(map(int, input().split())) 

for n in v:
  try:
  	if z[n]:
    	print(1)
  except:
    print(0)


"""
O(n^2)
		46732 kb 460 ms
"""

def f(arr, num):
  g, h = 0, len(arr)-1
  
  while g <= h:
    k = (g+h) // 2
    if arr[k] == num:
      return 1
    elif arr[k] > num:
      h = k - 1
    else:
      g = k + 1
  return 0
      
  
n = int(input())
x = list(map(int, input().split()))
m = int(input())
v = list(map(int, input().split())) 

x.sort()

for n in v:
  print(f(x, n))

"""
	50412 kb 172 ms
"""
n = int(input())
x = set(map(int, input().split()))

m = int(input())
v = list(map(int, input().split())) 

for n in v:
  if n in x:
      print(1)
  else:
      print(0)