"""Lesson screen."""

from PyQt5.QtWidgets import QVBoxLayout, QWidget
from PyQt5 import QtCore, QtGui

from Chapters import ChaptersWidget
from MenuButton import MenuButton


class LessonsWidget(QWidget):
    """Widget that displays rich text documents in pages."""

    def __init__(self):
        """Initialize LessonsWidget."""
        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)

        lesson1 = MenuButton('Φυσικοί Αριθμοί', "lessons")
        lesson2 = MenuButton('Κλάσματα', "lessons")
        lesson3 = MenuButton('Δεκαδικοί Αριθμοί', "lessons")
        back = MenuButton('Πίσω')
        back.setIcon(QtGui.QIcon("./resources/back.png"))
        back.setIconSize(QtCore.QSize(180, 180))

        layout.addWidget(lesson1)
        layout.addWidget(lesson2)
        layout.addWidget(lesson3)
        layout.addWidget(back)

        lesson1.clicked.connect(lambda _: self.LoadLessons(1))
        lesson2.clicked.connect(lambda _: self.LoadLessons(2))
        lesson3.clicked.connect(lambda _: self.LoadLessons(3))
        back.clicked.connect(self.Back)

    def LoadLessons(self, lessonNumber) -> None:
        """Load Lessons with lessonNumber."""
        chapter = ChaptersWidget(lessonNumber)

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


