#!/usr/bin/env python3
"""Education application."""

from sys import argv

from PyQt5.QtWidgets import (QAction, QApplication, QMainWindow, QMenu,
                             QMenuBar, QMessageBox, QPushButton,
                             QStackedWidget, QVBoxLayout, QWidget)

from Exercises import ExercisesWidget
from Lessons import LessonsWidget

##test

class FirstWindow(QMainWindow):
    """Main window."""

    def __init__(self) -> None:
        """Initialize the FirstWindow.

        Initialize the layout, encapsulate in a QStackedWidget and set it as the central Widget.
        """
        super().__init__()

        layout = QVBoxLayout()

        button = QPushButton('Μαθήματα')

        def openLessons():
            """TBD."""    
            viewer = LessonsWidget()
            self.centralWidget().addWidget(viewer)
            self.centralWidget().setCurrentWidget(viewer)

        button.clicked.connect(openLessons)
        layout.addWidget(button)

        button = QPushButton('Ασκήσεις')

        def openExercises() -> None:
            widget = ExercisesWidget()
            self.centralWidget().addWidget(widget)
            self.centralWidget().setCurrentWidget(widget)
        button.clicked.connect(openExercises)

        layout.addWidget(button)
        button = QPushButton('Στατιστικά')

        def openStatistics() -> None:
            alert = QMessageBox()
            alert.setText('You clicked Στατιστικά!')
            alert.exec()
            button.clicked.connect(openStatistics)
        layout.addWidget(button)

        button = QPushButton('Έξοδος')

        def exit() -> None:
            reply = QMessageBox.question(self, "QMessageBox.question()", "Σίγουρα θέλεις να τερματήσεις την εφαρμογή;", QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)

            if reply == QMessageBox.Yes:
                self.close()
            elif reply == QMessageBox.No:
                pass
        button.clicked.connect(exit)
        layout.addWidget(button)

        widget = QWidget()
        widget.setLayout(layout)
        stacked = QStackedWidget()
        stacked.addWidget(widget)

        self.setCentralWidget(stacked)
        self.setWindowTitle("TEST")

        # MenuBar
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("File")
        exitButton = QAction('Exit',self)
        exitButton.triggered.connect(exit)
        fileMenu.addAction(exitButton)



def main():
    """Main."""
    app = QApplication(argv)
    window = FirstWindow()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
