import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog,QApplication,QWidget,QMainWindow
import sqlite3
from PyQt5.QtChart import QChart,QChartView,QValueAxis,QBarCategoryAxis,QBarSet,QBarSeries
from PyQt5.Qt import Qt
from PyQt5.QtGui import QPainter
import random
# import bcrypt
database_name ='sample'
with open("myfile.txt", "r+") as file1:
    # Reading form a file
    database_name = file1.read()
    print(database_name)
class WelcomeScreen(QMainWindow):
    def __init__(self):
        super(WelcomeScreen,self).__init__()
        loadUi('untitled.ui',self)
        self.login_button.clicked.connect(self.gotologin)

    def gotologin(self):
        print('nice')
        username = self.username.text()
        password = self.password.text()
        print(username,password)
        if username == '' or password == '':
            self.messages.setText('please input all fields')
        else:
            con = sqlite3.connect(database_name)
            cur = con.cursor()
            query = f'select password from loginform where first_name ="{username}"'
            cur.execute(query)
            result = cur.fetchone()[0]
            # password = password.encode('utf-8')
            # result = result.encode('utf-8')
            # if bcrypt.checkpw(password,result):
            if result == password:
                login = LoginScreen()
                widgets.addWidget(login)
                widgets.setCurrentIndex(widgets.currentIndex()+1)
            else:
                self.messages.setText('invalid username and passsword')
    
        



class LoginScreen(QDialog):
    def __init__(self):
        super(LoginScreen,self).__init__()
        loadUi('loggedinview.ui',self)
        self.create_user.clicked.connect(self.Createuser)
        self.gotoconfig.clicked.connect(self.GotoConfig)
        self.logout.clicked.connect(self.logouts)
        self.chart.clicked.connect(self.charts)

    def Createuser(self):
        username = self.username.text()
        password = self.password1.text()
        password2 = self.password2.text()
        print(username,password,password2)
        if username == '' or password == '' or password2 == '':
            self.messages.setText('input all fields')
            print('gone')
        else:
            if password2 == password:
                # bytes = password.encode('utf-8')
                # salt = bcrypt.gensalt()
                # hash = bcrypt.hashpw(bytes, salt)
                print('entered')
                con = sqlite3.connect(database_name)
                cur = con.cursor()
                query = f'INSERT INTO loginform (first_name,password) VALUES ("{username}","{hash}")'
                cur.execute(query)
                print('welcome')
                con.commit()
                self.username.setText('')
                self.password1.setText('')
                self.password2.setText('')
    
    def logouts(self):
        conf = WelcomeScreen()
        widgets.addWidget(conf)
        widgets.setCurrentIndex(widgets.currentIndex()+1)
                
    def GotoConfig(self):
        conf = ConfigScreen()
        widgets.addWidget(conf)
        widgets.setCurrentIndex(widgets.currentIndex()+1)
    
    def charts(self):
        print('entere')
        conf = ChartView()
        widgets.addWidget(conf)
        widgets.setCurrentIndex(widgets.currentIndex()+1)
        print('finished')


class ConfigScreen(QDialog):
    def __init__(self):
        super(ConfigScreen, self).__init__()
        loadUi('config_screen.ui',self)
        self.database_name.setText(database_name)
        self.change.clicked.connect(self.changedb)
        self.back4.clicked.connect(self.backs)
        self.login_table.setText('loginform')
        self.chart_table.setText('chart')
        
    def changedb(self):
        name = self.change_db_name.text()
        if name == '' or name == None:
            pass
        else:
            database_name = name
            with open("myfile.txt", "w") as file1:
                file1.write(name)
            print(database_name)
    def backs(self):
        conf = LoginScreen()
        widgets.addWidget(conf)
        widgets.setCurrentIndex(widgets.currentIndex()+1)

    


class ChartView(QMainWindow):
    def __init__(self):
        super(ChartView,self).__init__()
        loadUi('chartsV.ui',self)
        self.resize(800,600)
        set0 = QBarSet('data')
        

        con = sqlite3.connect(database_name)
        cur = con.cursor()
        query = f'select data from reports where months ="jan"'
        cur.execute(query)
        result = cur.fetchone()[0]

        result0 = int(result)


        

        query = f'select data from reports where months ="feb"'
        cur.execute(query)
        result = cur.fetchone()[0]

        result2 = int(result)

        query = f'select data from reports where months ="mar"'
        cur.execute(query)
        result = cur.fetchone()[0]

        result3 = int(result)

        query = f'select data from reports where months ="apr"'
        cur.execute(query)
        result = cur.fetchone()[0]

        result4 = int(result)


        query = f'select data from reports where months ="may"'
        cur.execute(query)
        result = cur.fetchone()[0]

        result5 = int(result)


        query = f'select data from reports where months ="jun"'
        cur.execute(query)
        result = cur.fetchone()[0]

        result6 = int(result)       
        
        set0.append([result0,result2,result3,result4,result5,result6])
        
        
        series = QBarSeries()
        series.append(set0)
        

        chart = QChart()
        chart.addSeries(series)
        chart.setAnimationOptions(QChart.SeriesAnimations)
        print(result0,result2)

        months = ('jan','feb','mar','apr','may','jun')


        axisX = QBarCategoryAxis()
        axisX.append(months)

        axisY = QValueAxis()
        axisY.setRange(0,100)
        chart.addAxis(axisX,Qt.AlignBottom)
        chart.addAxis(axisY,Qt.AlignLeft)
        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)
        charView = QChartView(chart)
        self.setCentralWidget(charView)








app = QApplication(sys.argv)
welcome = WelcomeScreen()
widgets = QtWidgets.QStackedWidget()
widgets.addWidget(welcome)
widgets.setFixedHeight(800)
widgets.setFixedWidth(1200)
widgets.show()
try:
    sys.exit(app.exec_())
except:
    print('exiting')