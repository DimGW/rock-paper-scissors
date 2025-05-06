def km_to_miles(km):
    """Преобразует километры в обычные мили."""
    return km * 0.621371

def km_to_nautical_miles(km):
    """Преобразует километры в морские мили."""
    return km * 0.539957

def miles_to_km(miles):
    """Преобразует обычные мили в километры."""
    return miles / 0.621371

def nautical_miles_to_km(nautical_miles):
    """Преобразует морские мили в километры."""
    return nautical_miles / 0.539957

def main():
    print("Добро пожаловать в программу конвертации расстояний!")
    print("Выберите опцию:")
    print("1. Перевести километры в обычные мили")
    print("2. Перевести километры в морские мили")
    print("3. Перевести обычные мили в километры")
    print("4. Перевести морские мили в километры")
    
    choice = input("Введите номер опции (1/2/3/4): ")
    
    if choice == "1":
        km = float(input("Введите расстояние в километрах: "))
        print(f"{km} километров = {km_to_miles(km):.2f} обычных миль")
    elif choice == "2":
        km = float(input("Введите расстояние в километрах: "))
        print(f"{km} километров = {km_to_nautical_miles(km):.2f} морских миль")
    elif choice == "3":
        miles = float(input("Введите расстояние в обычных милях: "))
        print(f"{miles} обычных миль = {miles_to_km(miles):.2f} километров")
    elif choice == "4":
        nautical_miles = float(input("Введите расстояние в морских милях: "))
        print(f"{nautical_miles} морских миль = {nautical_miles_to_km(nautical_miles):.2f} километров")
    else:
        print("Неверный выбор! Попробуйте снова.")

if __name__ == "__main__":
    main()