"""Exercises window."""
from PyQt5.QtWidgets import (QVBoxLayout, QPushButton, QWidget)
from Question import FillBlankQuestion, MultipleChoiceQuestion, QuestionWidget


class ExercisesWidget(QWidget):
    """Widget for choosing a set of exercises."""

    def __init__(self):
        """Initialize ExercisesWidget."""
        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)

        exc1 = QPushButton('Ασκήσεις Μαθήματος 1')
        exc2 = QPushButton('Ασκήσεις Μαθήματος 2')
        exc3 = QPushButton('Ασκήσεις Μαθήματος 3')
        back = QPushButton('Πίσω')

        layout.addWidget(exc1)
        layout.addWidget(exc2)
        layout.addWidget(exc3)
        layout.addWidget(back)

        exc1.clicked.connect(self.Exercises1)
        exc2.clicked.connect(self.Exercises2)
        exc3.clicked.connect(self.Exercises3)
        back.clicked.connect(self.Back)

    def Exercises1(self) -> None:
        """First set of exercises."""
        questions = [
            FillBlankQuestion("Μία δεξαμενή πετρελαίου σε μια πολυκατοικία χωράει 2000lt, Ο διαχειριστής σε μια μέτρηση βρήκε ότι ήταν γεμάτη κατά τα 3/4. Πόσα λίτρα πετρέλαιο είχε η δεξαμενή;", " &lt", ["1500"]),
            FillBlankQuestion("Τα 3/5 ενός μπαχαρικού κοστίζουν 27Ευρώ. Πόσο κοστίζουν τα 8/9 του κιλού;", " &Ευρώ", ["45"]),
            FillBlankQuestion("Συμπλήρωσε τα παρακάτω κενά:", """
(α)	Στο κλάσμα Εικόνα οι αριθμοί κ και λ ονομάζονται & και &
(β) Ισχύει ότι: (α) α/1 = & (β) α/α  = & (γ) 0/α = &
(γ) Η φράση 'το μέρος κ/λ ενός μεγέθους Α' εκφράζει τον χωρισμό του μεγέθους Α σε & μεγέθη.
""", ["αριθμητής", "παρονομαστής", "α", "1", "0", "λ"]),
            MultipleChoiceQuestion("Τα κλάσματα 3/4, 2/3, 7/9, 10/9, 18/20, είναι όλα μικρότερα της μονάδας.", ["Σωστό", "Λάθος"], 1),
            MultipleChoiceQuestion("Αν το 1/5 ενός κιλού καρύδια είναι 14 καρύδια, το κιλό περιέχει 70 καρύδια;", ["Σωστό", "Λάθος"], 0),
            FillBlankQuestion("Από μία τούρτα περίσσεψαν 4 κομμάτια τα οποία αποτελούν τα 2/7 της τούρτας. Πόσα ήταν αρχικά όλα τα κομμάτια της τούρτας;", " &κομμάτια", ["14"]),
            FillBlankQuestion("Βρες ποιο μέρος του κιλού είναι τα:", """
(α) 100 γραμμάρια &
(β) 250 γραμμάρια &
(γ) 500 γραμμάρια &
(δ) 600 γραμμάρια &
""", ["1/10", "1/4", "1/2", "3/5"]),
            FillBlankQuestion("Ποιό μέρος:", """
(α) του μήνα &
(β) του εξαμήνου &
(γ) του έτους &
είναι οι 15 μέρες; (Έστω ότι ο μήνας έχει 15 ημέρες και ο χρόνος 365)
""", ["1/2", "1/12", "3/73"])
        ]

        stack = self.parentWidget()
        question = QuestionWidget(questions)
        stack.addWidget(question)
        stack.setCurrentWidget(question)

    def Exercises2(self):
        """TBD"""
        pass

    def Exercises3(self):
        """TBD"""
        pass

    def Back(self) -> None:
        """Go back to main page.

        Use the parent widget (QStacked) to set the previous widget as the current; then delete this one
        """
        parent = self.parentWidget()

        # print(parent.currentIndex())
        old_widget = parent.currentWidget()
        parent.setCurrentIndex(parent.currentIndex() - 1)
        parent.removeWidget(old_widget)
