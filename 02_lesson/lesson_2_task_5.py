def month_to_season(month):
    if month in [12, 1, 2]:
        return "Зима"
    elif month in [3, 4, 5]:
        return "Весна"
    elif month in [6, 7, 8]:
        return "Лето"
    elif month in [9, 10, 11]:
        return "Осень"
    else:
        return "Неверный номер месяца"


month_number = int(input("Введите номер месяца: "))
season = month_to_season(month_number)
print(f"Этот месяц относится к сезону: {season}")
