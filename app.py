#!/usr/bin/env python3
"""Education application."""

from PyQt5.QtWidgets import QMessageBox, QPushButton, QWidget, QApplication, QVBoxLayout, QStackedWidget, QMainWindow
from sys import argv
from MultipleChoice import MultipleChoiceLayout, MultipleChoiceQuestion
from Exercises import ExercisesWidget


class FirstWindow(QMainWindow):
    """Return The First Window a user sees in the application.

    Args:
        None

    Returns:
        QWidget: The QWidget that is to be shown in the QApplication
    """

    def openLessons(self):
        pass

    def openExercises(self):
        """Event handler for the button Ασκήσεις.

        Args:
            None

        Returns:
            Nothing

        """

        widget = ExercisesWidget()
        self.centralWidget().addWidget(widget)
        self.centralWidget().setCurrentWidget(widget)
# =======
#         prevLayout = self.layout()
#         QWidget().setLayout(self.layout())
#         self.setLayout(ExercisesLayout(prevLayout))

    def openStatistics():
        alert = QMessageBox()
        alert.setText('You clicked Στατιστικά!')
        alert.exec()

    def exit(self):
        reply = QMessageBox.question(self, "QMessageBox.question()", "Σίγουρα θέλεις να τερματήσεις την εφαρμογή;", QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)

        if reply == QMessageBox.Yes:
                self.close()
        elif reply == QMessageBox.No:
                pass        

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        button = QPushButton('Μαθήματα')
        button.clicked.connect(self.openLessons)
        layout.addWidget(button)
        button = QPushButton('Ασκήσεις')
        button.clicked.connect(self.openExercises)
        layout.addWidget(button)
        button = QPushButton('Στατιστικά')
        button.clicked.connect(self.openStatistics)
        layout.addWidget(button)
        button = QPushButton('Έξοδος')
        button.clicked.connect(self.exit)
        layout.addWidget(button)

        widget = QWidget()
        widget.setLayout(layout)
        stacked = QStackedWidget()
        stacked.addWidget(widget)

        self.setCentralWidget(stacked)


def main():
    app = QApplication(argv)
    window = FirstWindow()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
