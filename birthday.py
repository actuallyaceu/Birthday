"""Учебная программа для работы с датой рождения."""

import sys
from datetime import date


# Здесь записано, как выглядит каждая цифра на табло.
# У каждой цифры 7 строк, ширина цифры — 5 символов.
DIGITS = {
    "0": (
        "*****",
        "*   *",
        "*   *",
        "*   *",
        "*   *",
        "*   *",
        "*****",
    ),
    "1": (
        "  *  ",
        " **  ",
        "* *  ",
        "  *  ",
        "  *  ",
        "  *  ",
        "*****",
    ),
    "2": (
        "*****",
        "    *",
        "    *",
        "*****",
        "*    ",
        "*    ",
        "*****",
    ),
    "3": (
        "*****",
        "    *",
        "    *",
        "*****",
        "    *",
        "    *",
        "*****",
    ),
    "4": (
        "*   *",
        "*   *",
        "*   *",
        "*****",
        "    *",
        "    *",
        "    *",
    ),
    "5": (
        "*****",
        "*    ",
        "*    ",
        "*****",
        "    *",
        "    *",
        "*****",
    ),
    "6": (
        "*****",
        "*    ",
        "*    ",
        "*****",
        "*   *",
        "*   *",
        "*****",
    ),
    "7": (
        "*****",
        "    *",
        "   * ",
        "  *  ",
        " *   ",
        "*    ",
        "*    ",
    ),
    "8": (
        "*****",
        "*   *",
        "*   *",
        "*****",
        "*   *",
        "*   *",
        "*****",
    ),
    "9": (
        "*****",
        "*   *",
        "*   *",
        "*****",
        "    *",
        "    *",
        "*****",
    ),
}


WEEKDAYS = (
    "понедельник",
    "вторник",
    "среда",
    "четверг",
    "пятница",
    "суббота",
    "воскресенье",
)


def get_birth_date():
    """Спрашивает дату рождения и проверяет её."""
    while True:
        try:
            day = int(input("Введите день рождения: "))
            month = int(input("Введите месяц рождения: "))
            year = int(input("Введите год рождения: "))

            birth_date = date(year, month, day)

            if birth_date > date.today():
                print("Дата рождения не может быть в будущем. Попробуйте ещё раз.\n")
            else:
                return birth_date

        except ValueError:
            print("Такой даты нет. Попробуйте ещё раз.\n")


def get_weekday(birth_date):
    """Находит день недели."""
    weekday_number = birth_date.weekday()
    return WEEKDAYS[weekday_number]


def is_leap_year(year):
    """Проверяет, был ли год високосным."""
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    return year % 4 == 0


def calculate_age(birth_date, today=None):
    """Считает возраст в полных годах."""
    if today is None:
        today = date.today()

    age = today.year - birth_date.year

    # Если день рождения в этом году ещё не наступил, убираем один год.
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age = age - 1

    return age


def render_date(birth_date):
    """Рисует дату звёздочками в формате дд мм гггг."""
    day = f"{birth_date.day:02d}"
    month = f"{birth_date.month:02d}"
    year = f"{birth_date.year:04d}"

    date_parts = (day, month, year)
    result_lines = []

    # Собираем табло строка за строкой.
    for row in range(7):
        ready_parts = []

        for part in date_parts:
            ready_digits = []

            for digit in part:
                ready_digits.append(DIGITS[digit][row])

            ready_parts.append("  ".join(ready_digits))

        result_lines.append("     ".join(ready_parts).rstrip())

    return "\n".join(result_lines)


def main():
    birth_date = get_birth_date()

    print(f"\nДень недели вашего рождения: {get_weekday(birth_date)}.")

    if is_leap_year(birth_date.year):
        print(f"{birth_date.year} год был високосным.")
    else:
        print(f"{birth_date.year} год не был високосным.")

    print(f"Сейчас вам {calculate_age(birth_date)} лет.")
    print(f"\nВаша дата рождения: {birth_date:%d %m %Y}\n")
    print(render_date(birth_date))


if __name__ == "__main__":
    main()

    # Эта пауза нужна, чтобы готовый EXE не закрылся сразу.
    if getattr(sys, "frozen", False):
        input("\nНажмите Enter, чтобы выйти...")
