from textwrap import indent
from PyQt5.QtWidgets import QLabel, QPushButton, QVBoxLayout, QWidget, QHBoxLayout
from PyQt5.QtCore import Qt

class ChaptersWidget(QWidget):

    def __init__(self, ChapNumber):
        """Initialize LessonsWidget."""
        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.LoadChapter(ChapNumber)

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
        
        self.viewer = QLabel(self.htmlText[0])
        self.index = 0

        self.viewer.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.viewer)

        horizontalbox = QHBoxLayout()
        self.previous = QPushButton('Προηγούμενο')
        self.previous.clicked.connect(self.PreviousButton)
        self.previous.setEnabled(False)

        self.next = QPushButton('Επόμενο')
        self.next.clicked.connect(self.NextButton)

        horizontalbox.addWidget(self.previous)
        horizontalbox.addWidget(self.next)
        layout.addLayout(horizontalbox)
        
        back = QPushButton('Πίσω')
        layout.addWidget(back)
        back.clicked.connect(self.Back)

    def LoadChapter(self,chapNumber) -> None:

        match chapNumber:
            case 1:
                #Load Chapter 1 in self.htmlText
                """"""
            case 2:
                #Load Chapter 2 in self.htmlText
                """"""
            case 3:
                #Load Chapter 3 in self.htmlText
                """"""

    def PreviousButton(self) -> None:
        """"""
        if self.index != 0:
            self.viewer.setText(self.htmlText[self.index-1])
            self.index -= 1
            self.next.setEnabled(True)
        
        if self.index == 0:
            self.previous.setEnabled(False)


    def NextButton(self) -> None:
        """"""
        if self.index != (len(self.htmlText) -1):                
            self.viewer.setText(self.htmlText[self.index+1])
            self.index += 1
            self.previous.setEnabled(True)

        if self.index == (len(self.htmlText) -1):
            self.next.setEnabled(False)

    
    def Back(self) -> None:
        """Go back to main page.

        Use the parent widget (QStacked) to set the previous widget as the current; then delete this one
        """
        parent = self.parentWidget()

        # print(parent.currentIndex())
        old_widget = parent.currentWidget()
        parent.setCurrentIndex(parent.currentIndex() - 1)
        parent.removeWidget(old_widget)
        

