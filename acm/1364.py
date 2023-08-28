n=int(input())

x=[0]

x+=[0]*1000005

x[1]=1

v=1

i=2

while True:

    x[i] = x[i-1] + v

    x[i+1] = x[i] + v

    x[i+2] = x[i+1] + v

    x[i+3] = x[i+2] + v

    x[i+4] = x[i+3] + v+1

    x[i+5] = x[i+4] + v

    v += 1

    i += 6

    

    if i>n:

        break

print(x[n])

# coded on mobile