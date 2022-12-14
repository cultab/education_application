"""Chapters view."""

import os
import re

from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QHBoxLayout, QPushButton, QVBoxLayout, QWidget


class ChaptersWidget(QWidget):

    def __init__(self, ChapNumber):
        """Initialize LessonsWidget."""
        super().__init__()

        self.files = list()
        self.viewer = QWebEngineView()
        self.index = 0

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.LoadChapter(ChapNumber)

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

    def LoadChapter(self, chapNumber) -> None:
        """Load chapter by chapNumber."""
        path = os.getcwd() + "/resources/lessons/"
        dir = os.listdir(path)
        dir.sort()
        for file in dir:
            regex = "lesson" + str(chapNumber) + r".*"
            if re.match(regex, file):
                self.files.append(QUrl.fromLocalFile(path + file))

        self.viewer.setUrl(self.files[0])

    def PreviousButton(self) -> None:
        """."""
        if self.index != 0:
            self.index -= 1
            self.viewer.setUrl(self.files[self.index])
            self.next.setEnabled(True)

        if self.index == 0:
            self.previous.setEnabled(False)

    def NextButton(self) -> None:
        """."""
        if self.index < len(self.files) - 1:
            self.index += 1
            self.viewer.setUrl(self.files[self.index])
            self.previous.setEnabled(True)

        if self.index == (len(self.files) - 1):
            self.next.setEnabled(False)

    def Back(self) -> None:
        """Go back to main page.

        Use the parent widget (QStacked) to set the previous widget as the current; then delete this one
        """
        parent = self.parentWidget()

        old_widget = parent.currentWidget()
        parent.setCurrentIndex(parent.currentIndex() - 1)
        parent.removeWidget(old_widget)
