scan = input()
# my 1 dump solution
# print(int(scan, 2))

scan2 = scan[::-1]
total = 0
for i in range(len(scan2)):
    num = int(scan2[i], 2)
    total += num * 2 ** i

print(total)
