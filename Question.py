#!/usr/bin/env python
"""Multiple choice questions."""

from typing import Protocol
from os import getcwd

from PyQt5 import QtGui
from PyQt5.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLineEdit,
                             QListWidget, QListWidgetItem, QPushButton,
                             QRadioButton, QStackedWidget, QVBoxLayout,
                             QWidget)

from FlowLayout import FlowLayout
from WrapLabel import WrapLabel


class Question(Protocol):
    """
    Protocol defining a Question.

    Questions are required to have 2 attributes:

    * A prompt
    * An answer
    """

    prompt: str
    correct: str | list[str]
    answer: str | list[str]

    def isCorrect() -> bool:
        """Return whether the question has the correct answer."""
        raise NotImplementedError("Question is a protocol and has no implementation of isCorrect().")


class FillBlankQuestion():
    """
    A fill-in-the-blanks question.

    The '&' character in text represents a text box the
    student is expected to fill.

    The '&' character's count shall equal to that of the
    answers.
    """

    prompt: str
    text: str
    correct: list[str]
    answer: list[str]

    def __init__(self, prompt: str, text: str, correct: list[str]):
        """Initialize a FillBlankQuestion."""
        self.prompt = prompt
        self.text = text
        self.correct = [str(x) for x in correct]  # convert to string
        self.answer = list()

        if not len(self.correct) == self.text.count("&"):
            raise ValueError(f"Must give the same count of '&' characters and correct answers. Gave {len(self.correct)} correct answers and {self.text.count('&')} '&' characters.\n{self}")

    def __repr__(self):
        """Return string representation."""
        return f"{self.prompt=} {self.text=} {self.correct=} {self.answer=}"

    def isCorrect(self, index: int) -> bool:
        """Return whether a subquestion has the correct answer."""
        return self.answer[index] == self.correct[index]


class FillBlankQuestionWidget(QWidget):
    """Fill in the blanks question widget."""

    question: FillBlankQuestion
    answer: list[QLineEdit]

    def __init__(self, question: FillBlankQuestion, *args, **kwargs):
        """Initialize a FillBlankQuestionWidget."""
        super(FillBlankQuestionWidget, self).__init__(*args, **kwargs)

        self.question = question
        self.answer = list()
        layout = FlowLayout(0, 0, 0)
        self.setLayout(layout)

        layout.addWidget(WrapLabel(self.question.prompt))
        layout.newRow()

        letters = [*self.question.text]

        text = ""
        widget: QWidget = None
        for c in letters:
            match c:
                case "&" | "\n":
                    if text:
                        layout.addWidget(WrapLabel(text))
                        text = ""
                    match c:
                        case "&":
                            widget = QLineEdit()
                            layout.addWidget(widget)
                            self.answer.append(widget)
                        case "\n":
                            layout.newRow()
                case _:
                    text = text + c
        else:
            if text:
                layout.addWidget(WrapLabel(text))

    def getQuestion(self) -> FillBlankQuestion:
        """Get answered question."""
        answers = list()
        for answer in self.answer:
            answers.append(answer.text())
        self.question.answer = answers
        return self.question


class MultipleChoiceQuestion():
    """A multiple choice question."""

    prompt: str
    choices: list[str]
    correct: list[str]
    answer: str

    def __init__(self, prompt: str, choices: list[str], correctChoice: str):
        """
        Initialize a MultipleChoiceQuestion.

        correctChoice indexes the list choices
        """
        self.prompt = prompt
        self.choices = choices
        self.correct = correctChoice
        self.answer = ""

    def __repr__(self) -> str:
        """Return string representation."""
        return f"{self.prompt} {self.choices} -> {self.choices[self.correct]}"

    def isCorrect(self) -> bool:
        """Return whether the question has the correct answer."""
        if self.answer == self.choices[self.correct]:
            return True
        return False


class MultipleChoiceQuestionWidget(QWidget):
    """Multiple choice question widget."""

    question: MultipleChoiceQuestion
    radio_buttons: list[QRadioButton]

    def __init__(self, question: MultipleChoiceQuestion, *args, **kwargs):
        """Initialize a MultipleChoiceQuestionWidget."""
        super(MultipleChoiceQuestionWidget, self).__init__(*args, **kwargs)

        self.question = question
        self.size = 2
        box = QVBoxLayout()

        self.setLayout(box)

        box.addWidget(WrapLabel(self.question.prompt))

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

    def __init__(self, questions: list[any], question_set: str):
        """
        Initialize a QuestionWidget.

        Must be initilized with > 1 questions.
        """
        super().__init__()

        self.questions = questions
        self.name = question_set
        self.stack = QStackedWidget()

        if not len(questions) > 1:
            raise ValueError("QuestionWidget requires to be initilized with >1 questions.")

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
            self.next.clicked.disconnect(self.goto_next)
            self.next.clicked.connect(self.submit)

    def goto_prev(self):
        """Handle going to previous question."""
        stack: QStackedWidget = self.stack
        if stack.currentIndex() - 1 >= 0:
            stack.setCurrentIndex(stack.currentIndex() - 1)
            self.next.clicked.disconnect(self.goto_next)
            self.next.clicked.connect(self.goto_next)
            self.next.setText("Επόμμενη")
            self.next.setEnabled(True)

        if not stack.currentIndex() - 1 >= 0:
            self.prev.setEnabled(False)
            print("First question reached.")

    def submit(self):
        """Submit answers."""
        answered = list()
        for i in range(self.stack.count()):
            widget = self.stack.widget(i)
            answered.append(widget.getQuestion())

        stack = self.parentWidget()

        widget = OverviewListWidget(answered, self.name)
        stack.addWidget(widget)
        stack.setCurrentWidget(widget)
        # remove QuestionWidget
        stack.removeWidget(self)


class OverviewQuestionWidget(QWidget):
    """Widget that shows the results a single question."""

    def __init__(self, question: Question):
        """Initialize an OverviewQuestionWidget."""
        super(OverviewQuestionWidget, self).__init__()
        self.marks = 0
        horizontal = QVBoxLayout()

        self.setLayout(horizontal)

        # prepare labels
        correct_label = WrapLabel("Σωστό")
        correct_label.setStyleSheet("color: seagreen; font-weight: bold")
        wrong_label = WrapLabel("Λάθος")
        wrong_label.setStyleSheet("color: crimson; font-weight: bold")
        middle_label = WrapLabel("Σχεδόν")
        middle_label.setStyleSheet("color: goldenrod; font-weight: bold")

        # right side of widget
        right = QVBoxLayout()

        # add question prompt
        prompt = WrapLabel(question.prompt)
        prompt.setStyleSheet("color: indigo; font-weight: bold; font-size: 120%;")
        right.addWidget(prompt)

        # add question details based on question's type
        match question:
            case FillBlankQuestion():
                flow = FlowLayout()
                right.addLayout(flow)

                all_correct = True
                all_false = True
                labels: list[QWidget] = list()
                for answer, correct in zip(question.answer, question.correct):
                    if answer == correct:
                        self.marks += 1
                        all_false = False
                        label = WrapLabel(answer)
                        label.setStyleSheet("color: seagreen; font-weight: bold")
                        labels.append([label])
                    else:
                        all_correct = False
                        correction = list()
                        label = WrapLabel(answer)
                        label.setStyleSheet("color: crimson; font-weight: bold")
                        correction.append(label)
                        label = WrapLabel(correct)
                        label.setStyleSheet("color: seagreen; background-color: black; font-weight: bold")
                        correction.append(label)
                        labels.append(correction)

                if all_correct:
                    horizontal.addWidget(correct_label, 0)
                elif all_false:
                    horizontal.addWidget(wrong_label, 0)
                else:
                    horizontal.addWidget(middle_label, 0)

                letters = [*question.text]

                text = ""
                i = 0
                for c in letters:
                    match c:
                        case "&":
                            if text:
                                flow.addWidget(WrapLabel(text))
                                text = ""
                                for label in labels[i]:
                                    flow.addWidget(label)
                                i += 1
                        case "\n":
                            flow.newRow()
                        case _:
                            text = text + c
                else:
                    if text:
                        flow.addWidget(WrapLabel(text))

            case MultipleChoiceQuestion():
                flow = FlowLayout()
                right.addLayout(flow)

                correct = WrapLabel(question.choices[question.correct])
                correct.setStyleSheet("color: seagreen; font-weight: bold")
                no_answer = WrapLabel("Χωρίς Απάντηση")
                no_answer.setStyleSheet("color: goldenrod; font-weight: bold")

                if question.isCorrect():
                    self.marks += 1
                    horizontal.addWidget(correct_label, 0)
                    flow.addWidget(correct)
                elif not question.answer:
                    horizontal.addWidget(wrong_label, 0)
                    flow.addWidget(no_answer)
                else:
                    horizontal.addWidget(wrong_label, 0)
                    false = WrapLabel(question.answer)
                    false.setStyleSheet("color: crimson; font-weight: bold")

                    # add correct answer and given answer
                    flow.addWidget(correct)
                    flow.addWidget(WrapLabel(" | "))
                    flow.addWidget(false)
            case _:
                right.addWidget(WrapLabel("Prompt here and stuff also more text and things."))
                right.addWidget(WrapLabel("More text here and stuff also EVEN more text and things."))

        horizontal.addLayout(right, 100)


class OverviewListWidget(QListWidget):
    """Widget that contains a list of OverviewQuestionWidgets."""

    def __init__(self, questions: list[Question], question_set: str):
        """Initialize OverviewWidget with a list of Questions."""
        super(OverviewListWidget, self).__init__()

        # layout = QVBoxLayout()
        # self.setLayout(layout)
        # self.setUniformItemSizes(False)
        # self.setResizeMode(QListWidget.Adjust)
        # self.setSelectionRectVisible(True)

        for question in questions:
            overview_widget = OverviewQuestionWidget(question)  # question widget
            # layout.addWidget(widget)
            item = QListWidgetItem(self)
            item.setSizeHint(overview_widget.sizeHint())
            self.addItem(item)
            self.setItemWidget(item, overview_widget)  # associate item with widget

        back = QPushButton("Τέλος Άσκησης")
        back.clicked.connect(self.Back)
        item = QListWidgetItem(self)
        item.setSizeHint(back.sizeHint())
        self.addItem(item)
        self.setItemWidget(item, back)

        total_marks = overview_widget.marks / len(questions)

        with open(getcwd() + "/results.csv", 'a') as results:
            results.write(f'"{question_set}",{total_marks}\n')



    def Back(self) -> None:
        """Go back to main page.

        Use the parent widget (QStacked) to set the previous widget
        as the current, then delete this one.
        """
        parent = self.parentWidget()

        old_widget = parent.currentWidget()
        parent.setCurrentIndex(parent.currentIndex() - 1)
        parent.removeWidget(old_widget)


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
