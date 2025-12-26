def main():
    while True:
        try:
            sum1 = int(input("Enter first number: "))
        except:
            print("Enter a number!")
        else:
            break

    while True:
        try:
            sum2 = int(input("Enter second number: "))
        except:
            print("Enter a number!")
        else:
            break

    choice(sum1,sum2)

def choice(sum1,sum2):
    while True:
        print("Choice")
        print("1. +")
        print("2. -")
        print("3. *")
        print("4. /")
        print("5. square")
        print("6. quit")

        try:
            choice1 = int(input("Enter your choice: "))
        except:
            print("===Enter a 1-5===")

        if choice1 == 1:
            print(plus(sum1,sum2))
        elif choice1 == 2:
            print(minus(sum1,sum2))
        elif choice1 == 3:
            print(multiplication(sum1,sum2))
        elif choice1 == 4:
            print(division(sum1,sum2))
        elif choice1 == 5:
            print(square(sum1,sum2))
        elif choice1 == 6:
            print("Quiting")
            quit()
        else:
            print("===Enter a valid choice===")

def plus(sum1, sum2):
    sum3 = sum1 + sum2
    return f"{sum1} + {sum2} = {sum3}"

def minus(sum1, sum2):
    sum3 = sum1 - sum2
    return f"{sum1} - {sum2} = {sum3}"

def multiplication(sum1, sum2):
    sum3 = sum1 * sum2
    return f"{sum1} * {sum2} = {sum3}"

def division(sum1, sum2):
    if sum2 == 0:
        return "===Division by zero=="
    sum3 = sum1 / sum2
    return f"{sum1} / {sum2} = {sum3}"

def square(sum1, sum2):
    sum3 = sum1 ** sum2
    return f"{sum1}^{sum2} = {sum3}"


if __name__ == "__main__":
    main()