#!/usr/bin/env python
"""Multiple choice questions."""

from PyQt5.QtWidgets import QApplication, QPushButton, QVBoxLayout, QGridLayout, QRadioButton, QLabel, QWidget, QHBoxLayout


class MultipleChoiceQuestion():
    """A multiple choice question."""

    def __init__(self, p, ch, cor):
        """."""
        self.prompt = p
        self.choices = ch
        self.correct = cor


class MultipleChoiceQuestionWidget(QVBoxLayout):
    """Multiple choice question widget."""

    def __init__(self, question: MultipleChoiceQuestion):
        """Init."""
        self.size = 2

        super().__init__()
        self.addWidget(QLabel(question.prompt))

        grid = QGridLayout()
        self.addLayout(grid)

        for i, choice in enumerate(question.choices):
            grid.addWidget(QRadioButton(choice), i - (i % self.size), i % self.size)


class MultipleChoiceContainer(QVBoxLayout):
    """Multiple choice ."""

    def __init__(self, questions: list[MultipleChoiceQuestion]):
        """Init."""
        super().__init__()

        self.questions = questions
        self.currentQuestion = 0

        # init first question
        self.currentQuestionWidget = QWidget()
        self.currentQuestionWidget.setLayout(MultipleChoiceQuestionWidget(self.questions[self.currentQuestion]))
        self.addWidget(self.currentQuestionWidget)

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
        print("next")
        if self.currentQuestion + 1 < len(self.questions):
            self.currentQuestion += 1
            self.goto_current()
        else:
            print("Last question reached.")

        print(self.currentQuestion)

    def goto_prev(self):
        """Handle going to previous question."""
        print("prev")
        if self.currentQuestion - 1 >= 0:
            self.currentQuestion -= 1
            self.goto_current()
        else:
            print("First question reached.")

        print(self.currentQuestion)

    def goto_current(self):
        """Show the question corresponding to @self.currentQuestion."""
        old = self.currentQuestionWidget
        new = QWidget()

        # set new widgets content to a new MultipleChoiceQuestionWidget
        new.setLayout(MultipleChoiceQuestionWidget(self.questions[self.currentQuestion]))
        # replace the old with the new
        self.replaceWidget(old, new)
        # close the old
        old.hide()
        # update current
        self.currentQuestionWidget = new


def main():
    """Entry."""
    app = QApplication([])
    window = QWidget()

    question1 = MultipleChoiceQuestion("The number is 1. What's the number?", ["2", "23", "69", "1", "23", "26"], 3)
    question2 = MultipleChoiceQuestion("The number is 2. What's the number?", ["1", "2", "69", "2", "twenyone", "26"], 2)
    question3 = MultipleChoiceQuestion("The number is 3. What's the number?", ["3", "twenyone", "26"], 0)
    question4 = MultipleChoiceQuestion("The number is 4. What's the number?", ["1", "6", "4", "2", "twenyone", "26"], 2)

    window.setLayout(MultipleChoiceContainer([question1, question2, question3, question4]))

    window.show()
    app.exec()


if __name__ == "__main__":
    main()
