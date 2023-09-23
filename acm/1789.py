s = int(input())

n = 0

m = 0

for i in range(1, s):

	n += i	

	if n > s:

		m = i - 1

		break

	elif n == s:

		m = i

if s == 1 or s == 2:

	print(1)

else:	

    print(m)