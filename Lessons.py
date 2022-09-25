from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QWidget
from Chapters import ChaptersWidget

from os import getcwd
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextDocument
from PyQt5.QtWidgets import QLabel, QPushButton, QVBoxLayout, QWidget, QHBoxLayout


class LessonsWidget(QWidget):
    """Widget that displays rich text documents in pages."""

    def __init__(self):
        """Initialize LessonsWidget."""
        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)

        lesson1 = QPushButton('Μάθημα 1')
        lesson2 = QPushButton('Μάθημα 2')
        lesson3 = QPushButton('Μάθημα 3')

        horizontalbox = QHBoxLayout()

        layout.addLayout(horizontalbox)
        
        back = QPushButton('Πίσω')

        layout.addWidget(lesson1)
        layout.addWidget(lesson2)
        layout.addWidget(lesson3)
        layout.addWidget(back)

        lesson1.clicked.connect(self.Lesson1)
        lesson2.clicked.connect(self.Lesson2)
        lesson3.clicked.connect(self.Lesson3)
        back.clicked.connect(self.Back)

    def Lesson1(self) -> None:
        self.LoadLessons(1)

    def Lesson2(self) -> None:
        self.LoadLessons(2)

    def Lesson3(self) -> None:
        self.LoadLessons(3)

    def LoadLessons(self, lessonNumber) -> None:
        """"""
        match lessonNumber:
            case 1:
                #Load Chapter 1 in self.htmlText
                chapter = ChaptersWidget(1)
            case 2:
                #Load Chapter 2 in self.htmlText
                """"""
                chapter = ChaptersWidget(2)
            case 3:
                #Load Chapter 3 in self.htmlText
                """"""
                chapter = ChaptersWidget(3)

        stack = self.parentWidget()
        stack.addWidget(chapter)
        stack.setCurrentWidget(chapter)

    def Back(self) -> None:
        """Go back to main page.

        Use the parent widget (QStacked) to set the previous widget as the current; then delete this one
        """
        parent = self.parentWidget()

        # print(parent.currentIndex())
        old_widget = parent.currentWidget()
        parent.setCurrentIndex(parent.currentIndex() - 1)
        parent.removeWidget(old_widget)


