from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextDocument
from PyQt5.QtWidgets import QLabel, QPushButton, QVBoxLayout, QWidget, QHBoxLayout


class LessonsWidget(QWidget):
    """Widget that displays rich text documents in pages."""

    def __init__(self):
        """Initialize LessonsWidget."""
        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.viewer = QLabel("""<html>
         <body>
         <h2>HTML Image</h2>
         <div>
         <img src='pic_trulli.jpg' alt='Trulli' width='500' height='333'>
         </div>
         </body>
         </html>""")

        self.viewer.setAlignment(Qt.AlignCenter)
        self.htmlText = ["""<html>
         <body>
         <h2>HTML Image</h2>
         <div>
         <img src='pic_trulli.jpg' alt='Trulli' width='500' height='333'>
         </div>
         </body>
         </html>"""]

        self.htmlText.append ("""<html>
         <body>
         <h2>Hello</h2>
         </body>
         </html>""")


        layout.addWidget(self.viewer)

        horizontalbox = QHBoxLayout()
        previous = QPushButton('Προηγούμενο')
        previous.clicked.connect(self.PreviousButton)

        next = QPushButton('Επόμενο')
        next.clicked.connect(self.NextButton)

        horizontalbox.addWidget(previous)
        horizontalbox.addWidget(next)
        layout.addLayout(horizontalbox)
        
        back = QPushButton('Πίσω')
        layout.addWidget(back)
        back.clicked.connect(self.Back)

    def PreviousButton(self) -> None:
        """"""
        for i,text in enumerate(self.htmlText):
            if self.viewer.text() == text and i != 0:
                self.viewer.setText(self.htmlText[i-1])
                break


    def NextButton(self) -> None:
        """"""
        for i,text in enumerate(self.htmlText):
            if self.viewer.text() == text and i != (len(self.htmlText) -1):                
                self.viewer.setText(self.htmlText[i+1])
                break

    def Back(self) -> None:
        """Go back to main page.

        Use the parent widget (QStacked) to set the previous widget as the current; then delete this one
        """
        parent = self.parentWidget()

        # print(parent.currentIndex())
        old_widget = parent.currentWidget()
        parent.setCurrentIndex(parent.currentIndex() - 1)
        parent.removeWidget(old_widget)


