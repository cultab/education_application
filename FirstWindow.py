#!/usr/bin/env python3
from PyQt5.QtWidgets import QMessageBox, QPushButton, QWidget, QApplication, QVBoxLayout

from app import MultipleChoiceLayout,MultipleChoiceQuestion

class FirstWindow(QWidget) :
    """Return The First Window a user sees in the application.

    Args:
        None

    Returns:
        QWidget: The QWidget that is to be shown in the QApplication
    """
    def Lessons(self):
        """Event handler for the button Μαθήματα.

        Args:
            None

        Returns:
            Nothing

        """
        
        

    def Exercises(self):
        """Event handler for the button Ασκήσεις.

        Args:
            None

        Returns:
            Nothing

        """
        question1 = MultipleChoiceQuestion("The number is 1. What's the number?", ["2", "23", "69", "1", "23", "26"], 3)
        question2 = MultipleChoiceQuestion("The number is 2. What's the number?", ["1", "2", "69", "2", "twenyone", "26"], 2)
        question3 = MultipleChoiceQuestion("The number is 3. What's the number?", ["3", "twenyone", "26"], 0)
        question4 = MultipleChoiceQuestion("The number is 4. What's the number?", ["1", "6", "4", "2", "twenyone", "26"], 2)

        self.setLayout(MultipleChoiceLayout([question1, question2, question3, question4]))


    def Statistics():
        """Event handler for the button Στατιστικά.

        Args:
            None

        Returns:
            Nothing

        """
        alert = QMessageBox()
        alert.setText('You clicked Στατιστικά!')
        alert.exec()

    def Exit():
        """This is the event handler for the button Έξοδος

        Args:
            None

        Returns:
            Nothing

        """
        alert = QMessageBox()
        alert.setText('You clicked Έξοδος!')
        alert.exec()


    def __init__(self):
        super().__init__()
    
        layout = QVBoxLayout()
        button = QPushButton('Μαθήματα')
        button.clicked.connect(self.Lessons)
        layout.addWidget(button)
        button = QPushButton('Ασκήσεις')
        button.clicked.connect(self.Exercises)
        layout.addWidget(button)
        button = QPushButton('Στατιστικά')
        button.clicked.connect(self.Statistics)
        layout.addWidget(button)
        button = QPushButton('Έξοδος')
        button.clicked.connect(self.Exit)
        layout.addWidget(button)

        self.setLayout(layout)


def main():
    app = QApplication([])
    window = FirstWindow()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
