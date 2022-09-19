#!/usr/bin/env python
"""Multiple choice questions."""

from PyQt5.QtWidgets import QApplication, QPushButton, QVBoxLayout, QGridLayout, QRadioButton, QLabel, QWidget, QHBoxLayout, QStackedWidget
from functools import partial


class MultipleChoiceQuestion():
    """A multiple choice question."""

    def __init__(self, prompt: str, choices: list[str], correctChoice: str) -> None:
        """Initialize a MultipleChoiceQuestion"""
        self.prompt = prompt
        self.choices = choices
        self.correct = correctChoice

    def __repr__(self) -> str:
        """Return string representation."""
        return f"{self.prompt} {self.choices} -> {self.choices[self.correct]}"


class MultipleChoiceQuestionWidget(QWidget):
    """Multiple choice question widget."""

    def __init__(self, question: MultipleChoiceQuestion):
        """Initialize a MultipleChoiceQuestionWidget."""
        super().__init__()

        self.size = 2
        box = QVBoxLayout()

        self.setLayout(box)

        box.addWidget(QLabel(question.prompt))

        grid = QGridLayout()
        box.addLayout(grid)

        for i, choice in enumerate(question.choices):
            grid.addWidget(QRadioButton(choice), i - (i % self.size), i % self.size)

    def isCorrect(self) -> bool:
        """Check if question is answered correctly."""
        raise NotImplementedError


class QuestionWidget(QWidget):
    """Widget that displays questions."""

    def __init__(self, questions: list[any]):
        """
        Initialize a QuestionWidget.

        Must be initilized with > 1 questions.
        """
        super().__init__()

        self.questions = questions
        self.correctAnswers = 0
        self.stack = QStackedWidget()

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.stack = QStackedWidget()
        layout.addWidget(self.stack)

        # add questions
        new: QWidget = None
        for question in questions:
            # print(question)
            match question:
                case MultipleChoiceQuestion():
                    new = MultipleChoiceQuestionWidget(question)
                case _:
                    raise NotImplementedError(question)
            self.stack.addWidget(new)

        # show the first one
        self.stack.setCurrentIndex(0)

        # add next and prev buttons
        buttons = QHBoxLayout()
        layout.addLayout(buttons)

        next = QPushButton("Επόμενη")
        prev = QPushButton("Προηγούμενη")
        buttons.addWidget(prev)
        buttons.addWidget(next)

        def goto_next(next, prev):
            """Handle going to next question."""
            stack: QStackedWidget = self.stack
            if stack.currentIndex() + 1 < stack.count():
                stack.setCurrentIndex(stack.currentIndex() + 1)
                prev.setEnabled(True)
            else:
                next.setEnabled(False)
                print("Last question reached.")

        def goto_prev(next, prev):
            """Handle going to previous question."""
            stack: QStackedWidget = self.stack
            if stack.currentIndex() - 1 >= 0:
                stack.setCurrentIndex(stack.currentIndex() - 1)
                next.setEnabled(True)
            else:
                prev.setEnabled(False)
                print("First question reached.")

        n = partial(goto_next, next, prev)
        p = partial(goto_prev, next, prev)

        # add handlers
        next.clicked.connect(n)
        prev.clicked.connect(p)



def test():
    """Testing."""
    app = QApplication([])
    window = QWidget()

    question1 = MultipleChoiceQuestion("The number is 1. What's the number?", ["2", "23", "69", "1", "23", "26"], 3)
    question2 = MultipleChoiceQuestion("The number is 2. What's the number?", ["1", "2", "69", "2", "twenyone", "26"], 2)
    question3 = MultipleChoiceQuestion("The number is 3. What's the number?", ["3", "twenyone", "26"], 0)
    question4 = MultipleChoiceQuestion("The number is 4. What's the number?", ["1", "6", "4", "2", "twenyone", "26"], 2)

    window.setLayout(QuestionWidget([question1, question2, question3, question4]))

    window.show()
    app.exec()


if __name__ == "__main__":
    test()
