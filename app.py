#!/usr/bin/env python3
"""Education application."""

from PyQt5.QtWidgets import QMessageBox, QPushButton, QWidget, QApplication, QVBoxLayout

from MultipleChoice import MultipleChoiceLayout, MultipleChoiceQuestion


class FirstWindow(QWidget):
    """Return The First Window a user sees in the application.

    Args:
        None

    Returns:
        QWidget: The QWidget that is to be shown in the QApplication
    """

    def openLessons(self):
        """Event handler for the button Μαθήματα.

        Args:
            None

        Returns:
            Nothing

        """

    def openExercises(self): ############# TO DO FIX BACK BUTTON ##########################
        """Event handler for the button Ασκήσεις.

        Args:
            None

        Returns:
            Nothing

        """

        layout = QVBoxLayout()
        button = QPushButton('Ασκήσεις Μαθήματος 1')
        button.clicked.connect(self.Exercises1)
        layout.addWidget(button)
        button = QPushButton('Ασκήσεις Μαθήματος 2')
        button.clicked.connect(self.Exercises2)
        layout.addWidget(button)
        button = QPushButton('Ασκήσεις Μαθήματος 3')
        button.clicked.connect(self.Exercises3)
        layout.addWidget(button)
        button = QPushButton('Πίσω')
        button.clicked.connect(self.Back)
        layout.addWidget(button)

        self.prevLayout = self.layout()
        QWidget().setLayout(self.layout())
        self.setLayout(layout)

    def openStatistics():
        """Event handler for the button Στατιστικά.

        Args:
            None

        Returns:
            Nothing

        """
        alert = QMessageBox()
        alert.setText('You clicked Στατιστικά!')
        alert.exec()

    def exit(self):
        """Event handler for the button Έξοδος.

        Args:
            Nothing

        Returns:
            Nothing
        """
        reply = QMessageBox.question(self, "QMessageBox.question()", "Σίγουρα θέλεις να τερματήσεις την εφαρμογή;", QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)

        match reply:
            case QMessageBox.Yes:
                self.close()
            case QMessageBox.No:
                pass
            case _:
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

        self.setLayout(layout)


def main():
    app = QApplication([])
    window = FirstWindow()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
