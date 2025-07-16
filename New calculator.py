while True:
    try:
        a = float(input("Введите первое число:"))
        b = float(input("Введите второе число:"))
        c = input("Введите операцию, которую хотите совершить (+, -, *, /):")

        if c == "+":
            res = a + b
        elif c == "-":
            res = (a - b)
        elif c == "/":
            res = (a / b)
        elif c == "*":
            res = a * b
        elif c == "!=":
            res = (a != b)
        else:
            print("Операция не верная")
            continue

        print("Результат:", res)

    except ZeroDivisionError as ex:
        print("Предупреждение! Нельзя делить на 0")

    print("Хотите продолжить работу калькулятора?")
    answer = input("Yes or no?")
    if answer != "yes":
        break