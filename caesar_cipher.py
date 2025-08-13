#!/usr/bin/env python3
"""
Шифр Цезаря: шифрование/дешифрование с поддержкой русского и английского
алфавитов, сохранением регистра и возможностью выбора языка.

В русском алфавите используется 32 буквы (без «ё»).
"""


def caesar(text: str, shift: int, lang: str, mode: str) -> str:
    """Выполняет шифрование или дешифрование строки `text`.

    :param text: исходный текст
    :param shift: шаг сдвига вправо
    :param lang: язык ('русский' или 'английский')
    :param mode: 'шифрование' для кодирования или 'дешифрование' для обратного сдвига
    :returns: преобразованный текст
    :raises ValueError: если язык не распознан
    """
    # алфавиты в нижнем регистре
    ru = "абвгдежзийклмнопрстуфхцчшщъыьэюя"   # 32 буквы, без "ё"
    en = "abcdefghijklmnopqrstuvwxyz"        # 26 букв

    # выбор алфавита
    if lang.startswith(("ru", "рус", "р")):
        alphabet = ru
    elif lang.startswith(("en", "анг", "a", "e")):
        alphabet = en
    else:
        raise ValueError("Неизвестный язык. Укажите 'русский' или 'английский'.")

    n = len(alphabet)

    # направление: шифрование — сдвиг вправо; дешифрование — влево (отрицательный)
    if mode.startswith(("д", "de", "рас", "dec")):
        shift = -shift

    # нормализуем сдвиг
    shift %= n

    res_chars: list[str] = []
    for ch in text:
        # выбираем, с каким алфавитом работать (нижний/верхний)
        if ch.isalpha():
            is_upper = ch.isupper()
            base = alphabet.upper() if is_upper else alphabet
            idx = base.find(ch)
            if idx != -1:
                # циклический сдвиг
                new_ch = base[(idx + shift) % n]
                res_chars.append(new_ch)
            else:
                # символ не из выбранного алфавита (например, латиница в режиме RU) — не меняем
                res_chars.append(ch)
        else:
            # неалфавитные символы не меняем
            res_chars.append(ch)

    return "".join(res_chars)


def main() -> None:
    """Диалог с пользователем для шифрования/дешифрования текста."""
    print("Шифр Цезаря")
    mode = input("Направление (шифрование/дешифрование): ").strip().lower()
    lang = input("Язык (русский/английский): ").strip().lower()

    # шаг сдвига вправо (целое число)
    while True:
        try:
            k = int(input("Шаг сдвига (целое число, вправо): ").strip())
            break
        except ValueError:
            print("Введите целое число.")

    text = input("Введите текст: ")

    try:
        result = caesar(text, k, lang, mode)
        print("Результат:", result)
    except ValueError as e:
        print("Ошибка:", e)


if __name__ == '__main__':
    main()