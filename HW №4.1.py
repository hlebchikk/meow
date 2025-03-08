#Хэштег
from keyword import kwlist
import string

hastag = "#"

stroka = input("Введите строку:")

trimming_hastag = stroka[:140]
title_stroka = trimming_hastag.title()
delete_punctuation = title_stroka.translate(str.maketrans("", "", string.punctuation)).replace(" ", "")
add_hastag = hastag+delete_punctuation

print(add_hastag)