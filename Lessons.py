from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextDocument
from PyQt5.QtWidgets import QLabel, QPushButton, QVBoxLayout, QWidget


class LessonsWidget(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)
        
        viewer = QTextDocument()


        viewer = QLabel("<h2>HTML Image</h2> <img src='/home/asimakis/Code/Digital\ Learning/education_application/pic_trulli.jpg' width='500' height='333'>")
        viewer.setAlignment(Qt.AlignCenter)

        layout.addWidget(viewer)


        back = QPushButton('Πίσω')
        layout.addWidget(back)
        back.clicked.connect(self.Back)


    def Back(self):
        """Go back to main page. Use the parent widget (QStacked) to set the previous widget as the current; then delete this one
        
        Args:
            self: Mandatory

        Returns:
            Nothing
        
        """
        parent = self.parentWidget()

        # print(parent.currentIndex())
        old_widget = parent.currentWidget()
        parent.setCurrentIndex(parent.currentIndex() - 1)
        parent.removeWidget(old_widget)
        

        