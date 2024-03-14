from .scheme_task import SchemeTask
from .student_task import StudentTask
from .bayes_task import BayesTask

from app_behavior import AppBehavior


class Calculator:
    def __init__(self, behavior: AppBehavior):
        self.behavior = behavior
        self.scheme = SchemeTask()
        self.student = StudentTask()
        self.bayes = BayesTask()
        self.invalid_input = "Неверные входные данные."

    def set_behavior(self, behavior: AppBehavior):
        self.behavior = behavior

    def to_numbers(self, user_input: str) -> list:
        data = []
        user_input = user_input.replace(' ', '')
        user_input = user_input.replace(',', '.')

        if len(user_input) == 0:
            return data

        for n in user_input.split(';'):
            if any(not (c.isdigit() or c == '.') for c in n) or n == '':
                return []
            data.append(int(n) if self.behavior == AppBehavior.student_task else float(n))

        return data

    def validate_data(self, user_input: list) -> bool:
        match self.behavior:
            case AppBehavior.scheme_task:
                if len(user_input) != 5:
                    return False
                if any(n < 0 or n > 1 for n in user_input):
                    return False
            case AppBehavior.student_task:
                if (len(user_input) != 3
                        or user_input[0] > user_input[2]
                        or user_input[1] > user_input[2]):
                    return False
            case AppBehavior.bayes_task:
                if any(n < 0 or n > 1 for n in user_input):
                    return False
                hypothesis_prob = sum(user_input[0:len(user_input) // 2])
                if hypothesis_prob != 1:
                    return False

        return True

    def calculate(self, user_input: str) -> str:
        data = self.to_numbers(user_input if self.behavior == AppBehavior.scheme_task else user_input[2:])

        invalid_input = self.invalid_input
        if self.behavior == AppBehavior.student_task:
            invalid_input = self.invalid_input + '_' + self.invalid_input

        if len(data) == 0:
            return invalid_input
        if not self.validate_data(data):
            return invalid_input

        match self.behavior:
            case AppBehavior.scheme_task:
                return f'Ответ: {self.scheme.calculate_probability(*data)}'
            case AppBehavior.student_task:
                answer = self.student.calculate_probability(
                    int(user_input[0]), *data
                )
                prom = [str(c)[0:5] for c in answer[0]]
                return f'Промежуточный ответ: {', '.join(prom)}_Ответ{answer[1]}'
            case AppBehavior.bayes_task:
                ln = len(data)
                return f'Ответ: {self.bayes.calculate_probability(
                    int(user_input[0]), data[0: ln // 2], data[ln // 2:]
                )}'
