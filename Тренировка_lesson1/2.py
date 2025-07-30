#Работа со списками
# employee_list = ["Jonh Snow", "Piter Pen", "Drakula", "IvanIV", "Moana", "Juilet"]

# print(employee_list [1] + ", " + employee_list [-2])

#Деление на 3
def dev_by_three(number):
   return "Да" if number % 3 == 0 else "Нет"

num = int(input("Введите число: "))
result = dev_by_three(num)
print(f"Делится ли на 3 {num}? - {result}")

#Округление
# import math

# def min_boxes(items):
#     return math.ceil(items / 5)

# num_items = int(input("Введите количество предметов: "))
# print(f"Минимальное количество коробок: {min_boxes(num_items)}")

#Два делителя
# n = int(input("Введите число:"))

# def check_divisibility(n):
#     for i in range(1, n + 1):
#         if i % 4 == 0:
#             print(f"{i} - Делится и на 2, и на 4")
#         elif i % 2 == 0:
#             print(f"{i} - Делится на 2, но не на 4")
#         else:
#             print(i)

# check_divisibility(n)

#Квартал
# def quarter_of_year(month):
#     if 1 <= month <=3:
#         return "I квартал"
#     elif 4 <= month <= 6:
#         return "II квартал"
#     elif 7 <= month <= 9:
#         return "III квартал"
#     elif 10 <= month <= 12:
#         return "IV квартал"
#     else:
#         return "Неверный номер месяца"
    
#     try:
#         month = int(input("Введите номер месяца (1-12): "))
#         print(quarter_of_year(month))
#     except ValueError:
#         print("Пожалйуста введите целое число от 1 до 12.")

#Фильтрация списка

#Range
my_list = list(range(25, 0, -5))
print(my_list)

#Поменять значения местами
var_1 = 50
var_2 = 5

temp = var_1
ar_1 = var_2
var_2 = temp

print("var_1 =")

