# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

def sum_digits(num):
    return sum(map(int, num.replace('.','').replace('-','')))

num = input('Введите число: ')
print(f'Сумма цифр в веденном Вами числе -> {sum_digits(num)}')