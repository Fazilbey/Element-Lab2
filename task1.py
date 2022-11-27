scan = int(input())
scan1 = int(input())

result = []

for i in range(scan,scan1+1):
    if i % 2 == 0:
        result.append(i)
print(*result)