def process_numbers(numbers):
    for num in numbers:
        if num < 0:  # Если число отрицательное, прерываем цикл
            print("Найдено отрицательное число. Программа завершена.")
            break
        print(num)  # Выводим положительное число

# Пример использования
numbers = list(map(int, input("Введите список чисел через пробел: ").split()))
process_numbers(numbers)