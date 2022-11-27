def elect(x, y, z):
    if x + y + z >= 2:
        return 1
    else:
        return 0


a = input().split(" ")
x = int(a[0])
y = int(a[1])
z = int(a[2])

if elect(x, y, z):
    print(1)
else:
    print(0)
