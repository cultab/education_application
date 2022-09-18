from unicodedata import name
from PyQt5.QtWidgets import *

def Lessons():
    """This is the event handler for the button Μαθήματα

    Args:
        None

    Returns:
        Nothing 
    
    """
    alert = QMessageBox()
    alert.setText('You clicked Μαθήματα!')
    alert.exec()

def Exercises():
    """This is the event handler for the button Ασκήσεις

    Args:
        None

    Returns:
        Nothing 
    
    """
    alert = QMessageBox()
    alert.setText('You clicked Ασκήσεις!')
    alert.exec()

def Statistics():
    """This is the event handler for the button Στατιστικά

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


def FirstWindow() -> QWidget:
    """Returns The First Window a User sees in the application

    Args:
        None
    
    Returns:
        QWidget: The QWidget that is to be shown in the QApplication
    
    """
    window = QWidget()

    layout = QVBoxLayout()
    button = QPushButton('Μαθήματα')
    button.clicked.connect(Lessons)
    layout.addWidget(button)
    button = QPushButton('Ασκήσεις')
    button.clicked.connect(Exercises)
    layout.addWidget(button)
    button = QPushButton('Στατιστικά')
    button.clicked.connect(Statistics)
    layout.addWidget(button)
    button = QPushButton('Έξοδος')
    button.clicked.connect(Exit)
    layout.addWidget(button)

    window.setLayout(layout)

    return window



def main():
    app = QApplication([])
    window = FirstWindow()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()