#!/usr/bin/env python3
"""Education application."""

from sys import argv

from PyQt5.QtWidgets import (QAction, QApplication, QMainWindow, QMenu,
                             QMenuBar, QMessageBox, QPushButton,
                             QStackedWidget, QVBoxLayout, QWidget)

from PyQt5 import QtGui
from PyQt5 import QtCore

from Exercises import ExercisesWidget
from Lessons import LessonsWidget
from MenuButton import MenuButton


class FirstWindow(QMainWindow):
    """Main window."""

    def __init__(self) -> None:
        """Initialize the FirstWindow.

        Initialize the layout, encapsulate in a QStackedWidget and set it as the central Widget.
        """
        super().__init__()

        layout = QVBoxLayout()

        lessons = MenuButton('Μαθήματα', "lessons")

        def openLessons():
            """TBD."""
            viewer = LessonsWidget()
            self.centralWidget().addWidget(viewer)
            self.centralWidget().setCurrentWidget(viewer)

        lessons.clicked.connect(openLessons)
        layout.addWidget(lessons)

        exercises = MenuButton('Ασκήσεις', 'exercises')

        def openExercises() -> None:
            widget = ExercisesWidget()
            self.centralWidget().addWidget(widget)
            self.centralWidget().setCurrentWidget(widget)
        exercises.clicked.connect(openExercises)

        layout.addWidget(exercises)
        statistics = MenuButton('Στατιστικά', "statistics")

        def openStatistics() -> None:
            alert = QMessageBox()
            alert.setText('You clicked Στατιστικά!')
            alert.exec()
            exercises.clicked.connect(openStatistics)
        layout.addWidget(statistics)

        exit_app = MenuButton('Έξοδος', "exit")
        exit_app.setIcon(QtGui.QIcon("./resources/illustration-exit-door_53876-5844.jpg"))
        exit_app.setIconSize(QtCore.QSize(180, 180))
        exit_app.setProperty("cssClass", "bigButton")

        def exit() -> None:
            reply = QMessageBox.question(self, "QMessageBox.question()", "Σίγουρα θέλεις να τερματήσεις την εφαρμογή;", QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)

            if reply == QMessageBox.Yes:
                self.close()
            elif reply == QMessageBox.No:
                pass
        exit_app.clicked.connect(exit)
        layout.addWidget(exit_app)

        widget = QWidget()
        widget.setLayout(layout)
        stacked = QStackedWidget()
        stacked.addWidget(widget)

        self.setCentralWidget(stacked)
        self.setWindowTitle("TEST")

        # MenuBar
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("File")
        exitButton = QAction('Exit', self)
        exitButton.triggered.connect(exit)
        fileMenu.addAction(exitButton)


        # margin-right: 90%;
        # margin-left: 90%;
    # background-image: url(./resources/math-seamless-pattern_111409-585.jpg);
css = """
MenuButton {
    font-size: 48pt;
    color: dimgray;
    border: 10px solid white;
    border-radius: 30px;
    font-weight: bold;
}

MenuButton:hover {
        color: black;
        border: 10px solid black;
}

QPushButton#exercises {
    background-image: url(./resources/Hourglass_512.png);
}

QPushButton#lessons {
    background-image: url(./resources/math-seamless_256.jpg);
}

QPushButton#statistics {
    background-image: url(./resources/calculator_yellow.png);
}

"""


def main():
    """Main."""
    app = QApplication(argv)
    app.setStyleSheet(css)
    window = FirstWindow()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
