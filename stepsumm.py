def calculate_expression(n):
    # Вычисляем выражение n^2 + n^3 + n^4
    result = n**2 + n**3 + n**4
    return result

# Запрашиваем у пользователя целое число
n = int(input("Введите целое число n: "))

# Выводим результат
print(f"Результат выражения n^2 + n^3 + n^4 для n = {n}: {calculate_expression(n)}")