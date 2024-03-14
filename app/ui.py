from .form import Ui_Widget
from app_behavior import AppBehavior
from calculator import Calculator

from PyQt5.QtGui import QPixmap


class Ui:
    def __init__(self, ui_widget: Ui_Widget, calculator: Calculator, behavior: AppBehavior):
        self.behavior = behavior
        self.ui_widget = ui_widget
        self.observers = []
        self.calculator = calculator

        # -----------загрузка картинок------
        self.scheme_pixmap = QPixmap()
        self.scheme_pixmap.load("formulas/number1/scheme.png")
        self.first_number_formula = QPixmap()
        self.first_number_formula.load("formulas/number1/prob_formulas.png")

        self.prom = QPixmap()
        self.prom.load("formulas/number3/prom3")

        self.sobs = [QPixmap() for i in range(0, 4)]
        for i in range(1, 5):
            self.sobs[i - 1].load("formulas/number3/sob" + str(i))

        self.vers = [QPixmap() for i in range(0, 4)]
        for i in range(1, 5):
            self.vers[i - 1].load("formulas/number3/ver" + str(i))

        self.fourth_number_formulas = [QPixmap() for i in range(0, 2)]
        self.fourth_number_formulas[1].load("formulas/number4/bayes.png")
        self.fourth_number_formulas[0].load("formulas/number4/total_prob.png")
        # ----------------------------------

        # ----------коннекты-----------
        self.ui_widget.task_selection.currentIndexChanged.connect(self.task_changed)
        self.ui_widget.compute_button.clicked.connect(self.set_answer)
        self.ui_widget.compute_button_2.clicked.connect(self.set_answer)
        self.ui_widget.compute_button_3.clicked.connect(self.set_answer)

        self.ui_widget.subtask_CB.currentIndexChanged.connect(self.set_formulas)
        self.ui_widget.formulas_CB.currentIndexChanged.connect(self.set_formulas)
        # ----------------------------

        self.set_formulas()

    def set_behavior(self, new_behavior: AppBehavior):
        self.behavior = new_behavior

    def get_user_data(self) -> str:
        match self.behavior:
            case AppBehavior.scheme_task:
                return self.ui_widget.data_LE.text()
            case AppBehavior.student_task:
                return (f'{self.ui_widget.subtask_CB.currentIndex()};{self.ui_widget.m1_LE.text()};'
                        f'{self.ui_widget.m2_LE.text()};{self.ui_widget.n_LE.text()}')
            case AppBehavior.bayes_task:
                i = self.ui_widget.gip_number.text()
                i = '0' if len(i) == 0 else i
                return (f'{self.ui_widget.formulas_CB.currentIndex()};'
                        f'{self.ui_widget.gipotez_LE.text()};{self.ui_widget.lineEdit_2.text()};{i}')

    def set_answer(self):
        answer = self.calculator.calculate(self.get_user_data())
        match self.behavior:
            case AppBehavior.scheme_task:
                self.ui_widget.answer_label.setText(answer)
            case AppBehavior.student_task:
                self.ui_widget.answer_label_2.setText(answer[answer.find('_') + 1:])
                self.ui_widget.probVer_answer_label.setText(answer[0: answer.find('_')])
            case AppBehavior.bayes_task:
                self.ui_widget.answer_label_3.setText(answer)

    def task_changed(self):
        self.notify_observers()
        self.change_page()

    def change_page(self):
        self.ui_widget.stackedWidget.setCurrentIndex(2 - self.behavior.value)
        self.set_formulas()

    def set_formulas(self):
        match self.behavior:
            case AppBehavior.scheme_task:
                self.ui_widget.sheme_label.setPixmap(self.scheme_pixmap)
                self.ui_widget.formulas_label.setPixmap(self.first_number_formula)
            case AppBehavior.student_task:
                self.ui_widget.promVer_formul_label.setPixmap(self.prom)
                self.ui_widget.sob_formul_label.setPixmap(
                    self.sobs[self.ui_widget.subtask_CB.currentIndex()]
                )
                self.ui_widget.ver_formul_label.setPixmap(
                    self.vers[self.ui_widget.subtask_CB.currentIndex()]
                )
            case AppBehavior.bayes_task:
                self.ui_widget.formulas_label_2.setPixmap(
                    self.fourth_number_formulas[self.ui_widget.formulas_CB.currentIndex()]
                )

    def get_new_behavior(self) -> AppBehavior:
        return self.ui_widget.task_selection.currentIndex()

    def register_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self):
        for o in self.observers:
            o.notify_observer()
