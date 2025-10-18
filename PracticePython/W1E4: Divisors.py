N = int(input())
arr = []
for i in list(range(1, N)):
    if N % i == 0:
        arr.append(i)
    else:
        continue
for j in arr:
    print(j)
