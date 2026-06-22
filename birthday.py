"""Информация о дате рождения и вывод даты в виде электронного табло."""

from datetime import date


DIGITS = {
    "0": ("***", "* *", "* *", "* *", "***"),
    "1": ("  *", " **", "  *", "  *", "***"),
    "2": ("***", "  *", "***", "*  ", "***"),
    "3": ("***", "  *", "***", "  *", "***"),
    "4": ("* *", "* *", "***", "  *", "  *"),
    "5": ("***", "*  ", "***", "  *", "***"),
    "6": ("***", "*  ", "***", "* *", "***"),
    "7": ("***", "  *", "  *", "  *", "  *"),
    "8": ("***", "* *", "***", "* *", "***"),
    "9": ("***", "* *", "***", "  *", "***"),
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


def get_birth_date() -> date:
    """Последовательно запрашивает день, месяц и год до корректного ввода."""
    while True:
        try:
            day = int(input("Введите день рождения: "))
            month = int(input("Введите месяц рождения: "))
            year = int(input("Введите год рождения: "))
            birth_date = date(year, month, day)
            if birth_date > date.today():
                print("Дата рождения не может быть в будущем. Повторите ввод.\n")
                continue
            return birth_date
        except ValueError:
            print("Некорректная дата. Введите целые числа и повторите попытку.\n")


def get_weekday(birth_date: date) -> str:
    """Возвращает название дня недели для указанной даты."""
    return WEEKDAYS[birth_date.weekday()]


def is_leap_year(year: int) -> bool:
    """Определяет, является ли год високосным по григорианскому календарю."""
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


def calculate_age(birth_date: date, today: date | None = None) -> int:
    """Вычисляет число полных лет на текущую (или переданную) дату."""
    today = today or date.today()
    birthday_has_not_happened = (today.month, today.day) < (
        birth_date.month,
        birth_date.day,
    )
    return today.year - birth_date.year - birthday_has_not_happened


def render_date(birth_date: date) -> str:
    """Рисует дату в формате дд мм гггг звёздочками."""
    groups = (
        f"{birth_date.day:02d}",
        f"{birth_date.month:02d}",
        f"{birth_date.year:04d}",
    )
    lines = []
    for row in range(5):
        rendered_groups = [
            " ".join(DIGITS[digit][row] for digit in group) for group in groups
        ]
        lines.append("   ".join(rendered_groups).rstrip())
    return "\n".join(lines)


def main() -> None:
    """Запускает диалог с пользователем."""
    birth_date = get_birth_date()

    print(f"\nДень недели: {get_weekday(birth_date)}")
    leap_message = "високосный" if is_leap_year(birth_date.year) else "не високосный"
    print(f"{birth_date.year} год — {leap_message}.")
    print(f"Возраст пользователя: {calculate_age(birth_date)}")
    print(f"\nДата рождения: {birth_date:%d %m %Y}\n")
    print(render_date(birth_date))


if __name__ == "__main__":
    main()
