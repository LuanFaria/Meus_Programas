# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'youtube.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(342, 365)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bt_mp4 = QtWidgets.QPushButton(self.centralwidget)
        self.bt_mp4.setGeometry(QtCore.QRect(220, 160, 111, 51))
        self.bt_mp4.setObjectName("bt_mp4")
        self.bt_mp3 = QtWidgets.QPushButton(self.centralwidget)
        self.bt_mp3.setGeometry(QtCore.QRect(100, 160, 111, 51))
        self.bt_mp3.setObjectName("bt_mp3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 120, 121, 20))
        self.label_2.setObjectName("label_2")
        self.input = QtWidgets.QLineEdit(self.centralwidget)
        self.input.setGeometry(QtCore.QRect(100, 120, 231, 25))
        self.input.setObjectName("input")
        self.titulo = QtWidgets.QLineEdit(self.centralwidget)
        self.titulo.setGeometry(QtCore.QRect(80, 20, 201, 71))
        self.titulo.setCursorPosition(17)
        self.titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.titulo.setReadOnly(True)
        self.titulo.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.titulo.setClearButtonEnabled(False)
        self.titulo.setObjectName("titulo")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(10, 230, 321, 111))
        self.listView.setObjectName("listView")
        self.download_andamento = QtWidgets.QLabel(self.centralwidget)
        self.download_andamento.setGeometry(QtCore.QRect(20, 240, 391, 21))
        self.download_andamento.setObjectName("download_andamento")
        self.resultado = QtWidgets.QLabel(self.centralwidget)
        self.resultado.setGeometry(QtCore.QRect(20, 280, 391, 21))
        self.resultado.setObjectName("resultado")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", " "))
        self.bt_mp4.setText(_translate("MainWindow", "MP4"))
        self.bt_mp3.setText(_translate("MainWindow", "MP3"))
        self.label_2.setText(_translate("MainWindow", "Insira o Link:"))
        self.titulo.setText(_translate("MainWindow", "Youtube Download "))
        self.download_andamento.setText(_translate("MainWindow", "TextLabel"))
        self.resultado.setText(_translate("MainWindow", "TextLabel"))