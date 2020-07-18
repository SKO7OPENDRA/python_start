def lesson2():
    print("Great Python Program!")
    print("Привет, программист!")
    name = input("Ваше имя: ")

    print(name, ", добро пожаловать в мир Python!")

    answer = input("Давайте поработаем? (Y/N)")

    # PEP-8 рекомендует делать отступ, равный 4 пробелам
    if answer == 'y' or answer == 'Y':
        print("Вам премия!")  # <- здесь будет код домашнего задания
    else:
    # Оператор == (двойное равно) - это логический оператор сравнения
        print("До встречи!")

lesson2()

while True:
    flag = input('Ещё раз? [Y/N]: ')

    if flag == 'y' or flag == 'Y':
        lesson2()
    else:
        break