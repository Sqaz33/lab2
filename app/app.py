from PyQt5 import QtWidgets
from .form import Ui_Widget
from .ui import Ui
from calculator import *
from app_behavior import AppBehavior

import sys


class App:
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.Widget = QtWidgets.QWidget()
        self.calculator = Calculator(AppBehavior.scheme_task)
        widget = Ui_Widget()
        widget.setupUi(self.Widget)
        self.ui = Ui(widget, self.calculator, AppBehavior.scheme_task)

    def run(self):
        self.Widget.show()
        sys.exit(self.app.exec_())

    def notify_observer(self):
        behavior = self.ui.get_new_behavior()
        self.ui.set_behavior(behavior)
        self.calculator.set_behavior(behavior)



