# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Tela Inicial.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1082)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:\Qt Desgner\K-removebg-preview (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(205,240,255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Button_Cadastrar = QtWidgets.QPushButton(self.centralwidget)
        self.Button_Cadastrar.setGeometry(QtCore.QRect(840, 630, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(18)
        self.Button_Cadastrar.setFont(font)
        self.Button_Cadastrar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Button_Cadastrar.setStyleSheet("QPushButton{\n"
"background-color: rgb(0, 0, 127);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"   background-color:white;\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.Button_Cadastrar.setObjectName("Button_Cadastrar")
        self.Button_Login = QtWidgets.QPushButton(self.centralwidget)
        self.Button_Login.setGeometry(QtCore.QRect(1040, 630, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(18)
        self.Button_Login.setFont(font)
        self.Button_Login.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Button_Login.setStyleSheet("QPushButton{\n"
"background-color: rgb(0, 0, 127);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"   background-color:white;\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.Button_Login.setObjectName("Button_Login")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(600, 180, 961, 631))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.Tela_inicial = QtWidgets.QLabel(self.frame)
        self.Tela_inicial.setGeometry(QtCore.QRect(90, 70, 721, 101))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(50)
        self.Tela_inicial.setFont(font)
        self.Tela_inicial.setAlignment(QtCore.Qt.AlignCenter)
        self.Tela_inicial.setObjectName("Tela_inicial")
        self.Imagem = QtWidgets.QLabel(self.frame)
        self.Imagem.setGeometry(QtCore.QRect(220, 120, 391, 361))
        self.Imagem.setText("")
        self.Imagem.setPixmap(QtGui.QPixmap("D:\Qt Desgner\K-removebg-preview (1).png"))
        self.Imagem.setScaledContents(True)
        self.Imagem.setObjectName("Imagem")
        self.Imagem.raise_()
        self.Tela_inicial.raise_()
        self.frame.raise_()
        self.Button_Cadastrar.raise_()
        self.Button_Login.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Kitton Informatica "))
        self.Button_Cadastrar.setText(_translate("MainWindow", "Cadastrar"))
        self.Button_Login.setText(_translate("MainWindow", "Login"))
        self.Tela_inicial.setText(_translate("MainWindow", "Tela Inicial "))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())