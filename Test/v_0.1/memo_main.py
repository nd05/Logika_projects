import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from memo_data import Form
from random import randint, shuffle
import fileinput

class Application(QWidget):
    cor, incor, iter= 0, 0, 0
    group_box= 'Qwest'
    def get_data(self):
        self.qwestions= []
        for line in fileinput.input(files ='memory.txt'):
            qw= line.split(' | ')
            self.qwestions.append(Form(qw[0], qw[1], qw[2], qw[3], qw[4]))
    def write_data(self):
        memory= open('memory.txt', 'w')
        for i in range(len(self.qwestions)):
            out= [self.qwestions[i].question, self.qwestions[i].answer, self.qwestions[i].wrong_answer1, self.qwestions[i].wrong_answer2, self.qwestions[i].wrong_answer3]
            str_out= ' | '.join(out)
            memory.write(str_out+'\n')
        memory.close()
    def __init__(self):
        super().__init__()
        self.get_data()
        self.number_of_qwestions= len(self.qwestions)
        self.initUI()
    def initUI(self):
        self.setGeometry(300, 300, 500, 200)
        self.setWindowTitle('Memory_card')
        
        self.menue= QPushButton('Меню')
        self.menue.clicked.connect(self.show_menue)
        self.run_memory_test= QPushButton('Тестування')
        self.run_memory_test.clicked.connect(self.show_memory)
        self.run_test_editor= QPushButton('До редактору')
        self.run_test_editor.clicked.connect(self.go_to_Test_editor)
        self.relaxation= QPushButton('Відплчинок')
        self.relaxation.clicked.connect(self.start_rest)
        self.min= QDoubleSpinBox()
        self.time_text= QLabel('Хвилин')
        self.quest= QLabel('')
        self.progr_of_resting= QProgressBar()
        self.ans_button= QPushButton('Відповісти')
        self.ans_button_pos= 'Qwestion'
        self.ans_button.clicked.connect(self.cange)

        layoutH1= QHBoxLayout()
        layoutH2= QHBoxLayout()
        layoutH3= QHBoxLayout()
        layoutH4= QHBoxLayout()

        layoutH1.addWidget(self.menue)
        layoutH1.addWidget(self.run_memory_test)
        self.run_memory_test.hide()
        layoutH1.addStretch(1)
        layoutH1.addWidget(self.run_test_editor)
        self.run_test_editor.hide()
        layoutH1.addWidget(self.relaxation)
        layoutH1.addWidget(self.min)
        layoutH1.addWidget(self.time_text)
        
        layoutH2.addWidget(self.quest, alignment = Qt.AlignCenter)
        layoutH2.addWidget(self.progr_of_resting, alignment= Qt.AlignCenter)
        self.progr_of_resting.hide()

        self.qestion()
        self.test_end()
        self.ans_for_qwestion()
        self.show_qw()

        layoutH3.addWidget(self.AnsGroupbox)
        layoutH3.addWidget(self.QwestGroupbox)
        layoutH3.addWidget(self.ResGroupBox)

        layoutH4.addWidget(self.ans_button, alignment = Qt.AlignCenter)

        v_line= QVBoxLayout()
        v_line.addLayout(layoutH1)
        v_line.addLayout(layoutH2)
        v_line.addLayout(layoutH3)
        v_line.addLayout(layoutH4)
        
        self.setLayout(v_line)
        self.show()
    def show_menue(self):
        self.menue.hide()
        self.run_memory_test.show()
        self.run_test_editor.show()
        self.relaxation.hide()
        self.min.hide()
        self.time_text.hide()
        self.quest.hide()
        self.QwestGroupbox.hide()
        self.AnsGroupbox.hide()
        self.ResGroupBox.hide()
        self.ans_button.hide()
    def show_memory(self):
        self.menue.show()
        self.run_memory_test.hide()
        self.run_test_editor.hide()
        self.relaxation.show()
        self.min.show()
        self.time_text.show()
        self.quest.show()
        if self.group_box == 'Qwest':
            self.QwestGroupbox.show()
        else:
            self.QwestGroupbox.hide()
        if self.group_box == 'Ans':
            self.AnsGroupbox.show()
        else:
            self.AnsGroupbox.hide()
        if self.group_box == 'End':
            self.ResGroupBox.show()
        else:
            self.ResGroupBox.hide()
        self.ans_button.show()
    def start_rest(self):
        self.progr_of_resting.show()
        time_of_resting= int(60*self.min.value())
        self.progr_of_resting= QProgressBar()
        self.quest.hide()
        self.QwestGroupbox.hide()
        self.AnsGroupbox.hide()
        self.ResGroupBox.hide()
        self.ans_button.hide()
        self.progr_of_resting.show()
        #Я пока не разобрался с QTimer
    #Часть Application с тестом
    def qestion(self):
        shuffle(self.qwestions)
        self.QwestGroupbox= QGroupBox('Питання')
        self.QwestGroupbox.show()

        self.rBtn1= QRadioButton()
        self.rBtn2= QRadioButton()
        self.rBtn3= QRadioButton()
        self.rBtn4= QRadioButton()
 
        layoutH2= QHBoxLayout()
        layoutH3= QHBoxLayout()

        layoutH2.addWidget(self.rBtn1, alignment = Qt.AlignCenter)
        layoutH2.addWidget(self.rBtn2, alignment = Qt.AlignCenter)

        layoutH3.addWidget(self.rBtn3, alignment = Qt.AlignCenter)
        layoutH3.addWidget(self.rBtn4, alignment = Qt.AlignCenter)

        V_line= QVBoxLayout()
        V_line.addLayout(layoutH2)
        V_line.addLayout(layoutH3)

        self.QwestGroupbox.setLayout(V_line)
        
        self.positions= ['not', 'not', 'not', 'not']
        self.rBtn1.clicked.connect(self.action_of_radiobutton1)
        self.rBtn2.clicked.connect(self.action_of_radiobutton2)
        self.rBtn3.clicked.connect(self.action_of_radiobutton3)
        self.rBtn4.clicked.connect(self.action_of_radiobutton4)
    def ans_for_qwestion(self):
        self.AnsGroupbox= QGroupBox('Відповідь')
        self.AnsGroupbox.hide()
        self.ans= QLabel('')
        
        v_line= QVBoxLayout()
        v_line.addWidget(self.ans, alignment= Qt.AlignCenter)
        self.AnsGroupbox.setLayout(v_line)
    def test_end(self):
        self.quest.setText('Результат')
        self.ResGroupBox = QGroupBox('Результат тесту')
        self.ResGroupBox.hide()
        
        V_line= QVBoxLayout()
        self.text = QLabel('-')
        V_line.addWidget(self.text, alignment = Qt.AlignCenter)
        self.ResGroupBox.setLayout(V_line)
    def cange(self):
        if self.ans_button_pos == 'Qwestion':
            self.show_ans()
            if self.iter != self.number_of_qwestions-1:
                self.ans_button_pos= 'Answer'
                self.ans_button.setText('Наступне питання')
            else:
                self.ans_button_pos= 'Results'
                self.ans_button.setText('Перейти до результату')
        elif self.ans_button_pos == 'Answer':
            self.ans_button_pos= 'Qwestion'
            self.ans_button.setText('Відповісти')
            self.iter+= 1
            self.show_qw()
        elif self.ans_button_pos == 'Results':
            self.show_end()
            self.ans_button.setText('Перейти до редактору тесту')
            self.ans_button_pos= 'Go to the test redactor'
        else:
            self.go_to_Test_editor()
    def show_qw(self):
        self.quest.setText(self.qwestions[self.iter].question)
        answers_for_the_qw= [self.qwestions[self.iter].answer, self.qwestions[self.iter].wrong_answer1, self.qwestions[self.iter].wrong_answer2, self.qwestions[self.iter].wrong_answer3]
        text_of_qw= answers_for_the_qw[randint(0, 3)]
        if self.qwestions[self.iter].answer == text_of_qw:
            self.corect= 0
        answers_for_the_qw.remove(text_of_qw)
        self.rBtn1.setText(text_of_qw)
        text_of_qw= answers_for_the_qw[randint(0, 2)]
        if self.qwestions[self.iter].answer == text_of_qw:
            self.corect= 1
        answers_for_the_qw.remove(text_of_qw)
        self.rBtn2.setText(text_of_qw)
        text_of_qw= answers_for_the_qw[randint(0, 1)]
        if self.qwestions[self.iter].answer == text_of_qw:
            self.corect= 2
        answers_for_the_qw.remove(text_of_qw)
        self.rBtn3.setText(text_of_qw)
        if self.qwestions[self.iter].answer == answers_for_the_qw[0]:
            self.corect= 3
        self.rBtn4.setText(answers_for_the_qw[0])

        self.group_box= 'Qwest'
        self.QwestGroupbox.show()
        self.AnsGroupbox.hide()
        self.ResGroupBox.hide()
    def show_ans(self):
        self.ans.setText(self.qwestions[self.iter].answer)
        if self.positions[self.corect] == 'act':
            self.cor+= 1
        else:
            self.incor+= 1

        self.group_box= 'Ans'
        self.QwestGroupbox.hide()
        self.AnsGroupbox.show()
        self.ResGroupBox.hide()
    def action_of_radiobutton1(self):
        self.positions[0]= 'act'
        self.positions[1]= 'not'
        self.positions[2]= 'not'
        self.positions[3]= 'not'
    def action_of_radiobutton2(self):
        self.positions[0]= 'not'
        self.positions[1]= 'act'
        self.positions[2]= 'not'
        self.positions[3]= 'not'
    def action_of_radiobutton3(self):
        self.positions[0]= 'not'
        self.positions[1]= 'not'
        self.positions[2]= 'act'
        self.positions[3]= 'not'
    def action_of_radiobutton4(self):
        self.positions[0]= 'not'
        self.positions[1]= 'not'
        self.positions[2]= 'not'
        self.positions[3]= 'act'
    def show_end(self):
        self.group_box= 'End'
        self.QwestGroupbox.hide()
        self.AnsGroupbox.hide()
        self.ResGroupBox.show()
        self.text.setText(str(self.cor)+'/'+str(self.cor+self.incor)+'\n'+str(self.cor/(self.cor+self.incor)*100)+'%')
    def go_to_Test_editor(self):
        self.menue.hide()
        self.run_memory_test.hide()
        self.run_test_editor.hide()
        self.relaxation.hide()
        self.min.hide()
        self.time_text.hide()
        self.quest.hide()
        self.QwestGroupbox.hide()
        self.AnsGroupbox.hide()
        self.ResGroupBox.hide()
        self.ans_button.hide()
        self.init_test_editor()
    #Часть Application с редактором теста
    def init_test_editor(self):
        self.setGeometry(300, 300, 500, 200)
        self.setWindowTitle('Список питань')


app= QApplication(sys.argv)
main_win= Application()
app.exec_()