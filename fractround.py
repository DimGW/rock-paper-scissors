from fractions import Fraction

# Вещественное число
number = 9.75

# Преобразуем число в дробь, ограничивая точность до 2 знаков после запятой
fraction = Fraction(number).limit_denominator(100)

# Выводим результат
print(f"{number} ≈ {fraction.numerator}/{fraction.denominator}")