#!/usr/bin/env python3
"""Education application."""

from PyQt5.QtWidgets import QMessageBox, QPushButton, QWidget, QApplication, QVBoxLayout, QStackedWidget, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings
from PyQt5.QtCore import QUrl
from sys import argv
from Exercises import ExercisesWidget


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
            browser = QWebEngineView()
            browser.settings().setAttribute(QWebEngineSettings.PluginsEnabled, True)
            browser.settings().setAttribute(QWebEngineSettings.PdfViewerEnabled, True)
            browser.setUrl(QUrl.fromLocalFile("/home/asimakis/Desktop/test.pdf"))
            self.centralWidget().addWidget(browser)
            self.centralWidget().setCurrentWidget(browser)

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


def main():
    """Main."""
    app = QApplication(argv)
    window = FirstWindow()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
