from .form import Ui_Widget
from app_behavior import AppBehavior
from calculator import Calculator


class Ui:
    def __init__(self, ui_widget: Ui_Widget, calculator: Calculator, behavior: AppBehavior):
        self.behavior = behavior
        self.ui_widget = ui_widget
        self.observers = []
        self.calculator = calculator

        self.ui_widget.task_selection.currentIndexChanged.connect(self.select_task)
        self.ui_widget.calculate.clicked.connect(self.calculate)

    def set_behavior(self, new_behavior: AppBehavior):
        self.behavior = new_behavior

    def get_user_data(self) -> str:
        match self.behavior:
            case AppBehavior.scheme_task:
                return self.ui_widget.data_1.text()
            case AppBehavior.student_task:
                pass
            case AppBehavior.bayes_task:
                pass

    def calculate(self):
        answer = self.calculator.calculate(self.get_user_data())
        self.ui_widget.answer.setText(answer)

    def select_task(self):
        self.notify_observers()

    def get_new_behavior(self) -> AppBehavior:
        return self.ui_widget.task_selection.currentIndex()

    def register_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self):
        for o in self.observers:
            o.notify_observer()
