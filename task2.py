scan = int(input())
minval = 0
for i in range(scan, 1, -1):
    if scan % i == 0:
        minval = i
print(minval)
