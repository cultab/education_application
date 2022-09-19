from PyQt5.QtWidgets import QApplication, QPushButton, QVBoxLayout, QGridLayout, QRadioButton, QLabel, QWidget, QHBoxLayout, QMainWindow, QStackedWidget


class ExercisesWidget(QWidget):
    """Window layout for choosing a set of exercises."""

    def __init__(self):
        """Initialize ExercisesLayout."""
        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)

        lesson1 = QPushButton('Ασκήσεις Μαθήματος 1')
        lesson2 = QPushButton('Ασκήσεις Μαθήματος 2')
        lesson3 = QPushButton('Ασκήσεις Μαθήματος 3')
        back = QPushButton('Πίσω')

        layout.addWidget(lesson1)
        layout.addWidget(lesson2)
        layout.addWidget(lesson3)
        layout.addWidget(back)

        lesson1.clicked.connect(self.Exercises1)
        lesson2.clicked.connect(self.Exercises2)
        lesson3.clicked.connect(self.Exercises3)
        back.clicked.connect(self.Back)

    def Exercises1(self):
        pass

    def Exercises2(self):
        pass

    def Exercises3(self):
        pass

    def Back(self):
        print(self.parentWidget().currentIndex())
        widget = self.parentWidget().currentWidget()
        self.parentWidget().setCurrentIndex(self.parentWidget().currentIndex() -1 )
        self.parentWidget().removeWidget(widget)
