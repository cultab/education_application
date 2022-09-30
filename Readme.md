-   [1 Εισαγωγή](#εισαγωγή)
-   [2 Δομή του Project](#δομή-του-project)
-   [3 Δομή της εφαρμογής](#δομή-της-εφαρμογής)
    -   [3.1 class
        FirstWindow(QMainWindow)](#class-firstwindowqmainwindow)
        -   [3.1.1 init() -\> None](#init---none)
        -   [3.1.2 openLessons() -\> None](#openlessons---none)
        -   [3.1.3 openExercises() -\> None](#openexercises---none)
        -   [3.1.4 openStatistics() -\> None](#openstatistics---none)
        -   [3.1.5 exit() -\> None](#exit---none)
        -   [3.1.6 help() -\> None](#help---none)
        -   [3.1.7 about() -\> None](#about---none)
    -   [3.2 class FlowLayout(QLayout)](#class-flowlayoutqlayout)
        -   [3.2.1 init(margin=-1, hSpacing=-1, vSpacing=-1, \*args,
            \*\*kwargs)](#initmargin-1-hspacing-1-vspacing-1-args-kwargs)
        -   [3.2.2 addItem(item: QLayoutItem) -\>
            None](#additemitem-qlayoutitem---none)
        -   [3.2.3 newRow() -\> None](#newrow---none)
    -   [3.3 class Question(Protocol)](#class-questionprotocol)
        -   [3.3.1 isCorrect() -\> bool](#iscorrect---bool)
    -   [3.4 class FillBlankQuestion()](#class-fillblankquestion)
        -   [3.4.1 init(prompt: str, text: str, correct: list\[str\])
            -\> None](#initprompt-str-text-str-correct-liststr---none)
        -   [3.4.2 isCorrect(index: int) -\>
            bool](#iscorrectindex-int---bool)
    -   [3.5 class
        FillBlankQuestionWidget(QWidget)](#class-fillblankquestionwidgetqwidget)
        -   [3.5.1 init(question: FillBlankQuestion, \*args,
            \*\*kwargs)](#initquestion-fillblankquestion-args-kwargs)
        -   [3.5.2 getQuestion() -\>
            FillBlankQuestion](#getquestion---fillblankquestion)
    -   [3.6 class
        MultipleChoiceQuestion()](#class-multiplechoicequestion)
        -   [3.6.1 init(self, prompt: str, choices: list\[str\],
            correct:
            int):t](#initself-prompt-str-choices-liststr-correct-intt)
    -   [3.7 class
        MultipleChoiceQuestion(QWidget)](#class-multiplechoicequestionqwidget)
        -   [3.7.1 init(question: MultipleChoiceQuestion, \*args,
            \*\*kwargs)](#initquestion-multiplechoicequestion-args-kwargs)
        -   [3.7.2 getQuestion() -\>
            MultipleChoiceQuestion](#getquestion---multiplechoicequestion)
    -   [3.8 class
        QuestionWidget(QWidget)](#class-questionwidgetqwidget)
        -   [3.8.1 init(questions: list\[Question\], question_set:
            str)](#initquestions-listquestion-question_set-str)
        -   [3.8.2 goto_next() -\> None](#goto_next---none)
        -   [3.8.3 goto_prev() -\> None](#goto_prev---none)
        -   [3.8.4 submit() -\> None](#submit---none)
    -   [3.9 class
        OverviewListWidget(QListWidget)](#class-overviewlistwidgetqlistwidget)
        -   [3.9.1 init(questions: list\[Question\], question_set:
            str)](#initquestions-listquestion-question_set-str-1)
        -   [3.9.2 Back() -\> None](#back---none)
    -   [3.10 class
        OverviewQuestionWidget(QWidget)](#class-overviewquestionwidgetqwidget)
        -   [3.10.1 init(question: Question)](#initquestion-question)
    -   [3.11 class
        ExercisesWidget(QWidget)](#class-exerciseswidgetqwidget)
        -   [3.11.1 Exercises1-3 -\> None](#exercises1-3---none)
        -   [3.11.2 Back() -\> None](#back---none-1)
    -   [3.12 class LessonsWidget(QWidget)](#class-lessonswidgetqwidget)
        -   [3.12.1 LoadLessons(lessonNumber: int) -\>
            None](#loadlessonslessonnumber-int---none)
        -   [3.12.2 Back() -\> None](#back---none-2)
    -   [3.13 class
        ChaptersWidget(QWidget)](#class-chapterswidgetqwidget)
        -   [3.13.1 init(ChapNumber: int)](#initchapnumber-int)
        -   [3.13.2 LoadChapter(ChapNumber: int) -\>
            None](#loadchapterchapnumber-int---none)
        -   [3.13.3 PreviousButton() και
            NextButton()](#previousbutton-και-nextbutton)
        -   [3.13.4 Back() -\> None](#back---none-3)
    -   [3.14 class Statistics(QWidget)](#class-statisticsqwidget)
        -   [3.14.1 setLabels(marks:
            list\[float\])](#setlabelsmarks-listfloat)
        -   [3.14.2 showAverages() -\> None](#showaverages---none)
        -   [3.14.3 showLatest() -\> None](#showlatest---none)
        -   [3.14.4 showBest() -\> None](#showbest---none)
-   [4 Διαδικασία Επέκτασης](#διαδικασία-επέκτασης)
    -   [4.1 Προαπαιτούμενα και
        Προϋποθέσεις](#προαπαιτούμενα-και-προϋποθέσεις)
        -   [4.1.1 Γνώσεις](#γνώσεις)
        -   [4.1.2 Λογισμικό](#λογισμικό)
        -   [4.1.3 Άδεια](#άδεια)
    -   [4.2 Επιπλέον Υλικό Θεωρίας](#επιπλέον-υλικό-θεωρίας)
    -   [4.3 Επιπλέον Ασκήσεις](#επιπλέον-ασκήσεις)
    -   [4.4 Επιπλέον Λειτουργικότητα](#επιπλέον-λειτουργικότητα)

<!-- Cache of copy-paste'ables {{{-->
<!-- section renaming# {{{ -->
<!-- \renewcommand{\thesubsection}{Δραστηριότητα\space\arabic{subsection}:} -->
<!-- \renewcommand{\thesubsubsection}{\arabic{section}.\arabic{subsection}.\arabic{subsubsection}} -->
<!-- \addtolength{\cftsubsecnumwidth}{6em}# }}} -->
<!-- latex figure with subfigures# {{{ -->
<!-- \begin{figure}[H] -->
<!-- \centering -->
<!--     \begin{subfigure}[b]{\textwidth} -->
<!--     \centering -->
<!--         \includegraphics[width=\textwidth]{} -->
<!--         \caption{} -->
<!--     \end{subfigure} -->
<!--     \begin{subfigure}[b]{\textwidth} -->
<!--     \centering -->
<!--         \includegraphics[width=\textwidth]{} -->
<!--         \caption{} -->
<!--     \end{subfigure} -->
<!--     \caption{} -->
<!--     \label{} -->
<!-- \end{figure} -->
<!-- }}} -->
<!-- python code then output# {{{ -->
<!-- ```{r setup} -->
<!-- CACHE <- FALSE -->
<!-- ``` -->
<!-- ```{python, code=readLines("file"), results='asis', cache=USE_CACHE, cache.extra = tools::md5sum('./file')} -->
<!-- ``` -->
<!-- ```{python, code=readLines("file"), eval=FALSE} -->
<!-- ``` -->
<!-- ## Αποτελέσματα -->
<!---->
<!-- ```{python, code=readLines("file"), echo=FALSE, results='asis', cache=USE_CACHE, cache.extra = tools::md5sum('./file')} -->
<!-- ``` -->
<!-- }}} -->
<!-- }}} -->
<!-- \renewcommand*{\lstlistlistingname}{Κατάλογος Κώδικα} -->
<!-- \renewcommand*{\lstlistingname}{Κώδικας} -->
<!-- \listoffigures -->
<!-- \listoftables -->
<!-- \lstlistoflistings -->
# 1 Εισαγωγή

Σε αυτό το εγχειρίδιο θα αναλυθεί συνοπτικά η δομή της εφαρμογής και του
project όπως και η διαδικασία επέκτασης της εφαρμογής. Η δομή της
εφαρμογής θα αναλυθεί μέσω από τις αλληλεπιδράσεις των διαφόρων
συναρτήσεων και αντικειμένων της. Η δομή του project θα αναλυθεί μέσω
των εργαλείων που χρειάζονται για την ανάπτυξη και επέκταση της
εφαρμογής. Τέλος θα δοθεί μια καθαρή αρχή για όποιον προτίθεται να
επεκτάσει την εφαρμογή.

Το παρόν εγχειρίδιο έχει γραφτεί σε Rmarkdown (Allaire κ.ά. 2021) (Xie,
Allaire, και Grolemund 2018) (Xie, Dervieux, και Riederer 2020).

# 2 Δομή του Project

Η διαχείριση πηγαίου κώδικα του πρότζεκτ γίνεται με git (Chacon και
Straub 2014). Η διαχείριση των dependencies του πρότζεκτ γίνεται με
poetry (Poetry core contributors 2022)

Η βασική δομή των αρχείων του πρότζεκτ είναι η παρακάτω.

    education_application
    ├── app.py
    ├── resources
    │  ├── lessons
    │  │  ├── img
    │  │  │  └── <εικόνες για html αρχεία μαθημάτων>
    │  │  ├── style.css
    │  │  └── <αρχεία html μαθημάτων>
    │  └── <εικόνες για το UI>
    ├── style.css
    ├── results.csv
    ├── Chapters.py
    ├── Exercises.py
    ├── FlowLayout.py
    ├── Lessons.py
    ├── MenuButton.py
    ├── Question.py
    ├── Statistics.py
    ├── WrapLabel.py
    ├── poetry.lock
    ├── pyproject.toml
    ├── LICENSE
    └── todo.norg

Στο root του φακέλου βρίσκονται τα αρχεία πηγαίου κώδικα python, το css
του UI, τα αρχεία του poetry και ο φάκελος resources. Ο φάκελος
resources περιέχει όλα τα αρχεία που φορτώνονται από το UI όπως και τον
φάκελο lessons. O φάκελος lessons περιέχει όλο το υλικό των μαθημάτων σε
HTML μορφή και επιπλέον εικόνες στο φάκελο img.

# 3 Δομή της εφαρμογής

Σε αυτή την ενότητα θα αναλυθούν οι συναρτήσεις και τα αντικείμενα της
εφαρμογής.

## 3.1 class FirstWindow(QMainWindow)

Το αρχικό παράθυρο της εφαρμογής. Παρέχει 4 MenuButtons, για Μαθήματα,
Ασκήσεις, Στατιστικά και έξοδο. Επίσης παρέχει ένα MenuBar με ένα κουμπί
Help (ανοίγει το εγχειρίδιο χρήστη) και ένα About (εμφανίζει έκδοση και
πληροφορίες επικοινωνίας).

### 3.1.1 init() -\> None

Κατασκευαστής, δεν παίρνει ορίσματα.

### 3.1.2 openLessons() -\> None

Event handler για κλικ πάνω στο κουμπί Μαθημάτων. Αλλάζει το
centralWidget του FirstWindow σε ένα **LessonsWidget**.

### 3.1.3 openExercises() -\> None

Event handler για κλικ πάνω στο κουμπί Ασκήσεων. Αλλάζει το
centralWidget του FirstWindow σε ένα **ExercisesWidget**.

### 3.1.4 openStatistics() -\> None

Event handler για κλικ πάνω στο κουμπί Στατιστικών. Αλλάζει το
centralWidget του FirstWindow σε ένα **StatisticsWidget**.

### 3.1.5 exit() -\> None

Event handler για κλικ πάνω στο κουμπί Έξοδος. Ανοίγει ένα διάλογο
ναι/όχι και σε περίπτωση ναι, τερματίζει την εφαρμογή.

### 3.1.6 help() -\> None

Event handler για κλικ πάνω στο κουμπί Help. Ανοίγει το εγχειρίδιο
χρήστη.

### 3.1.7 about() -\> None

Event handler για κλικ πάνω στο κουμπί About. Εμφανίζει την έκδοση της
εφαρμογής και πληροφορίες επικοινωνίας.

## 3.2 class FlowLayout(QLayout)

Παρέχει ένα **QLayout** το οποίο εμφανίζει τα widget του σε γραμμές
ανάλογα με τον διαθέσιμο χώρο. Σε περίπτωση που ένα widget δεν χωράει
στην τελευταία γραμμή, προστίθεται στην επόμενη. Η κώδικας είναι
μετάφραση του [C++
παραδείγματος](https://doc.qt.io/qt-6/qtwidgets-layouts-flowlayout-example.html)
που παρέχεται από το documentation του Qt6 σε Python με μια επιπλέον
λειτουργία.

### 3.2.1 init(margin=-1, hSpacing=-1, vSpacing=-1, \*args, \*\*kwargs)

Κατασκευαστής.

-   margin: *int* **default = -1** Το εσωτερικό κενό του χώρου του
    Layout και των widget του.
-   hSpacing: *int* **default = -1** Το οριζόντιο κενό μεταξύ των widget
    του Layout.
-   vSpacing: *int* **default = -1** Το κάθετο κενό μεταξύ των widget
    του Layout.

### 3.2.2 addItem(item: QLayoutItem) -\> None

Προσθέτει ένα item στο Layout.

-   item: *QLayoutItem* Το item που θα προστεθεί.

### 3.2.3 newRow() -\> None

Προσθέτει ένα **QSpacerItem** μηδενικού μεγέθους. Δεν υπάρχει στην C++
έκδοση του κώδικα. Αναγκάζει τα widget που θα προστεθούν μετά από την
κλήση της, να πάνε στην επόμενη σειρά, ανεξαρτήτου εάν χωρούσαν στην
τελευταία ή όχι.

## 3.3 class Question(Protocol)

Ορίζει ένα **Protocol** (implicit interface) για το τι πρέπει να
περιέχουν οι κλάσεις που θεωρούνται **Question**.

-   prompt: *str* Το κείμενο της ερώτησης

-   correct: *int \| list\[str\]* Η σωστή απάντηση/απαντήσεις της
    ερώτησης

-   answer: *str \| list\[str\]* Η απάντηση/απαντήσεις που θα έχει δώσει
    ο χρήστης

### 3.3.1 isCorrect() -\> bool

Συνάρτηση που θα πρέπει να επιστρέφει True όταν οι απαντήσεις του χρήστη
είναι σωστές, False διαφορετικά.

## 3.4 class FillBlankQuestion()

Υλοποίηση του **Question(Protocol)**. Ορίζει μια ερώτηση τύπου
συμπλήρωσε-τα-κενά.

-   answer: *list\[str\]* Οι απαντήσεις που θα έχει δώσει ο χρήστης

### 3.4.1 init(prompt: str, text: str, correct: list\[str\]) -\> None

-   prompt: *str* Το κείμενο της ερώτησης

-   correct: *list\[str\]* Οι σωστές απαντήσεις της ερώτησης

-   text: *str* Το κείμενο της ερώτησης που περιέχει τα κενά που ο
    χρήστης πρέπει να γεμίσει. Ο χαρακτήρας ᾽&᾽ μέσα στο κείμενο ορίζει
    ένα κενό προς γέμισμα.

### 3.4.2 isCorrect(index: int) -\> bool

Επιστέφει True εάν η ερώτηση που δεικτοδοτήται από το index έχει
απαντηθεί σωστά από τον χρήστη.

## 3.5 class FillBlankQuestionWidget(QWidget)

-   answer: \*list\[QLineEdit\] Λίστα των πεδίων που ο χρήστης θα πρέπει
    γεμίσει.

### 3.5.1 init(question: FillBlankQuestion, \*args, \*\*kwargs)

-   question: *FillBlankQuestion* Η ερώτηση του widget.

Κατασκευαστής, γεμίζει το **answer** με τα QLineEdit.

### 3.5.2 getQuestion() -\> FillBlankQuestion

Επιστρέφει την ερώτηση του widget με τις απαντήσεις του χρήστη.

## 3.6 class MultipleChoiceQuestion()

Υλοποίηση του **Question(Protocol)**. Ορίζει μια ερώτηση τύπου
επέλεξε-το-σωστό.

-   answer: *str* Η απάντηση που θα δώσει ο χρήστης

### 3.6.1 init(self, prompt: str, choices: list\[str\], correct: int):t

-   prompt: *str* Η ερώτηση.
-   choices: *list\[str\]* Οι επιλογές που δίνονται στον χρήστη
-   correct: *int* Ο δείκτης της σωστής επιλογής στη λίστα των επιλογών

## 3.7 class MultipleChoiceQuestion(QWidget)

### 3.7.1 init(question: MultipleChoiceQuestion, \*args, \*\*kwargs)

-   question: *MultipleChoiceQuestion* Η ερώτηση του widget.

### 3.7.2 getQuestion() -\> MultipleChoiceQuestion

Επιστρέφει την ερώτηση του widget με τις απαντήσεις του χρήστη.

## 3.8 class QuestionWidget(QWidget)

Widget που εμφανίζει ερωτήσεις και δύο κουμπιά για να προχωράει ο
χρήστης στην επόμενη και να πάει πίσω.

### 3.8.1 init(questions: list\[Question\], question_set: str)

-   questions: *list\[Question\]* Η λίστα των ερωτήσεων που θα
    παρουσιαστούν στον χρήστη
-   question_set: *str* Αναγνωριστικό για το σύνολο των ερωτήσεων,
    χρησιμοποιείται για τα στατιστικά.

### 3.8.2 goto_next() -\> None

Event handler για το κουμπί εμφάνισης επόμενης ερώτησης. Στην περίπτωση
που ο χρήστης βρίσκεται στην προτελευταία ερώτηση η συνάρτηση επίσης
αλλάζει τον Event handler του κουμπιού ώστε να χρησιμοποιεί την
συνάρτηση **submit()**.

### 3.8.3 goto_prev() -\> None

Event handler για το κουμπί εμφάνισης προηγούμενης ερώτησης.

### 3.8.4 submit() -\> None

Event handler για το κουμπί υποβολής. Μαζεύει τις ερωτήσεις με τις
απαντήσεις του χρήστη και δημιουργεί ένα **OverviewListWidget** με
αυτές.

## 3.9 class OverviewListWidget(QListWidget)

Widget που εμφανίζει στον χρήστη τα αποτελέσματα της άσκησής του.

### 3.9.1 init(questions: list\[Question\], question_set: str)

-   questions: *list\[Question\]* Λίστα ερωτήσεων που έχουν απαντηθεί
    (δηλαδή που έχουν προκύψει από μια συνάρτηση **getQuestion()**)

-   question_set: *str* Αναγνωριστικό για το σύνολο των ερωτήσεων,
    χρησιμοποιείται για τα στατιστικά.

Για κάθε ερώτηση στη λίστα questions φτιάχνει ένα
**OverviewQuestionWidget** και το εμφανίζει. Μετά ανακτεί της μονάδες
που κέρδισε ο χρήστης από κάθε **OverviewQuestionWidget**, εμφανίζει ένα
μήνυμα επιτυχίας/αποτυχίας και γράφει τα αποτελέσματα στο αρχείο
`results.csv` με το αναγνωριστικό **question_set**.

### 3.9.2 Back() -\> None

Event handler για το κουμπί επιστροφής στην σελίδα επιλογής ασκήσεων.

## 3.10 class OverviewQuestionWidget(QWidget)

Widget που εμφανίζει αν μια ερώτηση είναι σωστά απαντημένη όπως και την
σωστή απάντηση σε περίπτωση λάθος απάντησης. Υποστηρίζει
MultipleChoiceQuestion και FillBlankQuestion.

### 3.10.1 init(question: Question)

Κατασκευαστής.

-   question: *Question* Η ερώτηση του widget.

## 3.11 class ExercisesWidget(QWidget)

Widget που εμφανίζει 3 **MenuButton** για 3 διαφορετικά σετ ασκήσεων και
ένα **MenuButton** που επιστρέφει στην αρχική σελίδα.

### 3.11.1 Exercises[1-3]() -\> None

Οι συναρτήσεις Exercises\[1-3\] είναι event handlers των **MenuButton**
και φτιάχνουν ένα σετ ασκήσεων που χρησιμοποιούν για να φτιάξουν ένα
**QuestionWidget**.

### 3.11.2 Back() -\> None

Event handler για το κουμπί επιστροφής στην αρχική σελίδα.

## 3.12 class LessonsWidget(QWidget)

Widget που εμφανίζει 3 **MenuButton** για 3 διαφορετικά σετ θεωρίας και
ένα **MenuButton** που επιστρέφει στην αρχική σελίδα.

Τα κουμπιά έχουν event handler που καλούν την συνάρτηση *LoadLessons()*
με το σωστό αναγνωριστικό κεφάλαιο που τους αντιστοιχεί όπως φαίνεται
παρακάτω.

``` py
lesson1.clicked.connect(lambda _: self.LoadLessons(1))
lesson2.clicked.connect(lambda _: self.LoadLessons(2))
lesson3.clicked.connect(lambda _: self.LoadLessons(3))
```

### 3.12.1 LoadLessons(lessonNumber: int) -\> None

-   lessonNumber: *int* Το αναγνωριστικό του κεφαλαίου που θα ανοίξει.

Η συνάρτηση δημιουργεί ένα **ChaptersWidget()** χρησιμοποιώντας το
**lessonNumber** και το εμφανίζει.

### 3.12.2 Back() -\> None

Event handler για το κουμπί επιστροφής στην αρχική σελίδα.

## 3.13 class ChaptersWidget(QWidget)

Widget το οποίο εμφανίζει ένα webview στο οποίο φορτώνουμε τα αρχεία
θεωρίας των μαθημάτων. Παρέχει 2 κουμπιά ώστε ο χρήστης να επιλέγει την
σελίδα που θέλει να διαβάσει και ένα κουμπί που τον επιστρέφει την
σελίδα επιλογής θεωρίας.

### 3.13.1 init(ChapNumber: int)

-   ChapNumber: *int* Αριθμός κεφάλαιου.

### 3.13.2 LoadChapter(ChapNumber: int) -\> None

-   chapNumber: *int* Αριθμός κεφάλαιου.

Φορτώνει τα μονοπάτια των αρχείων θεωρίας που βρίσκονται στον φάκελο
`/resources/lessons/` και ακολουθούν την κανονική έκφραση
“lesson<chapNumber>.\*“[^1].

### 3.13.3 PreviousButton() και NextButton()

Event handlers για τα κουμπιά εμφάνισης επόμενης και προηγούμενης
σελίδας. Αλλάζουν το αρχείο που εμφανίζεται στο webview.

### 3.13.4 Back() -\> None

Event handler για το κουμπί επιστροφής στην σελίδα επιλογής κεφαλαίου.

## 3.14 class Statistics(QWidget)

Widget που εμφανίζει στατιστικά για τα διαγωνίσματα του χρήστη.

### 3.14.1 setLabels(marks: list\[float\])

-   marks: *list\[float\]* Λίστα βαθμών

Ενημερώνει το UI με τους βαθμούς στο **marks**.

### 3.14.2 showAverages() -\> None

Υπολογίζει τους μέσους όρους των βαθμών και καλεί την **setLabels()**.

### 3.14.3 showLatest() -\> None

Βρίσκει τους πιο πρόσφατους βαθμούς και καλεί την **setLabels()**.

### 3.14.4 showBest() -\> None

Υπολογίζει τους μέγιστους βαθμούς και καλεί την **setLabels()**.

# 4 Διαδικασία Επέκτασης

Η εφαρμογή μπορεί να επεκταθεί με διάφορους τρόπους προς πολλές
κατευθύνσεις. Σε αυτή την ενότητα θα δούμε κάποιες από αυτές τις
κατευθύνσεις.

## 4.1 Προαπαιτούμενα και Προϋποθέσεις

Για να επεκταθεί η εφαρμογή υπάρχουν κάποιες προυποθέσεις που πρέπει να
τηρηθούν.

### 4.1.1 Γνώσεις

-   Ανάπτυξη εφαρμογών σε python3
-   Γνώσεις χρήσης qt5 gui framework
-   Γνώσεις χρήσης pandas (για στατιστικά)

### 4.1.2 Λογισμικό

-   Εγκατάσταση python \>= 3.10
-   Εγκατάσταση poetry
-   Εγκατάσταση git

### 4.1.3 Άδεια

Παράγωγα έργα **πρέπει** να ακολουθούν τους όρους του AGPLv3 όπως
ορίζονται στο αρχείο LICENSE.

## 4.2 Επιπλέον Υλικό Θεωρίας

Επιπλέον υλικό θεωρίας μπορεί να δημιουργηθεί δημιουργώντας κατάλληλα
ονομασμένα αρχεία στον φάκελο `resources/lessons/`. Πιο συγκεκριμένα
πρέπει να ακολουθούν το πρότυπο “lesson<αριθμόςΚεφαλαίου>.html” με
προσοχή ότι γίνεται λεξικογραφική ταξινόμηση όπου τα μεγαλύτερα ονόματα
έρχονται πρώτα όταν δηλαδή το αρχείο `lesson2.1.html` θα εμφανιστεί πριν
το αρχείο `lesson2.html`, έτσι προτείνεται το δεύτερο αρχείο να
μετονομαστεί σε `lesson2.0.html`. Τέλος θα πρέπει να προστεθεί το
αντίστοιχο κουμπί στην κλάση *LessonWidget*

## 4.3 Επιπλέον Ασκήσεις

Επιπλέον υλικό ασκήσεων μπορεί να δημιουργηθεί στην κλάση **Exercises**
με παρόμοιο τρόπο όπως οι υπάρχουσες. Προσοχή να δοθεί στο **text** των
**FillBlankQuestion** όπου οι χαρακτήρες ᾽&᾽ σημαίνουν “κενό προς
γέμισμα” και ‘\\n’ νέα γραμμή.

## 4.4 Επιπλέον Λειτουργικότητα

Η εφαρμογή έχει σχεδιαστεί με την επεκτασιμότητα στο νου άρα οποιαδήποτε
λειτουργία είναι πιθανός υλοποιήσημη λόγω της modular δομής της. Για
παράδειγμα είναι πολύ απλό να προστεθεί ένα νέο είδος ερώτησης. Απλά θα
χρειαστεί:

-   class \<New\>Question
-   class \<New\>QuestionWidget
-   υποστήριξη στην ΟverviewQuestionWidget στο match statement

<div id="refs" class="references csl-bib-body hanging-indent">

<div id="ref-Rmd" class="csl-entry">

Allaire, JJ, Yihui Xie, Jonathan McPherson, Javier Luraschi, Kevin
Ushey, Aron Atkins, Hadley Wickham, Joe Cheng, Winston Chang, και
Richard Iannone. 2021. *rmarkdown: Dynamic Documents for R*.
<https://github.com/rstudio/rmarkdown>.

</div>

<div id="ref-progit" class="csl-entry">

Chacon, Scott, και Ben Straub. 2014. *Pro git*. Apress.

</div>

<div id="ref-poetry" class="csl-entry">

Poetry core contributors. 2022. ‘Poetry official website’.
<https://python-poetry.org>.

</div>

<div id="ref-RmdDG" class="csl-entry">

Xie, Yihui, J. J. Allaire, και Garrett Grolemund. 2018. *R Markdown: The
Definitive Guide*. Boca Raton, Florida: Chapman; Hall/CRC.
<https://bookdown.org/yihui/rmarkdown>.

</div>

<div id="ref-RmdCB" class="csl-entry">

Xie, Yihui, Christophe Dervieux, και Emily Riederer. 2020. *R Markdown
Cookbook*. Boca Raton, Florida: Chapman; Hall/CRC.
<https://bookdown.org/yihui/rmarkdown-cookbook>.

</div>

</div>

[^1]: lesson<n>.\*: αρχίζει με τους χαρακτήρες ‘lesson’ και ακολουθείτε
    από έναν αριθμό n
