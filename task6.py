def double_power(num, power):
    if power == 0:
        return 1
    elif power == 1:
        return num
    else:
        power = num ** power
        return power


scan = input()
result = scan.split(" ")
print(double_power(float(result[0]), int(result[1])))
