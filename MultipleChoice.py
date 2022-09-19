#!/usr/bin/env python
"""Multiple choice questions."""

from PyQt5.QtWidgets import QApplication, QPushButton, QVBoxLayout, QGridLayout, QRadioButton, QLabel, QWidget, QHBoxLayout


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
        """Initialize a MultipleChoiceQuestionWidget"""
        super().__init__()

        self.size = 2
        box = QVBoxLayout()

        self.setLayout(box)

        box.addWidget(QLabel(question.prompt))

        grid = QGridLayout()
        box.addLayout(grid)

        for i, choice in enumerate(question.choices):
            grid.addWidget(QRadioButton(choice), i - (i % self.size), i % self.size)


class MultipleChoiceLayout(QVBoxLayout):
    """Multiple choice layout."""

    def __init__(self, questions: list[MultipleChoiceQuestion]):
        """Initialize a MultipleChoiceLayout"""
        super().__init__()

        self.questions = questions
        self.currentQuestion = 0

        # add questions and hide them
        for question in questions:
            print(question)
            new = MultipleChoiceQuestionWidget(question)
            new.hide()
            self.addWidget(new)

        # show the first one
        self.itemAt(0).widget().show()

        # add next and prev buttons
        buttons = QHBoxLayout()
        self.addLayout(buttons)

        next = QPushButton("Επόμενη")
        prev = QPushButton("Προηγούμενη")
        buttons.addWidget(prev)
        buttons.addWidget(next)

        # add handlers
        next.clicked.connect(self.goto_next)
        prev.clicked.connect(self.goto_prev)

    def goto_next(self):
        """Handle going to next question."""
        if self.currentQuestion + 1 < len(self.questions):
            self.itemAt(self.currentQuestion).widget().hide()
            self.currentQuestion += 1
            self.itemAt(self.currentQuestion).widget().show()
        else:
            print("Last question reached.")

    def goto_prev(self):
        """Handle going to previous question."""
        if self.currentQuestion - 1 >= 0:
            self.itemAt(self.currentQuestion).widget().hide()
            self.currentQuestion -= 1
            self.itemAt(self.currentQuestion).widget().show()
        else:
            print("First question reached.")


def test():
    """Testing."""
    app = QApplication([])
    window = QWidget()

    question1 = MultipleChoiceQuestion("The number is 1. What's the number?", ["2", "23", "69", "1", "23", "26"], 3)
    question2 = MultipleChoiceQuestion("The number is 2. What's the number?", ["1", "2", "69", "2", "twenyone", "26"], 2)
    question3 = MultipleChoiceQuestion("The number is 3. What's the number?", ["3", "twenyone", "26"], 0)
    question4 = MultipleChoiceQuestion("The number is 4. What's the number?", ["1", "6", "4", "2", "twenyone", "26"], 2)

    window.setLayout(MultipleChoiceLayout([question1, question2, question3, question4]))

    window.show()
    app.exec()


if __name__ == "__main__":
    test()
