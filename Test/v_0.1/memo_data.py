import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from random import randint, shuffle
import fileinput

class Form():
    def __init__(self, question='?', answer='!', wrong_answer1='-', wrong_answer2='-', wrong_answer3='-'):
        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3

'''
class edit_memory(QWidget):
    def get_data(self):
        self.qwestions= []
        for line in fileinput.input(files ='/Users/macbook/Documents/my_programs/2022-2023/Logika/Test/memory.txt'):
            qw= line.split(' | ')
            self.qwestions.append(Form(qw[0], qw[1], qw[2], qw[3], qw[4]))
    def write_data(self):
        memory= open('/Users/macbook/Documents/my_programs/2022-2023/Logika/Test/memory.txt', 'w')
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
        self.setWindowTitle('Список питань')
        
        listView = QListView()
        slm = QStringListModel()
        self.qList = []
        for i in range(len(self.qwestions)):
            self.qList.append(self.qwestions[i].question)
        slm.setStringList(self.qList)
        listView.setModel(slm)
        layout_form= QFormLayout()
        txt_ans= QLineEdit('')
        layout_form.addRow(
            'Питання:', txt_ans
        )

        layoutH1= QHBoxLayout()
        layoutH2= QHBoxLayout()
        layoutH3= QHBoxLayout()
        
        layoutH1.addWidget(listView)
        layoutH1.addLayout(layout_form)

        v_line= QVBoxLayout()
        v_line.addLayout(layoutH1)
        v_line.addLayout(layoutH2)
        v_line.addLayout(layoutH3)
        
        self.setLayout(v_line)
        self.show()

app= QApplication(sys.argv)
main_win= edit_memory()
app.exec_()
'''