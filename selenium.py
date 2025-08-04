from selenium import webdriver
from selenium.webdriver.common.by import By
from string import punctuation

# Запускаем браузер и открываем сайт
driver = webdriver.Chrome()
driver.get("https://www.work.ua/jobs-odesa-it")

vacancy_container = driver.find_element(By.ID, "pjax-jobs-list")

vacancy_cards = vacancy_container.find_elements(By.CLASS_NAME, "card")

cyrillic_letters = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
letters = cyrillic_letters + cyrillic_letters.upper()

#Удаляем из пунктуации дефис
punct_to_remove = punctuation.replace("-", " ")

#Сюда будут складываться все зарплаты
raw_salaries = []

for i in vacancy_cards:
    strong_600 = i.find_elements(By.CLASS_NAME, "strong-600")
    for j in strong_600:
        if "грн" not in j.text:
            continue
        raw_salaries.append(j.text)

salaries = []
# Обрабатываем каждый элемент с "зарплатой"
for i in raw_salaries:
    text = i.strip()

    # Удаляем неразрывные пробелы и обычные пробелы
    text = text.replace('\u202f', '').replace('\u2009', '').replace(' ', '')

    # Пропускаем, если вообще нет цифр
    if not any(j.isdigit() for j in text):
        continue

    #Меняем толстый дефис на обычный, так как зарплаты обозначены им
    text = text.replace("–", "-")

    # Удаляем кириллицу и знаки препинания
    for l in text:
        if l in letters or l in punct_to_remove:
            text = text.replace(l, "")

    # Разбиваем диапазон зарплат по дефису
    digits_text = text.split("-")

    #Превращаем все в целые числа, если вылазит ошибка, говорим об этом и пропускаем число
    try:
        digits = list(map(int, digits_text))
    except ValueError as ex:
        print("Ошибка преобразования:", ex)
        continue

    #Тут если 2 числа делаем среднее, или просто добавляем 1 число
    if digits:
        if len(digits) > 1:
            salary = sum(digits) / len(digits)
        else:
            salary = digits[0]

    salaries.append(salary)


print(salaries)

#Делим и округляем
middle_salary = round(sum(salaries)/len(salaries))

print(f"Средняя зарплата: {middle_salary}")

driver.quit()
