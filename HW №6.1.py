"""
 Преобразование слов в словарь
Условие:
Дан список строк вида "ключ:значение". Напишите функцию, которая превращает этот список в словарь, используя map, lambda и split.

Пример входных данных:

pairs = ["имя:Аня", "город:Одесса", "язык:Python"]
Ожидаемый результат:

{"имя": "Аня", "город": "Одесса", "язык": "Python"}
"""

pairs = ["имя:Аня", "город:Одесса", "язык:Python"]

def convert_pair():
    split_pairs = list(map(lambda x: x.split(":", 1), pairs))
    clean_space =  map(lambda x: (x[0].strip(), x[1].strip()), split_pairs)
    conversion_pairs = dict(clean_space)
    return(conversion_pairs)

print(convert_pair())

"""
 ЗАДАЧА: Фильтрация и нормализация пользовательских настроек
📋 Условие:
У тебя есть список строк, каждая из которых — это потенциальная пользовательская настройка.
Формат корректных строк: "ключ=значение". Некоторые строки могут быть:

с пробелами,

без знака =,

с пустыми ключами или значениями.

🎯 Цель:
Оставить только корректные строки, то есть содержащие один знак =.

Из каждой строки получить пару ключ–значение, обрезать пробелы.

Построить словарь настроек.
"""

raw_settings = [
    "тема = светлая",
    " язык= Python ",
    "режим=",
    "=значение",
    "прозрачность 80",
    "автообновление=вкл"
]

def check(conditions):
    if conditions.count("=") != 1:
       return False

    key , meaning = conditions.split("=", 1)
    strip_key = key.strip()
    strip_meaning = meaning.strip()
    if strip_key and strip_meaning:
        return True
    else:
        return False

fil = filter(check, raw_settings)
split_list = list(map(lambda x: x.split("=", 1), fil))
strip_list = map(lambda x: (x[0].strip().lower(), x[1].strip()), split_list)

convert_list = dict(strip_list)

print(convert_list)

"""
ЗАДАЧА:Распознавание тональности по эмодзи
📋 Условие:
У тебя есть список пользовательских отзывов, каждый из которых заканчивается эмодзи:

😊 → позитив

😐 → нейтрально

😡 → негатив

Нужно превратить этот список в список слов "позитив", "нейтрально" или "негатив", используя map и lambda.
"""

from collections import Counter

def emoji (feedbacks_emoji):
    return feedbacks_emoji.strip()[-1]

feedbacks = [
    "Очень понравилось! 😊",
    "Было нормально 😐",
    "Разочарован 😡",
    "Просто супер! 😊",
    "Так себе 😐"
]

meaning = {"😊" : "positive", "😐" : "netural", "😡" : "negative"}
transformation = map(emoji, feedbacks)
correspondence = tuple(map(lambda x: meaning[x], transformation))
counter_feedbacks = Counter(correspondence)

print(counter_feedbacks)
