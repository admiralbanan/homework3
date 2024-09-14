import random

# Список известных людей и их даты рождения
famous_people = {
    "А.С. Пушкин": "06.06.1799",
    "Л.Н. Толстой": "09.09.1828",
    "М.В. Ломоносов": "19.11.1711",
    "Ф.М. Достоевский": "11.11.1821",
    "П.И. Чайковский": "07.05.1840",
    "А.П. Чехов": "29.01.1860",
    "С.А. Есенин": "03.10.1895",
    "И.С. Тургенев": "09.11.1818",
    "В.В. Маяковский": "19.07.1893",
    "Н.В. Гоголь": "01.04.1809"
}

# Выбираем 5 случайных людей
selected_people = random.sample(list(famous_people.items()), 5)

correct_answers = 0
total_questions = len(selected_people)

# Викторина
for person, birth_date in selected_people:
    user_answer = input(f"Введите дату рождения {person} в формате 'dd.mm.yyyy': ")
    if user_answer == birth_date:
        print("Верно!")
        correct_answers += 1
    else:
        day, month, year = birth_date.split('.')
        print(f"Неверно! Правильный ответ: {int(day)}-{month_to_text(month)}-{year} года")

# Подсчет правильных и неправильных ответов
wrong_answers = total_questions - correct_answers
print(f"\nКоличество правильных ответов: {correct_answers}")
print(f"Количество неправильных ответов: {wrong_answers}")

# Повтор игры
while True:
    play_again = input("\nХотите начать сначала? (да/нет): ").lower()
    if play_again == "да":
        # Повторить викторину
    elif play_again == "нет":
        print("Игра завершена.")
        break
