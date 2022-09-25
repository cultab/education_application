"""Exercises window."""
from PyQt5.QtWidgets import (QVBoxLayout, QPushButton, QWidget)
from Question import FillBlankQuestion, MultipleChoiceQuestion, QuestionWidget


class ExercisesWidget(QWidget):
    """Widget for choosing a set of exercises."""

    def __init__(self):
        """Initialize ExercisesWidget."""
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

    def Exercises1(self) -> None:
        """First set of exercises."""
        question1 = MultipleChoiceQuestion("The number is 1. What's the number?", ["2", "23", "69", "1", "23", "26"], 3)
        question2 = MultipleChoiceQuestion("The number is 2. What's the number?", ["1", "2", "69", "2", "twenyone", "26"], 2)
        question3 = MultipleChoiceQuestion("The number is 3. What's the number?", ["3", "twenyone", "26"], 0)
        question4 = MultipleChoiceQuestion("The number is 4. What's the number?", ["1", "6", "4", "2", "twenyone", "26"], 2)
        question5 = FillBlankQuestion("Fill in the blanks:", "1 + 1 =&" + "2 + 2 =&" + "4 + 4 =&", [2, 4, 8])

        stack = self.parentWidget()
        question = QuestionWidget([question5, question2, question3, question4, question1])
        stack.addWidget(question)
        stack.setCurrentWidget(question)

    def Exercises2(self):
        """TBD"""
        pass

    def Exercises3(self):
        """TBD"""
        pass

    def Back(self) -> None:
        """Go back to main page.

        Use the parent widget (QStacked) to set the previous widget as the current; then delete this one
        """
        parent = self.parentWidget()

        # print(parent.currentIndex())
        old_widget = parent.currentWidget()
        parent.setCurrentIndex(parent.currentIndex() - 1)
        parent.removeWidget(old_widget)
