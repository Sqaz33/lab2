from .form import Ui_Widget
from app_behavior import AppBehavior
from calculator import Calculator


class Ui:
    def __init__(self, ui_widget: Ui_Widget, calculator: Calculator, behavior: AppBehavior):
        self.behavior = AppBehavior(2 - behavior.value)
        self.ui_widget = ui_widget
        self.observers = []
        self.calculator = calculator

        # ----------коннекты-----------
        self.ui_widget.task_selection.currentIndexChanged.connect(self.select_task)
        self.ui_widget.compute_button.clicked.connect(self.calculate)
        self.ui_widget.compute_button_2.clicked.connect(self.calculate)
        self.ui_widget.compute_button_3.clicked.connect(self.calculate)

    def set_behavior(self, new_behavior: AppBehavior):
        self.behavior = new_behavior

    def get_user_data(self) -> str:
        match self.behavior:
            case AppBehavior.scheme_task:
                pass
            case AppBehavior.student_task:
                pass
            case AppBehavior.bayes_task:
                pass

    def calculate(self):
        answer = self.calculator.calculate(self.get_user_data())
        pass

    def select_task(self):
        self.notify_observers()
        self.change_ui()

    def change_ui(self):
        self.ui_widget.stackedWidget.setCurrentIndex(2 - self.behavior.value)

    def get_new_behavior(self) -> AppBehavior:
        return self.ui_widget.task_selection.currentIndex()

    def register_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self):
        for o in self.observers:
            o.notify_observer()
