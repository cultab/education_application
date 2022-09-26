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

    def Exercises2(self) -> None:
        """Second set of exercises."""
        questions = [
            FillBlankQuestion("Μία δεξαμενή πετρελαίου σε μια πολυκατοικία χωράει 2000lt, Ο διαχειριστής σε μια μέτρηση βρήκε ότι ήταν γεμάτη κατά τα 3/4. Πόσα λίτρα πετρέλαιο είχε η δεξαμενή;", " &lt", ["1500"]),
            FillBlankQuestion("Τα 3/5 ενός μπαχαρικού κοστίζουν 27Ευρώ. Πόσο κοστίζουν τα 8/9 του κιλού;", " &Ευρώ", ["45"]),
            FillBlankQuestion("Συμπλήρωσε τα παρακάτω κενά:", """
(α)	Στο κλάσμα κ/λ οι αριθμοί κ και λ ονομάζονται & και &
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
""", ["1/2", "1/12", "3/73"]),
            FillBlankQuestion("Ένα κατάστημα κάνει έκπτωση στα είδη του ίση με τα 2/5 της αρχικής τιμής τους. Ένα φόρεμα κόστιζε 90€ πριν την έκπτωση. Υπολόγισε πόσα ευρώ έκπτωση έγινε στο φόρεμα και πόσο θα πληρώσουμε για να το αγοράσουμε.", " &€", ["36"]),
            FillBlankQuestion("Σε μία τάξη τα 3/8 των μαθητών μαθαίνουν αγγλικά. Να βρεις πόσους μαθητές έχει η τάξη, αν γνωρίζεις ότι αυτοί που μαθαίνουν αγγλικά είναι 12 μαθητές.", "Η τάξη έχει συνολικά & μαθητές.", ["32"]),
            FillBlankQuestion("Σε ένα ορθογώνιο παραλληλόγραμμο η μια πλευρά του είναι 33 εκατοστά και η άλλη τα 3/11 της πρώτης.", "H περίμετρος του ορθογωνίου είναι & εκατοστά.", ["84"]),
            FillBlankQuestion("Ένα ευθύγραμμο τμήμα ΑΒ έχει μήκος 5 εκατοστά. Να βρείς το μήκος:", """
(α) ενός ευθύγραμμου τμήματος ΓΔ με μήκος τα 8/10 του ΑΒ: &cm
(β) ενός ευθύγραμμου τμήματος ΕΖ με μήκος τα 6/5 του ΑΒ &cm
""", ["4", "6"])
        ]

        stack = self.parentWidget()
        question = QuestionWidget(questions)
        stack.addWidget(question)
        stack.setCurrentWidget(question)

    def Exercises1(self):
        """First set of exercises."""
        questions = [
            FillBlankQuestion("Ποιοι είναι οι τρεις προηγούμενοι αριθμοί του 289 και ποιοι οι δύο επόμενοι;", " & & & 289 & &", ["286", "287", "288", "290", "291"]),
            FillBlankQuestion("Τοποθέτησε σε αύξουσα σειρά τους αριθμούς: 3.515, 4.800, 3.620, 3.508, 4.801.", " & & & & & & & & &", ["3508", "<", "3515", "<", "3620", "<", "4800", "<", "4801"]),
            FillBlankQuestion("Τοποθέτησε το κατάλληλο σύμβολο: <, =, >, στο κενό μεταξύ των ακόλουθων αριθμών:", """
            (α) 45 & 45
            (β) 38 & 36
            (γ) 456 & 465
            (δ) 8.765 & 8.970
            (ε) 90.876 & 86.945
            (στ) 345 & 5.690""", ["=", ">", "<", "<", ">", "<"]),
            MultipleChoiceQuestion("""Επέλεξε Σωστό ή Λάθος:
            Στον αριθμό 5780901 το μηδέν δηλώνει απουσία δεκάδων και χιλιάδων""", ["Σωστό", "Λάθος"], 0),
            MultipleChoiceQuestion("""Επέλεξε Σωστό ή Λάθος:
            Δέκα χιλιάδες είναι μία δεκάδα χιλιάδα""", ["Σωστό", "Λάθος"], 0),
            MultipleChoiceQuestion("""Επέλεξε Σωστό ή Λάθος:
            Σε μια πενταήμερη εκδρομή θα γίνουν πέντε διανυχτερεύσεις""", ["Σωστό", "Λάθος"], 1),
            MultipleChoiceQuestion("""Επέλεξε Σωστό ή Λάθος:
            Από τον αριθμό 32 ως τον αριθμό 122 υπάρχουν (χωρίς να μετράμε τον 122) 91 αριθμοί""", ["Σωστό", "Λάθος"], 1),
            MultipleChoiceQuestion("""Επέλεξε Σωστό ή Λάθος:
            Σε οκτώ ημέρες από σήμερα, που είναι Πέμπτη,θα είναι Παρασκευή""", ["Σωστό", "Λάθος"], 0),
            MultipleChoiceQuestion("""Επέλεξε Σωστό ή Λάθος:
            Από την 12η σελίδα του βιβλίου μέχρι και την 35η (χωρίς να μετράμε την 35η) είναι 24 σελίδες""", ["Σωστό", "Λάθος"], 1),
            MultipleChoiceQuestion("""Επέλεξε Σωστό ή Λάθος:
            Δεν υπάρχει φυσικός αριθμός μεταξύ των αριθμών 2 και 3""", ["Σωστό", "Λάθος"], 0),
            FillBlankQuestion("Στρογγυλοποίησε στην πλησιέστερη εκατοντάδα τους αριθμούς: ", """
            (α) 345 &
            (β) 761 &
            (γ) 659 &
            (δ) 2.567 &
            (ε) 9.532 &
            (στ) 123.564 &
            (ζ) 34.564 &
            (η) 31.549 &
            (θ) 8.765 &""", ["300", "800", "700", "2600", "9500", "123600", "34600", "31600", "8800"]),
            FillBlankQuestion("Στρογγυλοποίησε τον αριθμό 7.568.349 στις πλησιέστερες:", """
            (α) δεκάδες &
            (β) εκατοντάδες &
            (γ) χιλιάδες &
            (δ) δεκάδες χιλιάδες &
            (ε) εκατοντάδες χιλιάδες &""", ["7568350", "7568300", "7568000", "7570000", "7600000"]),


        ]

        stack = self.parentWidget()
        question = QuestionWidget(questions)
        stack.addWidget(question)
        stack.setCurrentWidget(question)

    def Exercises3(self):
        """Third set of exercises."""
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
