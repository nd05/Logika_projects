import sys, os
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import fileinput
from PyQt5 import Qt
class Form():
    def __init__(self, question='?', answer='!', wrong_answer1='-', wrong_answer2='-', wrong_answer3='-'):
        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3


class edit_memory(QWidget):
    value= 0
    active= -1
    def get_data(self):
        self.qwestions= []
        for line in fileinput.input(files = os.path.dirname(os.path.abspath(__file__))+'/memory.txt'):
            qw= line.split(' | ')
            self.qwestions.append(Form(qw[0], qw[1], qw[2], qw[3], qw[4]))
    def write_data(self):
        memory= open(os.path.dirname(os.path.abspath(__file__))+'/memory.txt', 'w')
        for i in range(len(self.qwestions)):
            out= [self.qwestions[i].question, self.qwestions[i].answer, self.qwestions[i].wrong_answer1, self.qwestions[i].wrong_answer2, self.qwestions[i].wrong_answer3, ' ']
            str_out= ' | '.join(out)
            if i+1==len(self.qwestions):
                memory.write(str_out)
                #print(str_out)
            else:
                memory.write(str_out+'\n')
                #print(str_out+'/')
        memory.close()
    def __init__(self, parent):
        super(edit_memory, self).__init__()
        self.parent= parent
        self.get_data()
        self.number_of_qwestions= len(self.qwestions)
        self.initUI()
    def initUI(self):
        self.setGeometry(300, 300, 500, 200)
        self.setWindowTitle('Список питань')
        
        self.listView = QListView()
        self.slm = QStringListModel()
        self.qList = []
        for i in range(len(self.qwestions)):
            self.qList.append(self.qwestions[i].question)
        self.slm.setStringList(self.qList)
        self.listView.setModel(self.slm)
        self.listView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.listView.clicked.connect(self.change_func)

        layout_form= QFormLayout()
        self.txt_qwestion= QLineEdit('Виберіть')
        self.txt_answer= QLineEdit('питання')
        self.txt_WA1= QLineEdit('-')
        self.txt_WA2= QLineEdit('-')
        self.txt_WA3= QLineEdit('-')

        layout_form.addRow('Питання:', self.txt_qwestion)
        layout_form.addRow('Правильна відповідь:', self.txt_answer)
        layout_form.addRow('Не правильна відповідь', self.txt_WA1)
        layout_form.addRow('Не правильна відповідь', self.txt_WA2)
        layout_form.addRow('Не правильна відповідь', self.txt_WA3)

        new_qw= QPushButton('Додати питання', clicked= self.add_qw)
        erase_qw= QPushButton('Видалити питання', clicked= self.del_qw)
        to_test= QPushButton('Почати тренування', clicked= self.go_to_test)

        layoutH1= QHBoxLayout()
        layoutH2= QHBoxLayout()
        layoutH3= QHBoxLayout()
        
        layoutH1.addWidget(self.listView)
        layoutH1.addLayout(layout_form)

        layoutH2.addWidget(new_qw)
        layoutH2.addWidget(erase_qw)

        layoutH3.addStretch(1)
        layoutH3.addWidget(to_test)
        layoutH3.addStretch(1)

        v_line= QVBoxLayout()
        v_line.addLayout(layoutH1)
        v_line.addLayout(layoutH2)
        v_line.addLayout(layoutH3)
        
        self.setLayout(v_line)
        self.show()
    def change_func(self, modelIndex): 
        #print(self.listView.currentIndex().data())
        #эту часть программы надо настроить, пока она не работает стабильно
        if self.active != -1:
            #print(self.active)
            self.qwestions[self.active].question= self.txt_qwestion.text()
            self.qwestions[self.active].answer= self.txt_answer.text()
            self.qwestions[self.active].wrong_answer1= self.txt_WA1.text()
            self.qwestions[self.active].wrong_answer2= self.txt_WA2.text()
            self.qwestions[self.active].wrong_answer3= self.txt_WA3.text()
            
            self.qList[self.active]= self.qwestions[self.active].question
            #print(self.qList)
            self.slm.setStringList(self.qList)
            self.listView.setModel(self.slm)
        # Я нашел что именно этот кусок куда работает не стабильно и получается при первый итерации работает а потом нет на получается из-за того что первый итрации у него вход -1 и она просто не работает
        self.ind = modelIndex.row()
       
        #print('|', self.ind, '|', self.active,'|', modelIndex.row())
        self.txt_qwestion.setText(self.qwestions[self.ind].question)
        self.txt_answer.setText(self.qwestions[self.ind].answer)
        self.txt_WA1.setText(self.qwestions[self.ind].wrong_answer1)
        self.txt_WA2.setText(self.qwestions[self.ind].wrong_answer2)
        self.txt_WA3.setText(self.qwestions[self.ind].wrong_answer3)
        self.active= self.ind
    def add_qw(self):
        self.qwestions.append(Form())
        self.qList.append(self.qwestions[-1].question)
        self.slm.setStringList(self.qList)
        self.listView.setModel(self.slm)
        
    def del_qw(self):
        self.qwestions.remove(self.qwestions[self.ind])
        '''
        for i in range(len(self.qwestions)):
            print(self.qwestions[i].question)
        '''
        #print(self.qList)
        self.qList = []
        for i in range(len(self.qwestions)):
            self.qList.append(self.qwestions[i].question)
        #print(self.qList)
        self.slm.setStringList(self.qList)
        self.listView.setModel(self.slm)
        self.active = -1
    def go_to_test(self):
        self.write_data()
        self.parent.show()        
        self.hide() 