#!/usr/bin/env python
"""Multiple choice questions."""

from PyQt5.QtWidgets import QApplication, QPushButton, QVBoxLayout, QGridLayout, QRadioButton, QLabel, QWidget, QHBoxLayout, QStackedWidget, QLineEdit

from re import sub
from FlowLayout import FlowLayout


class FillBlankQuestion():
    """
    A fill-in-the-blanks question.

    The character '&' in text represents a text box the
    student is expected to fill. '&' can be escaped using a
    forward slash.

    The unescaped '&' character's count shall equal to that of the
    answers.
    """

    prompt: str
    text: str
    correct: list[str]
    answers: list[str]

    def __init__(self, prompt: str, text: str, correct: list[str]):
        """Initialize a FillBlankQuestion."""
        self.prompt = prompt
        self.text = text
        self.correct = [str(x) for x in correct]  # convert to string
        self.answers = list()

    def __repr__(self):
        """Return string representation."""
        return f"{self.prompt=} {self.text=} {self.correct=} {self.answers=}"


class FillBlankQuestionWidget(QWidget):
    """Fill in the blanks question widget."""

    question: FillBlankQuestion
    answers: list[QLineEdit]

    def __init__(self, question: FillBlankQuestion):
        """Initialize a FillBlankQuestionWidget."""
        super().__init__()

        self.question = question
        self.answers = list()
        layout = FlowLayout(0, 0, 0)
        self.setLayout(layout)

        layout.addWidget(QLabel(self.question.prompt))

        text = sub(r"\\&", "<ambersand>", self.question.text)
        print(text)
        texts = text.split(sep="&")
        print(texts)

        for text in texts[:-1]:
            t = QLabel(text)
            e = QLineEdit()
            self.answers.append(e)
            layout.addWidget(t)
            layout.addWidget(e)

    def getQuestion(self) -> FillBlankQuestion:
        """Get answered question."""
        answers = list()
        for answer in self.answers:
            answers.append(answer.text())
        self.question.answers = answers
        return self.question


class MultipleChoiceQuestion():
    """A multiple choice question."""

    prompt: str
    choices: list[str]
    correct: list[str]
    answer: str

    def __init__(self, prompt: str, choices: list[str], correctChoice: str):
        """Initialize a MultipleChoiceQuestion."""
        self.prompt = prompt
        self.choices = choices
        self.correct = correctChoice
        self.answer = ""

    def __repr__(self) -> str:
        """Return string representation."""
        return f"{self.prompt} {self.choices} -> {self.choices[self.correct]}"


class MultipleChoiceQuestionWidget(QWidget):
    """Multiple choice question widget."""

    question: MultipleChoiceQuestion
    radio_buttons: list[QRadioButton]

    def __init__(self, question: MultipleChoiceQuestion):
        """Initialize a MultipleChoiceQuestionWidget."""
        super().__init__()

        self.question = question
        self.size = 2
        box = QVBoxLayout()

        self.setLayout(box)

        box.addWidget(QLabel(self.question.prompt))

        grid = QGridLayout()
        box.addLayout(grid)

        self.radio_buttons = list()

        for i, choice in enumerate(self.question.choices):
            radio = QRadioButton(choice)
            grid.addWidget(radio, i - (i % self.size), i % self.size)
            self.radio_buttons.append(radio)

    def getQuestion(self) -> MultipleChoiceQuestion:
        """Return answered question."""
        answer = ""
        for radio in self.radio_buttons:
            if radio.isChecked():
                answer = radio.text()
        self.question.answer = answer

        return self.question


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
                case FillBlankQuestion():
                    new = FillBlankQuestionWidget(question)
                case _:
                    raise NotImplementedError(question)
            self.stack.addWidget(new)

        # show the first one
        self.stack.setCurrentIndex(0)

        # add next and prev buttons
        buttons = QHBoxLayout()
        layout.addLayout(buttons)

        self.next = QPushButton("Επόμενη")
        self.prev = QPushButton("Προηγούμενη")
        self.prev.setEnabled(False)

        buttons.addWidget(self.prev)
        buttons.addWidget(self.next)

        # add handlers
        self.next.clicked.connect(self.goto_next)
        self.prev.clicked.connect(self.goto_prev)

    def goto_next(self):
        """Handle going to next question."""
        stack: QStackedWidget = self.stack
        if stack.currentIndex() + 1 < stack.count():
            stack.setCurrentIndex(stack.currentIndex() + 1)
            self.prev.setEnabled(True)

        if not stack.currentIndex() + 1 < stack.count():
            self.next.setText("Υποβολή")
            self.next.clicked.connect(self.submit)

    def goto_prev(self):
        """Handle going to previous question."""
        stack: QStackedWidget = self.stack
        if stack.currentIndex() - 1 >= 0:
            stack.setCurrentIndex(stack.currentIndex() - 1)
            self.next.clicked.connect(self.goto_next)
            self.next.setText("Επόμμενη")
            self.next.setEnabled(True)

        if not stack.currentIndex() - 1 >= 0:
            self.prev.setEnabled(False)
            print("First question reached.")

    def submit(self):
        """Submit answers."""
        for i in range(self.stack.count()):
            widget = self.stack.widget(i)
            answered = widget.getQuestion()
            print(answered)


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
