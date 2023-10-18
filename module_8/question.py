
class Question:

    def __init__(self, text_quest: str, level: str, answer: str, is_question=False, user_answer=None):
        self.text_quest = text_quest
        self.level = level
        self.answer = answer
        self.is_question = is_question
        self.user_answer = user_answer

    def __repr__(self):
        return f"""Вопрос: {self.text_quest}?
Сложность: {self.level}/5
Верный ответ: {self.answer}
 
Задан ли вопрос: {self.is_question}
Ответ пользователя: {self.user_answer}
Баллы за вопрос: {self.get_points()}"""

    def get_points(self) -> int:
        points = [10, 20, 30, 40, 50]
        """Возвращает int, количество баллов.
        Баллы зависят от сложности: за 1 дается 10 баллов, за 5 дается 50 баллов.
        """
        return points[int(self.level) - 1]

    def is_correct(self, user_answer) -> bool:
        """Возвращает True, если ответ пользователя совпадает
        с верным ответов иначе False.
        """
        return self.answer == user_answer

    def build_question(self) -> str:
        """Возвращает вопрос в понятном пользователю виде, например:
        Вопрос: What do people often call American flag?
        Сложность 4/5
        """
        return f"""
Программа: Вопрос: {self.text_quest}?
Программа: Сложность: {self.level}/5"""

    def feedback(self, user_answer) -> str:
        """Возвращает :
        Ответ верный, получено __ баллов
        """
        if self.is_correct(user_answer):
            return f'Ответ верный, получено {self.get_points()} баллов'
        return f'Ответ неверный, верный ответ {self.answer}'
