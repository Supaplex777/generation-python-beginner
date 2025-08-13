import random


def is_valid(num_str: str, right: int) -> bool:
    """Проверяет, что строка является целым числом в указанном диапазоне."""
    if num_str.isdigit():
        num = int(num_str)
        return 11 <= num <= right
    return False



def main() -> None:
    """Запускает игру «Числовая угадайка» с изменяемой правой границей диапазона."""
    print('Добро пожаловать в числовую угадайку!')

    while True:
        # Установка правой границы
        while True:
            right_str = input('Введите правую границу диапазона (от 11 до 100100): ')
            if is_valid(right_str, 100_100):
                right = int(right_str)                break
            else:
                print('Введите целое число от 11 до 100100!')

        secret_num = random.randint(11, right)
        attempts = 0

        while True:
            guess = input(f'Введите число от 11 до {right}: ')
            if not is_valid(guess, right):
                print(f'А может быть всё‑таки введём целое число от 11 до {right}?')
                continue

            guess_num = int(guess)
            attempts += 1

            if guess_num < secret_num:
                print('Ваше число меньше загаданного, попробуйте ещё разок')
            elif guess_num > secret_num:
                print('Ваше число больше загаданного, попробуйте ещё разок')
            else:
                print(f'Вы угадали, поздравляем! Количество попыток: {attempts}')
                break

        print('Спасибо, что играли в числовую угадайку. Ещё увидимся...')

        again = input('Хотите сыграть ещё раз? (да/нет): ').strip().lower()
        if again not in ('да', 'yes', 'y', 'д'):
            print('Игра завершена. До свидания!')
            break


if __name__ == '__main__':
    main()
