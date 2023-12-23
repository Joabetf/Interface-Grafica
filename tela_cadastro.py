from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form, remedios):
        self.remedios = remedios
        Form.setObjectName("Form")
        Form.resize(593, 466)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 601, 101))
        self.frame.setStyleSheet("background-color: rgb(255, 108, 110);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(160, 30, 301, 41))
        self.label_8.setStyleSheet("font: 87 20pt \"Arial Black\";")
        self.label_8.setObjectName("label_8")
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(0, 100, 591, 371))
        self.frame_2.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_nome = QtWidgets.QLabel(self.frame_2)
        self.label_nome.setGeometry(QtCore.QRect(100, 30, 71, 21))
        self.label_nome.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.label_nome.setObjectName("label_nome")
        self.label_validade = QtWidgets.QLabel(self.frame_2)
        self.label_validade.setGeometry(QtCore.QRect(100, 80, 81, 21))
        self.label_validade.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.label_validade.setObjectName("label_validade")
        self.label_prescricao = QtWidgets.QLabel(self.frame_2)
        self.label_prescricao.setGeometry(QtCore.QRect(100, 130, 91, 21))
        self.label_prescricao.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.label_prescricao.setObjectName("label_prescricao")
        self.label_tipo = QtWidgets.QLabel(self.frame_2)
        self.label_tipo.setGeometry(QtCore.QRect(100, 180, 81, 21))
        self.label_tipo.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.label_tipo.setObjectName("label_tipo")
        self.lineEdit_nome = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_nome.setGeometry(QtCore.QRect(230, 30, 191, 21))
        self.lineEdit_nome.setStyleSheet("QLineEdit{\n"
"border-radius: 10px 10px 20px 20px;\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.lineEdit_nome.setObjectName("lineEdit_nome")
        self.lineEdit_validade = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_validade.setGeometry(QtCore.QRect(230, 80, 191, 21))
        self.lineEdit_validade.setStyleSheet("QLineEdit{\n"
"border-radius: 10px 10px 20px 20px;\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.lineEdit_validade.setObjectName("lineEdit_validade")
        self.pushButton_cadastrar = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_cadastrar.setGeometry(QtCore.QRect(170, 280, 75, 23))
        self.pushButton_cadastrar.setStyleSheet("QPushButton{\n"
"border-radius: 10px 10px 20px 20px;\n"
"background-color: rgb(255, 175, 38);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border-radius: 10px 10px 20px 20px;\n"
"background-color: rgb(170, 169, 137);\n"
"}")
        self.pushButton_cadastrar.setObjectName("pushButton_cadastrar")
        self.pushButton_voltar = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_voltar.setGeometry(QtCore.QRect(320, 280, 75, 23))
        self.pushButton_voltar.setStyleSheet("QPushButton{\n"
"border-radius: 10px 10px 20px 20px;\n"
"background-color: rgb(255, 175, 38);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border-radius: 10px 10px 20px 20px;\n"
"background-color: rgb(170, 169, 137);\n"
"}")
        self.pushButton_voltar.setObjectName("pushButton_voltar")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(460, 90, 91, 91))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:\\Users\\joabe\\OneDrive\\Área de Trabalho\\Farmácia_Projeto\\../../../.designer/backup/Imagens/drogas.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.comboBox_tipo = QtWidgets.QComboBox(self.frame_2)
        self.comboBox_tipo.setGeometry(QtCore.QRect(230, 180, 201, 22))
        self.comboBox_tipo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_tipo.setObjectName("comboBox_tipo")
        self.comboBox_tipo.addItem("")
        self.comboBox_tipo.addItem("")
        self.comboBox_tipo.addItem("")
        self.comboBox_tipo.addItem("")
        self.comboBox_prescricao = QtWidgets.QComboBox(self.frame_2)
        self.comboBox_prescricao.setGeometry(QtCore.QRect(230, 130, 201, 22))
        self.comboBox_prescricao.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_prescricao.setObjectName("comboBox_prescricao")
        self.comboBox_prescricao.addItem("")
        self.comboBox_prescricao.addItem("")
        self.comboBox_prescricao.addItem("")
        self.comboBox_prescricao.addItem("")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_8.setText(_translate("Form", "Realizar Cadastro"))
        self.label_nome.setText(_translate("Form", "Nome:"))
        self.label_validade.setText(_translate("Form", "Validade:"))
        self.label_prescricao.setText(_translate("Form", "Prescrição:"))
        self.label_tipo.setText(_translate("Form", "Tipo:"))
        self.pushButton_cadastrar.setText(_translate("Form", "Cadastrar"))
        self.pushButton_voltar.setText(_translate("Form", "Voltar"))
        self.comboBox_tipo.setItemText(0, _translate("Form", "Analgésico "))
        self.comboBox_tipo.setItemText(1, _translate("Form", "Antibiótico"))
        self.comboBox_tipo.setItemText(2, _translate("Form", "Anti-Inflamatório"))
        self.comboBox_tipo.setItemText(3, _translate("Form", "Outro"))
        self.comboBox_prescricao.setItemText(0, _translate("Form", "Medicamentos Isentos de Prescrição (MIP)"))
        self.comboBox_prescricao.setItemText(1, _translate("Form", "Medicamentos de Venda Sob Prescrição"))
        self.comboBox_prescricao.setItemText(2, _translate("Form", "Sem retenção de receita"))
        self.comboBox_prescricao.setItemText(3, _translate("Form", "Com retenção de receita"))
        self.pushButton_cadastrar.clicked.connect(self.cadastrar_remedio)
        self.pushButton_voltar.clicked.connect(Form.close)

    def cadastrar_remedio(self):
        nome = self.lineEdit_nome.text()
        validade = self.lineEdit_validade.text()
        prescricao = self.comboBox_prescricao.currentText()
        tipo = self.comboBox_tipo.currentText()

        novo_remedio = [nome, validade, prescricao, tipo]

        self.remedios.append(novo_remedio)

        QtWidgets.QMessageBox.information(None, "Cadastro", "Remédio Cadastrado com sucesso!")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
