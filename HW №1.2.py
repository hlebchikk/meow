#Калькулятор
a = int(input("Введите первое число:"))
b = int(input("Введите второе число:"))
c = input("Введите операцию, которую хотите совершить:")

if c == "+":
    res = a + b
elif c == "-":
    res = (a - b)
elif (a == 0 or b == 0) and c == "/":
    res = "You can't divide by 0!"
elif c == "/":
    res = (a / b)
elif c == "*":
    res = a * b
elif c == "!=":
    res = (a != b)
else:
    res = "Error"
print(res)

#Калькулятор Модифицированный
while True:
 a = int(input("Введите первое число:"))
 b = int(input("Введите второе число:"))
 c = input("Введите операцию, которую хотите совершить:")

 if c == "+":
    res = a + b
 elif c == "-":
    res = (a - b)
 elif (a == 0 or b == 0) and c == "/":
    res = "You can't divide by 0!"
 elif c == "/":
    res = (a / b)
 elif c == "*":
    res = a * b
 elif c == "!=":
    res = (a != b)
 else:
    res = "Error"
 print(res)
 print("Хотите продолжить работу калькулятора?")
 answer = input("Yes or no?")
 if answer not in ("yes"):
     break
