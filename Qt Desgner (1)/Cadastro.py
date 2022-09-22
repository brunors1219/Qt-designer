# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Tela de Cadastro.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Janela_cadastrato(object):
    def setupUi(self, Janela_cadastrato):
        Janela_cadastrato.setObjectName("Janela_cadastrato")
        Janela_cadastrato.resize(1920, 1080)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:\Qt Desgner\K-removebg-preview (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Janela_cadastrato.setWindowIcon(icon)
        Janela_cadastrato.setStyleSheet("background-color: rgb(205,240,255);")
        Janela_cadastrato.setDocumentMode(False)
        Janela_cadastrato.setDockNestingEnabled(True)
        Janela_cadastrato.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(Janela_cadastrato)
        self.centralwidget.setObjectName("centralwidget")
        self.Button_Cadastrar = QtWidgets.QPushButton(self.centralwidget)
        self.Button_Cadastrar.setGeometry(QtCore.QRect(870, 860, 161, 61))
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
        self.Numero = QtWidgets.QLabel(self.centralwidget)
        self.Numero.setGeometry(QtCore.QRect(620, 310, 721, 101))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(50)
        self.Numero.setFont(font)
        self.Numero.setAlignment(QtCore.Qt.AlignCenter)
        self.Numero.setObjectName("Numero")
        self.CEP = QtWidgets.QLabel(self.centralwidget)
        self.CEP.setGeometry(QtCore.QRect(840, 610, 37, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.CEP.setFont(font)
        self.CEP.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.CEP.setObjectName("CEP")
        self.Endereo = QtWidgets.QLabel(self.centralwidget)
        self.Endereo.setGeometry(QtCore.QRect(820, 640, 71, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.Endereo.setFont(font)
        self.Endereo.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Endereo.setObjectName("Endereo")
        self.Bairro = QtWidgets.QLabel(self.centralwidget)
        self.Bairro.setGeometry(QtCore.QRect(840, 700, 61, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.Bairro.setFont(font)
        self.Bairro.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Bairro.setObjectName("Bairro")
        self.CPF = QtWidgets.QLabel(self.centralwidget)
        self.CPF.setGeometry(QtCore.QRect(850, 670, 37, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.CPF.setFont(font)
        self.CPF.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.CPF.setObjectName("CPF")
        self.Cidade = QtWidgets.QLabel(self.centralwidget)
        self.Cidade.setGeometry(QtCore.QRect(840, 730, 61, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.Cidade.setFont(font)
        self.Cidade.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Cidade.setObjectName("Cidade")
        self.UF = QtWidgets.QLabel(self.centralwidget)
        self.UF.setGeometry(QtCore.QRect(850, 770, 37, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.UF.setFont(font)
        self.UF.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.UF.setObjectName("UF")
        self.CPF_campo = QtWidgets.QLineEdit(self.centralwidget)
        self.CPF_campo.setGeometry(QtCore.QRect(910, 480, 133, 20))
        self.CPF_campo.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.CPF_campo.setAlignment(QtCore.Qt.AlignCenter)
        self.CPF_campo.setObjectName("CPF_campo")
        self.Data_nas_campo = QtWidgets.QLineEdit(self.centralwidget)
        self.Data_nas_campo.setGeometry(QtCore.QRect(910, 510, 133, 20))
        self.Data_nas_campo.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.Data_nas_campo.setAlignment(QtCore.Qt.AlignCenter)
        self.Data_nas_campo.setObjectName("Data_nas_campo")
        self.Contato_campo = QtWidgets.QLineEdit(self.centralwidget)
        self.Contato_campo.setGeometry(QtCore.QRect(910, 540, 133, 20))
        self.Contato_campo.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.Contato_campo.setAlignment(QtCore.Qt.AlignCenter)
        self.Contato_campo.setObjectName("Contato_campo")
        self.Data_cad_campo = QtWidgets.QLineEdit(self.centralwidget)
        self.Data_cad_campo.setGeometry(QtCore.QRect(910, 570, 133, 20))
        self.Data_cad_campo.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.Data_cad_campo.setAlignment(QtCore.Qt.AlignCenter)
        self.Data_cad_campo.setObjectName("Data_cad_campo")
        self.CEP_campo = QtWidgets.QLineEdit(self.centralwidget)
        self.CEP_campo.setGeometry(QtCore.QRect(910, 610, 133, 20))
        self.CEP_campo.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.CEP_campo.setAlignment(QtCore.Qt.AlignCenter)
        self.CEP_campo.setObjectName("CEP_campo")
        self.Endereo_campo = QtWidgets.QLineEdit(self.centralwidget)
        self.Endereo_campo.setGeometry(QtCore.QRect(910, 640, 133, 20))
        self.Endereo_campo.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.Endereo_campo.setAlignment(QtCore.Qt.AlignCenter)
        self.Endereo_campo.setObjectName("Endereo_campo")
        self.Numero_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.Numero_2.setGeometry(QtCore.QRect(910, 670, 133, 20))
        self.Numero_2.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.Numero_2.setAlignment(QtCore.Qt.AlignCenter)
        self.Numero_2.setObjectName("Numero_2")
        self.Bairro_campo = QtWidgets.QLineEdit(self.centralwidget)
        self.Bairro_campo.setGeometry(QtCore.QRect(910, 700, 133, 20))
        self.Bairro_campo.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.Bairro_campo.setAlignment(QtCore.Qt.AlignCenter)
        self.Bairro_campo.setObjectName("Bairro_campo")
        self.Cidade_campo = QtWidgets.QLineEdit(self.centralwidget)
        self.Cidade_campo.setGeometry(QtCore.QRect(910, 730, 133, 20))
        self.Cidade_campo.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.Cidade_campo.setAlignment(QtCore.Qt.AlignCenter)
        self.Cidade_campo.setObjectName("Cidade_campo")
        self.UF_campo = QtWidgets.QLineEdit(self.centralwidget)
        self.UF_campo.setGeometry(QtCore.QRect(910, 770, 133, 20))
        self.UF_campo.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.UF_campo.setAlignment(QtCore.Qt.AlignCenter)
        self.UF_campo.setObjectName("UF_campo")
        self.Contato = QtWidgets.QLabel(self.centralwidget)
        self.Contato.setGeometry(QtCore.QRect(830, 540, 53, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.Contato.setFont(font)
        self.Contato.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Contato.setObjectName("Contato")
        self.Nome_campo = QtWidgets.QLineEdit(self.centralwidget)
        self.Nome_campo.setGeometry(QtCore.QRect(910, 450, 133, 20))
        self.Nome_campo.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.Nome_campo.setAlignment(QtCore.Qt.AlignCenter)
        self.Nome_campo.setObjectName("Nome_campo")
        self.Data_nas = QtWidgets.QLabel(self.centralwidget)
        self.Data_nas.setGeometry(QtCore.QRect(810, 510, 86, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.Data_nas.setFont(font)
        self.Data_nas.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Data_nas.setObjectName("Data_nas")
        self.CPF_2 = QtWidgets.QLabel(self.centralwidget)
        self.CPF_2.setGeometry(QtCore.QRect(850, 480, 31, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.CPF_2.setFont(font)
        self.CPF_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.CPF_2.setObjectName("CPF_2")
        self.Nome = QtWidgets.QLabel(self.centralwidget)
        self.Nome.setGeometry(QtCore.QRect(840, 450, 51, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.Nome.setFont(font)
        self.Nome.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Nome.setObjectName("Nome")
        self.Data_cad = QtWidgets.QLabel(self.centralwidget)
        self.Data_cad.setGeometry(QtCore.QRect(780, 570, 118, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.Data_cad.setFont(font)
        self.Data_cad.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Data_cad.setObjectName("Data_cad")
        self.Fucionario = QtWidgets.QLabel(self.centralwidget)
        self.Fucionario.setGeometry(QtCore.QRect(820, 800, 81, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.Fucionario.setFont(font)
        self.Fucionario.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Fucionario.setObjectName("Fucionario")
        self.funcionario_campo = QtWidgets.QLineEdit(self.centralwidget)
        self.funcionario_campo.setGeometry(QtCore.QRect(910, 800, 133, 20))
        self.funcionario_campo.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.funcionario_campo.setAlignment(QtCore.Qt.AlignCenter)
        self.funcionario_campo.setObjectName("funcionario_campo")
        Janela_cadastrato.setCentralWidget(self.centralwidget)

        self.retranslateUi(Janela_cadastrato)
        QtCore.QMetaObject.connectSlotsByName(Janela_cadastrato)

    def retranslateUi(self, Janela_cadastrato):
        _translate = QtCore.QCoreApplication.translate
        Janela_cadastrato.setWindowTitle(_translate("Janela_cadastrato", "Kitton Informático"))
        self.Button_Cadastrar.setText(_translate("Janela_cadastrato", "Cadastrar "))
        self.Numero.setText(_translate("Janela_cadastrato", "Cadastro de Cliente"))
        self.CEP.setText(_translate("Janela_cadastrato", "CEP"))
        self.Endereo.setText(_translate("Janela_cadastrato", "Endereço"))
        self.Bairro.setText(_translate("Janela_cadastrato", "Bairro"))
        self.CPF.setText(_translate("Janela_cadastrato", "N°"))
        self.Cidade.setText(_translate("Janela_cadastrato", "Cidade"))
        self.UF.setText(_translate("Janela_cadastrato", "UF"))
        self.Contato.setText(_translate("Janela_cadastrato", "Contato"))
        self.Data_nas.setText(_translate("Janela_cadastrato", "Data de Nac."))
        self.CPF_2.setText(_translate("Janela_cadastrato", "CPF"))
        self.Nome.setText(_translate("Janela_cadastrato", "Nome"))
        self.Data_cad.setText(_translate("Janela_cadastrato", "Data de Cadastro"))
        self.Fucionario.setText(_translate("Janela_cadastrato", "Fucionario"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Janela_cadastrato()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())