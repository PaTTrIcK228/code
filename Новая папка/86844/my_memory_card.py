from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QRadioButton, QGroupBox, QButtonGroup
from random import shuffle

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = Question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
    def ask(self,question, right_answer, wrong1, wrong2, wrong3):
        self,shuffle(answers)
        answers[0].setText(right_answer)
        answers[1].setText(right_answer)
        answers[2].setText(right_answer)
        answers[3].setText(right_answer)
        ln_correct.setText(right_answer)
        lb_Question.setText(question)
        show_question()

q = Question('123', '1', '2', '3', '4')

question_list = []
question_list.append(Question('Государственный язык Португалии','Португальский', 'Английский', 'Испанский', 'Французский'))
question_list.append(Question('Какой национальности не существует?','Энцы','Чулымцы','Смурфы','Алеуты'))

app = QApplication([])
window = QWidget()
window.setWindowTitle('Memory card')

btn_OK = QPushButton('Ответить')
lb_Question = QLabel('Какой национальности не существует?')

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
layout_card = QVBoxLayout()
layout_card.setSpacing(20)

layout_line1.addWidget(lb_Question)

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2)
layout_line3.addStretch(1)

layout_card.addLayout(layout_line1)
layout_card.addLayout(layout_line2)
layout_card.addLayout(layout_line3)

rbtn_1 = QRadioButton('Энцы')
rbtn_2 = QRadioButton('Чулымцы')
rbtn_3 = QRadioButton('Смурфы')
rbtn_4 = QRadioButton('Алеуты')

RadioGroup = QButtonGroup() 
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

RadioGroupBox = QGroupBox('Варианты ответов')

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)
layout_line2.addWidget(RadioGroupBox)
#Панель результата
AnsGroupBox = QGroupBox('Результат:')
lb_Result = QLabel('Правильно/Неправильно')
lb_Correct = QLabel('Правильный ответ')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result)
layout_res.addWidget(lb_Correct)

AnsGroupBox.setLayout(layout_res)

layout_line2.addWidget(AnsGroupBox)

AnsGroupBox.hide()

def Show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')

def show_question():
    AnsGroupBox.hide()
    RadioGroupBox.show()
    btn_OK.setText('Ответить')

    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

def test():
    if btn_OK.text() == 'Ответить':
        Show_result()
    else:
        show_question()

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(self,question, right_answer, wrong1, wrong2, wrong3):
    self,shuffle(answers)
    answers[0].setText(right_answer)
    answers[1].setText(right_answer)
    answers[2].setText(right_answer)
    answers[3].setText(right_answer)
    ln_correct.setText(right_answer)
    lb_Question.setText(question)
    show_question()

btn_OK.clicked.connect(test)

def show_correct(res):
    lb_Result.setText(res)
    Show_result()

def check_answer():
    if answer[0].isCheked():
        show_correct('Правильный ответ')
    elif answer[1].isCheked():
        show_correct('Неправильный ответ')
    elif answer[2].isCheked():
        show_correct('Неправильный ответ')
    elif answer[3].isCheked():
        show_correct('Неправильный ответ')

window.cur_question = -1
def next_question():
    window.cur_question += 1
    if window.cur_question >= len(question_list):
        window.cur_question = 0
    q = question_list[window.cur_question]
    ask(q)
    
def click_ok():
    if btn_OK.text == 'Ответить':
        check_answer()
    elif btn_OK.text == 'Следующий вопрос':
        next_question()




window.setLayout(layout_card)

window.show()
app.exec()  