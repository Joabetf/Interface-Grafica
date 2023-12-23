from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Test(object):
    def setupUi(self, Form, remedios):
        self.remedios = remedios
        Form.setObjectName("Form")
        Form.resize(708, 341)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 891, 91))
        self.frame.setStyleSheet("background-color: rgb(255, 108, 110);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(300, 30, 321, 31))
        self.label.setStyleSheet("\n"
"font: 75 20pt \"Arial\";")
        self.label.setObjectName("label")
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(0, 90, 911, 271))
        self.frame_2.setStyleSheet("background-color: rgb(35, 255, 237);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.tableWidget_busca = QtWidgets.QTableWidget(self.frame_2)
        self.tableWidget_busca.setGeometry(QtCore.QRect(220, 70, 401, 121))
        self.tableWidget_busca.setObjectName("tableWidget_busca")
        self.tableWidget_busca.setColumnCount(4)
        self.tableWidget_busca.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        item.setFont(font)
        self.tableWidget_busca.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        item.setFont(font)
        self.tableWidget_busca.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        item.setFont(font)
        self.tableWidget_busca.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        item.setFont(font)
        self.tableWidget_busca.setHorizontalHeaderItem(3, item)
        self.pushButton_excluir = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_excluir.setGeometry(QtCore.QRect(260, 210, 75, 23))
        self.pushButton_excluir.setStyleSheet("QPushButton{\n"
"border-radius: 10px 10px 20px 20px;\n"
"background-color: rgb(255, 175, 38);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border-radius: 10px 10px 20px 20px;\n"
"background-color: rgb(170, 169, 137);\n"
"}")
        self.pushButton_excluir.setObjectName("pushButton_excluir")
        self.pushButton_voltar = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_voltar.setGeometry(QtCore.QRect(460, 210, 75, 23))
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
        self.campo_buscar = QtWidgets.QLineEdit(self.frame_2)
        self.campo_buscar.setGeometry(QtCore.QRect(240, 30, 281, 20))
        self.campo_buscar.setStyleSheet("QLineEdit{\n"
"border-radius: 10px 10px 20px 20px;\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.campo_buscar.setObjectName("campo_buscar")
        self.pushButton_buscar = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_buscar.setGeometry(QtCore.QRect(540, 30, 75, 23))
        self.pushButton_buscar.setStyleSheet("QPushButton{\n"
"border-radius: 10px 10px 20px 20px;\n"
"background-color: rgb(255, 175, 38);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border-radius: 10px 10px 20px 20px;\n"
"background-color: rgb(170, 169, 137);\n"
"}")
        self.pushButton_buscar.setObjectName("pushButton_buscar")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Consulta de Remédios"))
        item = self.tableWidget_busca.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Nome"))
        item = self.tableWidget_busca.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Validade"))
        item = self.tableWidget_busca.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Prescricao"))
        item = self.tableWidget_busca.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Tipo "))
        self.pushButton_excluir.setText(_translate("Form", "Excluir"))
        self.pushButton_voltar.setText(_translate("Form", "Voltar"))
        self.campo_buscar.setText(_translate("Form", "Digite um nome para busca..."))
        self.pushButton_buscar.setText(_translate("Form", "Buscar"))
        self.pushButton_voltar.clicked.connect(Form.close)
        self.pushButton_buscar.clicked.connect(self.realizar_busca)
        self.pushButton_excluir.clicked.connect(self.excluir_aluno)
        self.listar_remedios()

    def listar_remedios(self):
        for remedios in self.remedios:
            posicao = self.tableWidget_busca.rowCount()
            self.tableWidget_busca.insertRow(posicao)
            for indice, dado in enumerate(remedios):
                self.tableWidget_busca.setItem(posicao, indice, QtWidgets.QTableWidgetItem(str(dado)))

    def realizar_busca(self):
        remedio_busca = self.campo_buscar.text().lower()

        resultados = []

        for remedio in self.remedios:
            if remedio_busca in remedio[0].lower():
                resultados.append(
                    {'nome': remedio[0], 'idade': remedio[1], 'email': remedio[2], 'tel': remedio[3], 'curso': remedio[4]})

        self.atualizar_tabela(resultados)

    def atualizar_tabela(self, resultados):
        self.tableWidget_busca.clearContents()
        self.tableWidget_busca.setRowCount(0)

        for row, aluno in enumerate(resultados):
            self.tableWidget_busca.insertRow(row)
            self.tableWidget_busca.setItem(row, 0, QtWidgets.QTableWidgetItem(aluno['nome']))
            self.tableWidget_busca.setItem(row, 1, QtWidgets.QTableWidgetItem(aluno['idade']))
            self.tableWidget_busca.setItem(row, 2, QtWidgets.QTableWidgetItem(aluno['email']))
            self.tableWidget_busca.setItem(row, 3, QtWidgets.QTableWidgetItem(aluno['tel']))
            self.tableWidget_busca.setItem(row, 4, QtWidgets.QTableWidgetItem(aluno['curso']))

    def excluir_aluno(self):
        if not self.tableWidget_busca.selectedItems():
            QtWidgets.QMessageBox.warning(None, "Atenção", "Selecione um aluno para excluir.")
            return

        row = self.tableWidget_busca.currentRow()

        nome_remedio = self.tableWidget_busca.item(row, 0).text()

        remedio_para_excluir = None

        for remedio in self.remedios:
            if remedio[0] == nome_remedio:
                remedio_para_excluir = remedio
                break

        if remedio_para_excluir is not None:
            self.remedios.remove(remedio_para_excluir)

        self.tableWidget_busca.removeRow(row)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Test()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
