n = int(input())
x=[0, 1, 0, 1, 1, 1]
x += (1, 0, 1, 0, 1, 1, 1) *(1001//7)
print("SK" if x[n]==1 else "CY")