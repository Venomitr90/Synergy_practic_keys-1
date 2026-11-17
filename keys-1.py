import datetime
import calendar

def get_user_birthdate():
    """Запрашивает у пользователя дату рождения с проверкой корректности."""
    while True:
        try:
            day = int(input("Введите день вашего рождения (1-31): "))
            month = int(input("Введите месяц вашего рождения (1-12): "))
            year = int(input("Введите год вашего рождения: "))
            
            # Проверка, что дата существует (например, защита от 30 февраля)
            birth_date = datetime.date(year, month, day)
            
            # Проверка, что дата не в будущем
            if birth_date > datetime.date.today():
                print("Ошибка: Дата рождения не может быть в будущем. Попробуйте снова.\n")
                continue
                
            return birth_date
        except ValueError:
            print("Ошибка: Введены некорректные данные (проверьте день, месяц и год). Попробуйте снова.\n")

def get_weekday(date_obj):
    """Определяет день недели для заданной даты."""
    # weekday() возвращает 0 для понедельника и 6 для воскресенья
    # Используем массив для получения названия на русском
    days_ru = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
    return days_ru[date_obj.weekday()]

def is_leap_year(year):
    """Определяет, является ли год високосным."""
    # Функция calendar.isleap() делает это автоматически
    return calendar.isleap(year)

def calculate_age(birth_date):
    """Определяет, сколько сейчас лет пользователю."""
    today = datetime.date.today()
    age = today.year - birth_date.year
    
    # Корректировка, если день рождения в этом году еще не наступил
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    return age

def get_starry_date_string(date_obj):
    """Преобразует дату в формат 'дд мм гггг', где цифры заменены на звездочки."""
    # Форматируем дату в строку с ведущими нулями
    date_str = date_obj.strftime("%d %m %Y")
    
    # Заменяем все цифры на '*', оставляя пробелы
    starry_str = ""
    for char in date_str:
        if char.isdigit():
            starry_str += "*"
        else:
            starry_str += char
            
    return starry_str

def main():
    print("--- Программа стилистического преобразования даты ---")
    
    # 1. Получаем дату
    birth_date = get_user_birthdate()
    print(f"\nВы ввели дату: {birth_date.strftime('%d.%m.%Y')}")
    
    # 2. День недели
    weekday = get_weekday(birth_date)
    print(f"День недели: {weekday}")
    
    # 3. Високосный год?
    leap_status = "Да" if is_leap_year(birth_date.year) else "Нет"
    print(f"Был ли {birth_date.year} год високосным? {leap_status}")
    
    # 4. Возраст
    age = calculate_age(birth_date)
    print(f"Ваш возраст: {age} лет/года")
    
    # 5. Табло со звездочками
    starry_output = get_starry_date_string(birth_date)
    print("\nВаша дата рождения на электронном табло:")
    print("-------------------------")
    print(f"|  {starry_output}  |")
    print("-------------------------")

if __name__ == "__main__":
    main()
