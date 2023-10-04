import os
import json

def load_students() -> list:
    """Загружает список студентов из файла"""
    with open(os.path.join('data', 'students.json'), 'r') as file:
        return json.loads(file.read())


def load_professions() -> list:
    """Загружает список профессий из файла"""
    with open(os.path.join('data', 'professions.json'), 'r') as file:
        return json.loads(file.read())


def get_student_by_pk(pk: int) -> dict:
    """Получает словарь с данными студента по его pk"""
    return {key: value for elem in list(filter(lambda x: x['pk'] == pk, load_students())) for key, value in elem.items()}


def get_profession_by_title(title: str) -> dict:
    """Получает словарь с инфо о профе по названию"""
    return {key: value for elem in list(filter(lambda x: x['title'] == title, load_professions())) for key, value in elem.items()}

def check_fitness(student: int, profession: str) -> dict:
    """Функция, которая получив студента и профессию, возвращала бы словарь типа:
    {
    "has": ["Python", "Linux"],
    "lacks": ["Docker, SQL"],
    "fit_percent": 50
    }
    """
    student_set_skills = set(get_student_by_pk(student)['skills'])
    prof_set_skills = set(get_profession_by_title(profession)['skills'])
    return {
        'has' : list(student_set_skills.intersection(prof_set_skills)),
        'lacks' : list(prof_set_skills.difference(student_set_skills)),
        'fit_percent' : f'{(len(list(student_set_skills.intersection(prof_set_skills))) / len(list(prof_set_skills))) * 100}%'
        }

