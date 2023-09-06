questions = ["My name ___  Vova ", "I ___ a coder ", "I live ___ Moscow "]
answers = ["is", "am", "in"]
correct_answer_counter = 0
errors = 0
def contest(question: str, answer: str) -> bool:
  match question, answer:
    case 'My name ___  Vova ', 'is':
      print('Ответ верный!')
      return True
    case 'I ___ a coder ', 'am':
      print('Ответ верный!')
      return True
    case 'I live ___ Moscow ', 'in':
      print('Ответ верный!')
      return True

print("""Привет!
Предлагаю проверить свои знания английского!
Наберите "ready", чтобы начать!""")
command = input()
if command == "ready":
    for index, i_quest in enumerate(questions):
        errors = 0
        while errors != 3:
            question_and_answer = input(i_quest).lower()
            if contest(i_quest, question_and_answer):
                correct_answer_counter += 1
                break
            else:
                errors += 1
                print(f'Осталось попыток {3 - errors}, Попробуйте ещё раз!')
                continue
        else:
            print(f'Увы, но нет. Верный ответ: {answers[index]}')
            continue
    print(f"""
Вот и всё!
Вы ответили на {correct_answer_counter} вопросов из 3 верно.
Это {round((correct_answer_counter / 3) * 100)} процентов.
""")
else:
    print('Кажется, вы не хотите играть. Очень жаль.')

# альтернативное решение c вложенным списком

newList = [["My name ___  Vova ", "is"], ["I ___ a coder ", "am"], ["I live ___ Moscow ", "in"]]
print("""Привет! 
Предлагаю проверить свои знания английского! 
Наберите "ready", чтобы начать!""")
command = input()
if command == "ready":
    for index, value in enumerate(newList):
        errors = 0
        while errors != 3:
            question_and_answer = input(value[0]).lower()
            if question_and_answer == value[1]:
                correct_answer_counter += 1
                print('Ответ верный!')
                break
            else:
                errors += 1
                print(f'Осталось попыток {3 - errors}, Попробуйте ещё раз!')
                continue
        else:
            print(f'Увы, но нет. Верный ответ: {value[1]}')
            continue
    print(f"""
Вот и всё!
Вы ответили на {correct_answer_counter} вопросов из 3 верно.
Это {round((correct_answer_counter / 3) * 100)} процентов.
""")
else:
    print('Кажется, вы не хотите играть. Очень жаль.')