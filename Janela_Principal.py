from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_Janela_Principal(object):
    def setupUi(self, Janela_Principal, remedios):
        self.remedios = remedios
        Janela_Principal.setObjectName("Janela_Principal")
        Janela_Principal.resize(617, 452)
        self.centralwidget = QtWidgets.QWidget(Janela_Principal)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 191, 511))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.botao_cadastro = QtWidgets.QPushButton(self.frame)
        self.botao_cadastro.setGeometry(QtCore.QRect(50, 50, 81, 31))
        self.botao_cadastro.setStyleSheet("QPushButton{\n"
"    color: rgb(0, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"border-radius: 10px 10px 20px 20px;\n"
"    background-color: rgb(0, 170, 255);\n"
"}\n"
"QPushButton:hover{\n"
"border-radius: 10px 10px 20px 20px;\n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"")
        self.botao_cadastro.setObjectName("botao_cadastro")
        self.botao_acessar_conta = QtWidgets.QPushButton(self.frame)
        self.botao_acessar_conta.setGeometry(QtCore.QRect(50, 130, 81, 31))
        self.botao_acessar_conta.setStyleSheet("QPushButton{\n"
"    color: rgb(0, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"border-radius: 10px 10px 20px 20px;\n"
"    background-color: rgb(0, 170, 255);\n"
"}\n"
"QPushButton:hover{\n"
"border-radius: 10px 10px 20px 20px;\n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"")
        self.botao_acessar_conta.setObjectName("botao_acessar_conta")
        self.botao_remedios = QtWidgets.QPushButton(self.frame)
        self.botao_remedios.setGeometry(QtCore.QRect(50, 220, 81, 31))
        self.botao_remedios.setStyleSheet("QPushButton{\n"
"    color: rgb(0, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"border-radius: 10px 10px 20px 20px;\n"
"    background-color: rgb(0, 170, 255);\n"
"}\n"
"QPushButton:hover{\n"
"border-radius: 10px 10px 20px 20px;\n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"")
        self.botao_remedios.setObjectName("botao_remedios")
        self.botao_carrinho = QtWidgets.QPushButton(self.frame)
        self.botao_carrinho.setGeometry(QtCore.QRect(50, 300, 81, 31))
        self.botao_carrinho.setStyleSheet("QPushButton{\n"
"    color: rgb(0, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"border-radius: 10px 10px 20px 20px;\n"
"    background-color: rgb(0, 170, 255);\n"
"}\n"
"QPushButton:hover{\n"
"border-radius: 10px 10px 20px 20px;\n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"")
        self.botao_carrinho.setObjectName("botao_carrinho")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(189, -1, 431, 441))
        self.frame_2.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(10, 20, 381, 51))
        self.label_3.setStyleSheet("\n"
"font: 87 20pt \"Arial Black\";\n"
"")
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(100, 160, 231, 161))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:\\Users\\joabe\\OneDrive\\Área de Trabalho\\Farmácia_Projeto\\Imagens/farmacia.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(340, 20, 61, 51))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("C:\\Users\\joabe\\OneDrive\\Área de Trabalho\\Farmácia_Projeto\\Imagens/farmacia (1).png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        Janela_Principal.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Janela_Principal)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 617, 21))
        self.menubar.setObjectName("menubar")
        Janela_Principal.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Janela_Principal)
        self.statusbar.setObjectName("statusbar")
        Janela_Principal.setStatusBar(self.statusbar)

        self.retranslateUi(Janela_Principal)
        QtCore.QMetaObject.connectSlotsByName(Janela_Principal)

    def retranslateUi(self, Janela_Principal):
        _translate = QtCore.QCoreApplication.translate
        Janela_Principal.setWindowTitle(_translate("Janela_Principal", "MainWindow"))
        self.botao_cadastro.setText(_translate("Janela_Principal", "Cadastrar"))
        self.botao_acessar_conta.setText(_translate("Janela_Principal", "Remover"))
        self.botao_remedios.setText(_translate("Janela_Principal", "Procurar"))
        self.botao_carrinho.setText(_translate("Janela_Principal", "Sair"))
        self.label_3.setText(_translate("Janela_Principal", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">Farmácia Popular</span></p></body></html>"))
        self.botao_cadastro.clicked.connect(self.abrir_tela_cadastro)
        self.botao_remedios.clicked.connect(self.abrir_tela_procurar)
        self.botao_acessar_conta.clicked.connect(self.abrir_tela_excluir)
        self.botao_carrinho.clicked.connect(Janela_Principal.close)

    def abrir_tela_cadastro(self):
        from tela_cadastro import Ui_Form
        self.aba = QtWidgets.QWidget()
        self.abrir = Ui_Form()
        self.abrir.setupUi(self.aba, self.remedios)
        self.aba.show()

    def abrir_tela_procurar(self):
        from tela_procurar import Ui_Setup
        self.aba = QtWidgets.QWidget()
        self.abrir = Ui_Setup()
        self.abrir.setupUi(self.aba, self.remedios)
        self.aba.show()

    def abrir_tela_excluir(self):
        from tela_excluir import Ui_Test
        self.aba = QtWidgets.QWidget()
        self.abrir = Ui_Test()
        self.abrir.setupUi(self.aba, self.remedios)
        self.aba.show()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    remedios = []

    Janela_Principal = QtWidgets.QMainWindow()
    ui = Ui_Janela_Principal()
    ui.setupUi(Janela_Principal, remedios)
    Janela_Principal.show()
    sys.exit(app.exec_())
