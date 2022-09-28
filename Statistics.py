"""Statistics window."""

import pandas as pd

from os import getcwd

from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget, QLabel, QFormLayout, QLineEdit, QPushButton


class StatisticsWidget(QWidget):

    def __init__(self):
        super(StatisticsWidget, self).__init__()

        layout = QVBoxLayout()
        title = QLabel("Αποτελέσματα:")
        title.setStyleSheet("QLabel {font-size: 18pt;}")

        form = QFormLayout()

        self.naturals = QLabel("Φυσικοί:")
        self.fractions = QLabel("Κλάσματα:")
        self.decimals = QLabel("Δεκαδικοί:")

        self.marks_naturals = QLineEdit("")
        self.marks_fractions = QLineEdit("")
        self.marks_decimals = QLineEdit("")

        self.marks_naturals.setEnabled(False)
        self.marks_fractions.setEnabled(False)
        self.marks_decimals.setEnabled(False)

        form.addRow(self.naturals, self.marks_naturals)
        form.addRow(self.fractions, self.marks_fractions)
        form.addRow(self.decimals, self.marks_decimals)

        buttons = QHBoxLayout()

        self.avg = QPushButton("Μέσος Όρος")
        self.last = QPushButton("Πιό πρόσφατοι")
        self.best = QPushButton("Ρεκόρ")

        self.avg.clicked.connect(self.showAverages)
        self.last.clicked.connect(self.showLatest)
        self.best.clicked.connect(self.showBest)

        buttons.addWidget(self.avg)
        buttons.addWidget(self.last)
        buttons.addWidget(self.best)

        layout.addWidget(title)
        layout.addLayout(form)
        layout.addStretch()
        layout.addLayout(buttons)
        self.setLayout(layout)

        self.load_data()

        # show average by default
        self.showAverages()

    def showAverages(self):
        """Show average results."""
        self.avg.setEnabled(False)
        self.last.setEnabled(True)
        self.best.setEnabled(True)

    def showLatest(self):
        """Show latest results."""
        self.avg.setEnabled(True)
        self.last.setEnabled(False)
        self.best.setEnabled(True)

    def showBest(self):
        """Show best results."""
        self.avg.setEnabled(True)
        self.last.setEnabled(True)
        self.best.setEnabled(False)

    def load_data(self):
        """Load data from results.csv."""
        results_path = getcwd() + "/results.csv"

        df = pd.read_csv(results_path)
        print(df.head())



