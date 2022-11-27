def add(total):
    print("Enter the amount of money to add")
    money = int(input())
    return total + money


def sub(total):
    print("Enter the amount of money to take")
    money = int(input())
    return total - money


def todollar(total):
    dollar = total / 470
    print(f'You have {dollar}$')
    return dollar


def totenge(total):
    tenge = total * 470
    print(f'You have {tenge}T')
    return tenge


def show(total):
    print(f'You have {total} tenge')


def instruction():
    print(""""Welcome to element bank.Thanks to choosing our bank
              Our bank provides several operations
              Choose your option
              1. Insert your money
              2. Take your money
              3. Show balance
              4. Convert to Dollar
              5. Convert to Tenge
              6. Exit""")


total_overal = 0
while True:
    instruction()
    option = float(input())
    match option:
        case 1:
            total_overal = add(total_overal)
        case 2:
            total_overal = sub(total_overal)
        case 3:
            show(total_overal)
        case 4:
            total_overal = todollar(total_overal)
        case 5:
            total_overal = totenge(total_overal)
        case 6:
            break
