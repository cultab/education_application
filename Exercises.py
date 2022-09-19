from PyQt5.QtWidgets import QApplication, QPushButton, QVBoxLayout, QGridLayout, QRadioButton, QLabel, QWidget, QHBoxLayout, QMainWindow, QStackedWidget

from MultipleChoice import MultipleChoiceLayout, MultipleChoiceQuestion


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
        """"""

        # question1 = MultipleChoiceQuestion("The number is 1. What's the number?", ["2", "23", "69", "1", "23", "26"], 3)
        # question2 = MultipleChoiceQuestion("The number is 2. What's the number?", ["1", "2", "69", "2", "twenyone", "26"], 2)
        # question3 = MultipleChoiceQuestion("The number is 3. What's the number?", ["3", "twenyone", "26"], 0)
        # question4 = MultipleChoiceQuestion("The number is 4. What's the number?", ["1", "6", "4", "2", "twenyone", "26"], 2)
        # widget = QWidget()
        # widget.setLayout(MultipleChoiceLayout([question1, question2, question3, question4]))
        # self.parentWidget().addWidget(widget)
        # self.parentWidget().setCurrentWidget(widget)

    def Exercises2(self):
        pass

    def Exercises3(self):
        pass

    def Back(self):
        print(self.parentWidget().currentIndex())
        old_widget = self.parentWidget().currentWidget()
        self.parentWidget().setCurrentIndex(self.parentWidget().currentIndex() -1 )
        self.parentWidget().removeWidget(old_widget)
