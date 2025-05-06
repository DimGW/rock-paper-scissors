def convert_minutes(total_minutes):
    # Перевод минут в дни, часы и минуты
    days = total_minutes // (24 * 60)
    remaining_minutes = total_minutes % (24 * 60)
    hours = remaining_minutes // 60
    minutes = remaining_minutes % 60

    # Округляем часы и минуты
    if minutes >= 30:
        hours += 1
    if hours >= 24:
        days += 1
        hours = 0

    # Возвращаем результат в формате "дни:часы:минуты"
    return f"{int(days)}:{int(hours)}:{int(minutes)}"

# Пользовательский ввод
try:
    user_input = int(input("Введите общее количество минут: "))
    result = convert_minutes(user_input)
    print(f"Результат: {result}")
except ValueError:
    print("Ошибка: пожалуйста, введите целое число минут.")