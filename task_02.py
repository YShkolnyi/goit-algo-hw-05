from re import findall 
from typing import Callable

#Стовюємо генератор, що шукає числа
def generator_numbers(text:str):
    pattern = r'\d+\.\d+' #будь-яка кількість цифр, крапка і знову будь яак кількість цифр
    all_num = findall(pattern,text) #створюємо список всіх збігів з патерном у тексті
    for num in all_num:
        yield float(num)

#Функція сумування. Використовуємо функцію як аргумент
def sum_profit(text: str, func: Callable): 
    sum = float(0)
    for num in func(text):
        sum += num
    return sum

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}") #Виведе: Загальний дохід: 1351.46