# coding: utf-8

# Python. Быстрый старт.
# Занятие 2.

# Домашнее задание: в случае, если пользователь ввел Y, то придумать и вывести список действий,
#                    спросить, какое он хочет выполнить;
#                   ознакомиться с PEP8

print("Great Python Program!")
print("Привет, программист!")
name = input("Ваше имя: ")

print(name, ", добро пожаловать в мир Python!")

answer = input("Давайте поработаем? (Y/N)")
    
# PEP-8 рекомендует делать отступ, равный 4 пробелам   
if answer == 'Y':
    print("Вам премия!")            # <- здесь будет код домашнего задания

# Оператор == (двойное равно) - это логический оператор сравнения
elif answer == 'N':    
    print("До свидания!")
else:
    print("Неизвестный ответ")