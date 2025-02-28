#Палиндром

num = int(input("Введите трехзначное число:"))

delenie = 10

first_num = num % delenie

second_num = (num // delenie) % delenie

third_num = num // (delenie * delenie)

reversed_num = first_num * 100 + second_num * delenie + third_num

if num == reversed_num:
    print("This is palindrom")
else:
    print("This is not palindrom")
