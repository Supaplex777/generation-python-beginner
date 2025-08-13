import secrets

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_.'
ambiguous = 'il1Lo0O'

def filtered(s, exclude_ambiguous: bool) -> str:
    """Фильтрует символы, удаляя неоднозначные, если необходимо."""
    return ''.join(c for c in s if (c not in ambiguous) or not exclude_ambiguous)


def generate_password(length: int, pools: list[str]) -> str:
    """Генерирует пароль заданной длины из выбранных групп символов.

    Сначала выбирается по одному символу из каждой выбранной группы, затем оставшиеся
    символы добираются из общего набора, после чего получившийся список
    перемешивается (Fisher–Yates).
    """
    # берём по одному символу из каждой выбранной группы
    required = [secrets.choice(pool) for pool in pools]
    # общий алфавит
    all_chars = ''.join(pools)
    # добираем оставшиеся символы
    rest = [secrets.choice(all_chars) for _ in range(length - len(required))]
    pwd_list = required + rest
    # перемешиваем (Fisher–Yates)
    for i in range(len(pwd_list) - 1, 0, -1):
        j = secrets.randbelow(i + 1)
        pwd_list[i], pwd_list[j] = pwd_list[j], pwd_list[i]
    return ''.join(pwd_list)


def main() -> None:
    """Основная функция, запрашивающая параметры и выводящая пароли."""
    try:
        n = int(input('Сколько паролей нужно сгенерировать? '))
        length = int(input('Длина каждого пароля: '))
    except ValueError:
        print('Ошибка: введите целые числа.')
        return

    include_digits = input('Включать цифры 0123456789? (y/n) ').lower() == 'y'
    include_uppercase = input('Включать прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (y/n) ').lower() == 'y'
    include_lowercase = input('Включать строчные буквы abcdefghijklmnopqrstuvwxyz? (y/n) ').lower() == 'y'
    include_symbols = input('Включать символы !#$%&*+-=?@^_? (y/n) ').lower() == 'y'
    exclude_amb = input('Исключать неоднозначные символы il1Lo0O? (y/n) ').lower() == 'y'

    if length <= 0 or n <= 0:
        print('Ошибка: длина и количество должны быть положительными.')
        return

    # формируем выбранные группы (pools)
    pools = []
    if include_digits:
        pools.append(filtered(digits, exclude_amb))
    if include_uppercase:
        pools.append(filtered(uppercase_letters, exclude_amb))
    if include_lowercase:
        pools.append(filtered(lowercase_letters, exclude_amb))
    if include_symbols:
        pools.append(filtered(punctuation, exclude_amb))

    # фильтрация могла удалить все символы в группе
    pools = [p for p in pools if p]
    if not pools:
        print('Ошибка: не выбран ни один тип символов.')
        return

    # длина должна позволять положить минимум по одному из каждой группы
    if length < len(pools):
        print(f'Ошибка: длина пароля должна быть ≥ {len(pools)} (по числу выбранных групп).')
        return

    # --- Генерация ---
    for _ in range(n):
        print(generate_password(length, pools))


if __name__ == '__main__':
    main()
