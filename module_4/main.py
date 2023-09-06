"""Создаю базу данных из словарей"""
words_easy = {
    "family":"семья",
    "hand": "рука",
    "people":"люди",
    "evening": "вечер",
    "minute":"минута",
}
words_medium = {
    "believe":"верить",
    "feel": "чувствовать",
    "make":"делать",
    "open": "открывать",
    "think":"думать",
}
words_hard = {
    "rural":"деревенский",
    "fortune": "удача",
    "exercise":"упражнение",
    "suggest": "предлагать",
    "except":"кроме",
}
levels = {
   0: "Нулевой",
   1: "Так себе",
   2: "Можно лучше",
   3: "Норм",
   4: "Хорошо",
   5: "Отлично",
}
answers = {}
words = {}
rang = ['Отлично', 'Хорошо', 'Удовлетворительно']

"""Внешний цикл отвечает за выбор уровня сложности, 
перечисляет раунды, внутренний цикл задает вопросы, проверяет ответы 
и записывает их в новый словарь
"""
for i in range(1, 4):
    print('Программа: Выберите уровень сложности.\nПрограмма: Легкий, средний, сложный.')
    change_level = input('Пользователь: ').lower()
    words = words_easy if change_level == 'лёгкий' else words_medium if change_level == 'средний' else words_hard
    print(f'Раунд {i}')
    for word, translate in words.items():
        programm = input('Программа: Нажмите Enter.\nПользователь: ')
        print(f'Программа: {word}, {len(translate)} букв, начинается на {translate[:1]}')
        user_answer = input('Пользователь: ').lower()
        if user_answer == translate:
            print(f'Программа: Верно, {word} — это {translate}.')
            answers[word] = True
        else:
            print(f'Программа: Неверно, {word} — это {translate}.')
            answers[word] = False

"""ниже основной вывод результата, обработка исключения, если правильных ответов совсем нет"""
print()
print('Программа: Правильно отвечены слова:')
right_answer = list(filter(lambda x: answers[x] == True, answers))
print(*right_answer, sep='\n')
print('Программа: Неправильно отвечены слова:')
not_the_right_answer = list(filter(lambda x: not answers[x] == True, answers))
print(*not_the_right_answer, sep='\n')
try:
    if len(not_the_right_answer)/len(right_answer) <= 0.2:
        print(f'Программа:Ваш ранг:\n{rang[0]}')
    elif 0.2 < len(not_the_right_answer)/len(right_answer) < 0.5:
        print(f'Программа:Ваш ранг:\n{rang[1]}')
    else:
        print(f'Программа:Ваш ранг:\n{rang[2]}')
except ZeroDivisionError:
    print('Правильных ответов нет')

