from keyword import kwlist
import string

activator = True
punctuation = string.punctuation.replace("_", "")
stroka = input("Введите строку:")

if stroka.count("_") > 1:
    activator = False
elif stroka == kwlist:
    activator = False
elif stroka[0].isdigit():
    activator = False
elif stroka == punctuation:
    activator = False
elif stroka.isupper():
    activator = False
elif stroka == " ":
    activator = False

print(activator)
