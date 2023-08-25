question_list = ['Вопрос 1: My name ___ Vova. ', 'Вопрос 2: I ___ a coder. ', 'Вопрос 3: I live ___ Moscow. ']
correct_answer = ['Неправильно. Правильный ответ: is', 'Неправильно. Правильный ответ: am', 'Неправильно. Правильный ответ: in']
correct_answer_counter = 0
name_user = input('Привет! Предлагаю проверить свои знания английского! \nНапиши, как тебя зовут. ')
print(f'Привет, {name_user}, начинаем тренировку!')

question_and_answer = input('Вопрос 1: My name ___ Vova. ').lower()
if question_and_answer == 'is':
  correct_answer_counter += 1
  print('Ответ верный!\nВы получаете 10 баллов!')
else:
  print('Неправильно. Правильный ответ: is')
question_and_answer = input('Вопрос 2: I ___ a coder. ').lower()
if question_and_answer == 'am':
  correct_answer_counter += 1
  print('Ответ верный!\nВы получаете 10 баллов!')
else:
  print('Неправильно. Правильный ответ: am')
question_and_answer = input('Вопрос 3: I live ___ Moscow. ').lower()
if question_and_answer == 'in':
  correct_answer_counter += 1
  print('Ответ верный!\nВы получаете 10 баллов!')
else:
  print('Неправильно. Правильный ответ: in')

print(f"""Вот и всё, имя_пользователя!
Вы ответили на {correct_answer_counter} вопросов из 3 верно.
Вы заработали {correct_answer_counter*10} баллов.
Это {round((correct_answer_counter/3)*100)} процентов.""")

альтернативное решение, запускать этот код нужно по отдельности, иначе correct_answer_counter будет больше 100%

name_user = input('Привет! Предлагаю проверить свои знания английского! \nНапиши, как тебя зовут. ')
print(f'Привет, {name_user}, начинаем тренировку!')

def contest(question: str, answer: str) -> bool:
  match question, answer:
    case 'Вопрос 1: My name ___ Vova. ', 'is':
      print('Ответ верный!\nВы получаете 10 баллов!')
      return True
    case 'Вопрос 2: I ___ a coder. ', 'am':
      print('Ответ верный!\nВы получаете 10 баллов!')
      return True
    case 'Вопрос 3: I live ___ Moscow. ', 'in':
      print('Ответ верный!\nВы получаете 10 баллов!')
      return True

for index, i_quest in enumerate(question_list):
  question_and_answer = input(i_quest).lower()
  if contest(i_quest, question_and_answer):
    correct_answer_counter += 1
  else:
    print(correct_answer[index])

print(f"""Вот и всё, имя_пользователя!
Вы ответили на {correct_answer_counter} вопросов из 3 верно.
Вы заработали {correct_answer_counter*10} баллов.
Это {round((correct_answer_counter/3)*100)} процентов.""")

