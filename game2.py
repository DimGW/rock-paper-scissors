import random

def get_user_choice(player_name):
    """Получение выбора от игрока"""
    while True:
        choice = input(f"{player_name}, выберите камень (r), ножницы (s) или бумагу (p): ").lower()
        if choice in ['r', 's', 'p']:
            return choice
        else:
            print("Неверный выбор! Попробуйте снова.")

def determine_winner(choice1, choice2):
    """Определяем победителя по стандартным правилам игры"""
    if choice1 == choice2:
        return None  # Ничья
    elif (
        (choice1 == 'r' and choice2 == 's') or
        (choice1 == 'p' and choice2 == 'r') or
        (choice1 == 's' and choice2 == 'p')
    ):
        return choice1  # Победил первый игрок
    else:
        return choice2  # Победил второй игрок

def play_game():
    """Основная логика игры с тремя участниками"""
    print("Игра Камень-Ножницы-Бумага!")
    player1_name = input("Игрок 1 введите своё имя: ")
    player2_name = input("Игрок 2 введите своё имя: ")

    player1_choice = get_user_choice(player1_name)
    player2_choice = get_user_choice(player2_name)
    computer_choice = random.choice(['r', 's', 'p'])  # Ход компьютера выбирается случайным образом

    # Сообщаем игрокам выбор компьютера
    print(f"\nКомпьютер выбрал {computer_choice}\n")

    results = []
    players = [(player1_name, player1_choice), (player2_name, player2_choice), ('компьютер', computer_choice)]

    for i in range(len(players)):
        for j in range(i + 1, len(players)):
            winner = determine_winner(players[i][1], players[j][1])
            if winner is not None:
                winner_name = next((name for name, ch in players if ch == winner), '')
                loser_name = next((name for name, ch in players if ch != winner), '')
                results.append(f'{winner_name} победил {loser_name}')
            else:
                results.append(f'{players[i][0]} и {players[j][0]} сыграли вничью.')

    # Подводим итоги матча
    print("\nИтоги поединков:")
    for res in results:
        print(res)

        # Спросить, хочет ли игрок сыграть еще раз
        play_again = input("\nХотите сыграть еще раз? (y/n): ").lower()
        if play_again != "да":
            print("Спасибо за игру! До свидания!")
            break

play_game()
