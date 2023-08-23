question_count = 0
count = 0
score = 0
name_user = input('Привет! Предлагаю проверить свои знания английского! \nНапиши, как тебя зовут. ')
print(f'Привет, {name_user}, начинаем тренировку!')

question_and_answer = input('Вопрос 1: My name ___ Vova. ')
if question_and_answer == 'is':
  count += 1
  score += 10
  print('Ответ верный!\nВы получаете 10 баллов!')
else:
  print('Неправильно. Правильный ответ: is')
question_and_answer = input('Вопрос 2: I ___ a coder. ')
if question_and_answer == 'am':
  count += 1
  score += 10
  print('Ответ верный!\nВы получаете 10 баллов!')
else:
  print('Неправильно. Правильный ответ: am')
question_and_answer = input('Вопрос 3: I live ___ Moscow. ')
if question_and_answer == 'in':
  count += 1
  score += 10
  print('Ответ верный!\nВы получаете 10 баллов!')
else:
  print('Неправильно. Правильный ответ: in')

print(f"""Вот и всё, имя_пользователя!
Вы ответили на {count} вопросов из 3 верно.
Вы заработали {score} баллов.
Это {round((score/30)*100)} процентов.""")

# # альтернативное решение правда оно не сильно короче) Я торопился его сделать)

name_user = input('Привет! Предлагаю проверить свои знания английского! \nНапиши, как тебя зовут. ')
print(f'Привет, {name_user}, начинаем тренировку!')

def contest(question: str) -> bool:
  match question:
    case 'is':
      print('Ответ верный!\nВы получаете 10 баллов!')
      return True
    case 'am':
      print('Ответ верный!\nВы получаете 10 баллов!')
      return True
    case 'in':
      print('Ответ верный!\nВы получаете 10 баллов!')
      return True


while question_count != 3:
  question_and_answer = input('Вопрос 1: My name ___ Vova. ')
  question_count += 1
  if contest(question_and_answer):
    count += 1
    score += 10
  else:
    print('Неправильно. Правильный ответ: is')
  question_and_answer = input('Вопрос 2: I ___ a coder. ')
  question_count += 1
  if contest(question_and_answer):
    count += 1
    score += 10
  else:
    print('Неправильно. Правильный ответ: am')
  question_and_answer = input('Вопрос 3: I live ___ Moscow. ')
  question_count += 1
  if contest(question_and_answer):
    count += 1
    score += 10
  else:
    print('Неправильно. Правильный ответ: in')
print(f"""Вот и всё, имя_пользователя!
Вы ответили на {count} вопросов из 3 верно.
Вы заработали {score} баллов.
Это {round((score/30)*100)} процентов.""")



