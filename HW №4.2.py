from keyword import kwlist
import string

stroka = input("Введите строку:")

proverka = (stroka.count("_") <= 1, stroka not in kwlist , not stroka[0].isdigit(), not stroka == set(string.punctuation) - {"_"} , not any(i.isupper() for i in stroka))
answer = all(proverka)

print(answer)

