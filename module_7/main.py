from utils import get_student_by_pk, get_profession_by_title, check_fitness

if __name__ == '__main__':
    try:
        print('Программа: Введите номер студента')
        user_answer = int(input('Пользователь: '))
        if not 1 <= user_answer <= 4:
            raise IndexError
        print(f'Программа: Студент {get_student_by_pk(user_answer)["full_name"]}')
        skills_list = ', '.join(get_student_by_pk(user_answer)["skills"])
        print(f'Программа: Знает {skills_list}')
        print(f'Программа: Выберите специальность для оценки студента {get_student_by_pk(user_answer)["full_name"]}')
        user_answer1 = input('Пользователь: ').title()
        if not user_answer1 in ["Backend", "Frontend", "Testing"]:
            raise ValueError
        print(f'Программа: Пригодность {check_fitness(user_answer, user_answer1)["fit_percent"]}')
        print(f'Программа: {get_student_by_pk(user_answer)["full_name"]} знает {", ".join(check_fitness(user_answer, user_answer1)["has"])}')
        print(f'Программа: {get_student_by_pk(user_answer)["full_name"]} не знает {", ".join(check_fitness(user_answer, user_answer1)["lacks"])}')
    except IndexError:
        print('Программа: У нас нет такого студента')
    except ValueError:
        print('Программа: У нас нет такой специальности')


