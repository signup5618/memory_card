from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QButtonGroup, QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QGroupBox, QHBoxLayout, QRadioButton
from random import shuffle 
from random import randint


class Question():
    def __init__(self,question,right_answer,wrong1,wrong2,wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Memory Card')

RadioGroupBox = QGroupBox('Answer options')

RB_1 = QRadioButton('Enets')
RB_2 = QRadioButton('Smurfs')
RB_3 = QRadioButton('Chulyms')
RB_4 = QRadioButton('Aleuts')

LO_A1 = QHBoxLayout()
LO_A2 = QVBoxLayout()
LO_A3 = QVBoxLayout()

LO_A2.addWidget(RB_1)
LO_A2.addWidget(RB_2)
LO_A3.addWidget(RB_3)
LO_A3.addWidget(RB_4)
LO_A1.addLayout(LO_A2)
LO_A1.addLayout(LO_A3)

RadioGroupBox.setLayout(LO_A1)

LO_A4 = QVBoxLayout()
LO_A5 = QHBoxLayout()
LO_A6 = QHBoxLayout()
LO_A7 = QHBoxLayout()

RB_5 = QLabel('Which nationality does not exist?')
RB_6 = QPushButton('Answer')

LO_A5.addWidget(RB_5)
LO_A6.addWidget(RB_6)
LO_A7.addWidget(RadioGroupBox)
LO_A4.addLayout(LO_A5)
LO_A4.addLayout(LO_A7)
LO_A4.addLayout(LO_A6)

main_win.setLayout(LO_A4)
main_win.resize(700,600)


RadioGroupBox_2 = QGroupBox('Test result')

RB_7 = QLabel('True/False')
RB_8 = QLabel('Correct answer')

LO_A8 = QHBoxLayout()
LO_A9 = QHBoxLayout()
LO_A10 = QVBoxLayout()

LO_A8.addWidget(RB_7)
LO_A9.addWidget(RB_8)
LO_A10.addLayout(LO_A8)
LO_A10.addLayout(LO_A9)
RadioGroupBox_2.setLayout(LO_A10)
LO_A7.addWidget(RadioGroupBox_2)



main_win.setLayout(LO_A8)
RadioGroupBox_2.hide()
RadioGroupBox.show()

def show_result():
    RadioGroupBox.hide()
    RadioGroupBox_2.show()
    RB_6.setText('Next question')

def show_question():
    RadioGroupBox_2.hide()
    RadioGroupBox.show()
    RB_6.setText('Answer')
    RadioGroup.setExclusive(False)
    RB_1.setChecked(False)
    RB_2.setChecked(False)
    RB_3.setChecked(False)
    RB_4.setChecked(False)
    RadioGroup.setExclusive(True)

RadioGroup = QButtonGroup()
RadioGroup.addButton(RB_1)
RadioGroup.addButton(RB_2)
RadioGroup.addButton(RB_3)
RadioGroup.addButton(RB_4)


answers = [RB_1,RB_2,RB_3,RB_4]

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    RB_5.setText(q.question)
    RB_8.setText(q.right_answer)
    show_question()

def check_answer():
    if answers[0].isChecked():
        RB_7.setText('corret')
        main_win.score += 1
    else:
        RB_7.setText('incorrect')
    show_result()

#RB_6.clicked.connect(start_test)

questions_list = []
q1 = Question('What is the specific heat of water?','1000 cal/kg.C','0.418 kJ/g.C',
'0.1 cal/g.C','4.18 J/kg.C')
questions_list.append(q1)

q2 = Question('The energy of the electron in any energy level equals?','P.E+K.E',
'P.E-K.E','P.E/K.E','P.E*K.E')
questions_list.append(q2)

q3 = Question('If A is a matrix of order 2*3, then the number of elements in matrix A is?',
'6','4','9','5')
questions_list.append(q3)

q4 = Question('tan X csc X?','sec X','1','cos X','csc X')
questions_list.append(q4)

q5 = Question('The purple-coloured flowers character appers in pea plant with two genotypes which are?',
'(RR)and(Rr)','(RR)and(RW)','(RR)and(rr)','(Rr)and(rr)')
questions_list.append(q5)

q6 = Question('The state language of Brazil', 'Portuguese', 'English', 'Spanish', 
'Brazilian')
questions_list.append(q6)


main_win.total = 0
main_win.score = 0

def next_question():
    main_win.total += 1
    r = randint(0,len(questions_list)-1)
    qr = questions_list[r]
    ask(qr)
    rating = main_win.score/main_win.total*100
    print('your rating is',rating)

def start_test():
    if RB_6.text() == 'Answer':
        check_answer()
    else:
        next_question()

next_question()
RB_6.clicked.connect(start_test)



main_win.show()
app.exec_()
