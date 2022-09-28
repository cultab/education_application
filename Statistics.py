"""Statistics window."""

import pandas as pd

from os import getcwd

from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget, QLabel, QFormLayout, QLineEdit, QPushButton


class StatisticsWidget(QWidget):

    def __init__(self):
        super(StatisticsWidget, self).__init__()
        self.df: pd.DataFrame = None

        layout = QVBoxLayout()
        title = QLabel("Αποτελέσματα:")
        title.setStyleSheet("QLabel {font-size: 18pt;}")

        form = QFormLayout()

        naturals = QLabel("Φυσικοί:")
        fractions = QLabel("Κλάσματα:")
        decimals = QLabel("Δεκαδικοί:")
        final = QLabel("Επαναληπτικό Διαγώνισμα:")

        self.marks_naturals = QLineEdit("")
        self.marks_fractions = QLineEdit("")
        self.marks_decimals = QLineEdit("")
        self.marks_final = QLineEdit("")

        self.marks_naturals.setReadOnly(True)
        self.marks_fractions.setReadOnly(True)
        self.marks_decimals.setReadOnly(True)
        self.marks_final.setReadOnly(True)

        form.addRow(naturals, self.marks_naturals)
        form.addRow(fractions, self.marks_fractions)
        form.addRow(decimals, self.marks_decimals)
        form.addRow(final, self.marks_final)

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

        self.df = self.load_data()

        # show average by default
        self.showAverages()

    def setLabels(self, marks):
        """Set the labels to the correct mark."""
        marks = [f"{x:.2f}".split('.')[1] for x in marks]

        self.marks_naturals.setText(marks[0] + "/100")
        self.marks_decimals.setText(marks[1] + "/100")
        self.marks_fractions.setText(marks[2] + "/100")
        self.marks_final.setText(marks[3] + "/100")


    def showAverages(self):
        """Show average results."""
        self.avg.setEnabled(False)
        self.last.setEnabled(True)
        self.best.setEnabled(True)

        grouped = self.df.groupby("Question Set").mean().reset_index()

        marks = [
            grouped.loc[grouped['Question Set'] == "naturals"].values[0][1],
            grouped.loc[grouped['Question Set'] == "decimals"].values[0][1],
            grouped.loc[grouped['Question Set'] == "fractions"].values[0][1],
            grouped.loc[grouped['Question Set'] == "final"].values[0][1]
        ]

        self.setLabels(marks)

    def showLatest(self):
        """Show latest results."""
        self.avg.setEnabled(True)
        self.last.setEnabled(False)
        self.best.setEnabled(True)

        df = self.df

        marks = [
            df.loc[df['Question Set'] == "naturals"].values[-1][1],
            df.loc[df['Question Set'] == "decimals"].values[-1][1],
            df.loc[df['Question Set'] == "fractions"].values[-1][1],
            df.loc[df['Question Set'] == "final"].values[-1][1]
        ]

        self.setLabels(marks)

    def showBest(self):
        """Show best results."""
        self.avg.setEnabled(True)
        self.last.setEnabled(True)
        self.best.setEnabled(False)

        grouped = self.df.groupby("Question Set").max().reset_index()

        marks = [
            grouped.loc[grouped['Question Set'] == "naturals"].values[0][1],
            grouped.loc[grouped['Question Set'] == "decimals"].values[0][1],
            grouped.loc[grouped['Question Set'] == "fractions"].values[0][1],
            grouped.loc[grouped['Question Set'] == "final"].values[0][1],
        ]

        self.setLabels(marks)

    def load_data(self) -> pd.DataFrame:
        """Load data from results.csv."""
        results_path = getcwd() + "/results.csv"
        df = pd.read_csv(results_path)
        return df
