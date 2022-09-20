#!/usr/bin/env python3
"""Education application."""

from PyQt5.QtWidgets import QMessageBox, QPushButton, QWidget, QApplication, QVBoxLayout, QStackedWidget, QMainWindow
from sys import argv
from Exercises import ExercisesWidget


class FirstWindow(QMainWindow):
    """This is the First Window a user sees in the application.
    """

    def openLessons(self):
        """TBD"""
        pass

    def openExercises(self):
        """Event handler for the button Ασκήσεις. Create the Exercise Widget from Exercises.py then set it as the current Widget

        Args:
            self: Mandatory

        Returns:
            Nothing

        """

        widget = ExercisesWidget()
        self.centralWidget().addWidget(widget)
        self.centralWidget().setCurrentWidget(widget)
        

    def openStatistics():
        """TBD"""
        alert = QMessageBox()
        alert.setText('You clicked Στατιστικά!')
        alert.exec()

    def exit(self):
        """Event handler for the button Έξοδος. Create an exit event and handle the answer

        Args:
            self: Mandatory

        Returns:
            Nothing

        """

        reply = QMessageBox.question(self, "QMessageBox.question()", "Σίγουρα θέλεις να τερματήσεις την εφαρμογή;", QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)

        if reply == QMessageBox.Yes:
            self.close()
        elif reply == QMessageBox.No:
            pass

    def __init__(self):
        """Constructor of FirstWindow class. Initialize the layout, encapsulate in a QStackedWidget and set it as the central Widget

        Args:
            self: Mandatory

        Returns:
            Nothing
        """
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
    """"Main"""
    app = QApplication(argv)
    window = FirstWindow()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
