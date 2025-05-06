import random

def get_computer_choice():
    """Функция для случайного выбора компьютером"""
    choices = ["Камень", "Ножницы", "Бумага"]
    return random.choice(choices)

def get_user_choice():
    """Функция для получения выбора пользователя"""
    while True:
        print("\nВведите свой выбор:")
        print("1 - Камень\n2 - Ножницы\n3 - Бумага")
        user_input = input("Введите число (1/2/3): ")
        
        if user_input in ["1", "2", "3"]:
            choices = ["Камень", "Ножницы", "Бумага"]
            return choices[int(user_input) - 1]
        else:
            print("Некорректный ввод. Попробуйте снова.")

def determine_winner(user_choice, computer_choice):
    """Определение победителя"""
    if user_choice == computer_choice:
        return "Ничья!"
    elif (user_choice == "Камень" and computer_choice == "Ножницы") or \
         (user_choice == "Ножницы" and computer_choice == "Бумага") or \
         (user_choice == "Бумага" and computer_choice == "Камень"):
        return "Вы победили!"
    else:
        return "Вы проиграли!"

def play_game():
    """Основная функция для игры"""
    print("Добро пожаловать в игру 'Камень, Ножницы, Бумага'!")
    
    while True:
        # Выборы компьютера и игрока
        computer_choice = get_computer_choice()
        user_choice = get_user_choice()
        
        # Показать выборы
        print(f"\nВаш выбор: {user_choice}")
        print(f"Выбор компьютера: {computer_choice}")
        
        # Определение победителя
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        # Спросить, хочет ли игрок сыграть еще раз
        play_again = input("\nХотите сыграть еще раз? (да/нет): ").lower()
        if play_again != "да":
            print("Спасибо за игру! До свидания!")
            break

# Запуск игры
if __name__ == "__main__":
    play_game()