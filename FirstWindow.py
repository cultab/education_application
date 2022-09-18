from unicodedata import name
from PyQt5.QtWidgets import *

def FirstWindow() -> QWidget:
    """Returns The First Window a User sees in the application

    Args:
        None
    
    Returns:
        QWidget: The QWidget that is to be shown in the QApplication
    
    """
    window = QWidget()

    layout = QVBoxLayout()
    layout.addWidget(QPushButton('Μαθήματα'))
    layout.addWidget(QPushButton('Ασκήσεις'))
    layout.addWidget(QPushButton('Στατιστικά'))
    layout.addWidget(QPushButton('Έξοδος'))

    window.setLayout(layout)

    return window



def main():
    app = QApplication([])
    window = FirstWindow()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()