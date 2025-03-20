all_section = {
    1: 7,
    2: 16,
    3: 9
}
print("Здравствуйте! Секций с местами на самолет всего три:", all_section)
while True: #Основной цикл
    while True: #Цикл секций
        section = int(input("Выберите секцию, на которой хотите бронировать места (1-3) или нажмите 0 для выхода: "))
        if section == 0:
            print("Выход из системы.")
            exit()
        if section in all_section:
            print(f"Вы выбрали секцию {section}, в ней {all_section[section]} мест.")
            break
        else:
            print("Введеное число некоректно, попробуйте снова.")
    while True: #Цикл мест
        mesto = int(input("Теперь, укажите нужное количество мест из той секции что вы выбрали или нажмите 0 для выхода: "))
        if mesto == 0:
            print("Выход из системы.")
            exit()
        if 1 <= mesto <= all_section[section]:
            all_section[section] -= mesto
            print(f"Бронь успешна! В секции {section} осталось {all_section[section]} мест.")
            break
        else:
            print("Число мест больше либо меньше существующих, попробуйте еще раз.")
