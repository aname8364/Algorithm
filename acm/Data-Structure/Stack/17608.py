count = int(input())
st = []
for i in range(count):
    n = int(input())
    while st and st[-1] <= n:
        st.pop()
    st.append(n)
print(len(st))
    