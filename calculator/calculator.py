from .scheme_task import SchemeTask
from app_behavior import AppBehavior


class Calculator:
    def __init__(self, behavior: AppBehavior):
        self._behavior = behavior
        self.scheme = SchemeTask()
        self.invalid_input = "неверные входные данные"

    def set_behavior(self, behavior: AppBehavior):
        self._behavior = behavior

    def to_numbers(self, user_input: str) -> list[float]:
        probabilities = []
        user_input = user_input.replace(' ', '')
        user_input = user_input.replace(',', '.')

        for n in user_input.split(';'):
            if any(not (c.isdigit() or c == '.') for c in n):
                return []
            probabilities.append(float(n))

        return probabilities

    def validate_data(self, probabilities: list[float]) -> bool:
        if any(n < 0 or n > 1 for n in probabilities):
            return False

        match self._behavior:
            case AppBehavior.scheme_task:
                if len(probabilities) != 5:
                    return False
            case AppBehavior.student_task:
                pass
            case AppBehavior.bayes_task:
                pass

        return True

    def calculate(self, user_input: str) -> str:
        probabilities = self.to_numbers(user_input)
        if len(probabilities) == 0:
            return self.invalid_input

        match self._behavior:
            case AppBehavior.scheme_task:
                return (f'{self.scheme.calculateProbability(*probabilities)}' if self.validate_data(probabilities)
                        else self.invalid_input)
            case AppBehavior.student_task:
                pass
            case AppBehavior.bayes_task:
                pass
