from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QWidget

from Chapters import ChaptersWidget


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
        back = QPushButton('Πίσω')

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


