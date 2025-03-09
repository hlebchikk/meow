section1 = [i for i in range(8) if i > 0]
section2 = [i for i in range(17) if i > 0]
section3 = [i for i in range(10) if i > 0]
print("Здравствуйте! Секций с местами на самолет всего три: 1 секция - 7 мест",
      "2 секция - 16 мест",
      "3 секция - 9 мест")
while True: #Основной цикл
    while True: #Цикл сейций
        section = int(input("Выберите секцию, на которой хотите бронировать места (1-3): "))
        if section == 0:
            print("Выход из системы.")
            exit()
        if 1 <= section <= 3:
            break
        print("Такой секции не существует, попробуйте еще раз")
    while True: #Цикл мест
        mesto = int(input("Отлично! Теперь выберите из той секции что вы выбрали: "))
        if mesto == 0:
            print("Выход из системы.")
            exit()
        if 1 <= mesto <= 16:
            break
        print("Число мест больше существующих, попробуйте еще раз")
