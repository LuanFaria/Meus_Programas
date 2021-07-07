import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from interface import *



class Youtube_Download(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__(None)
        super().setupUi(self)

        # Fixar nesse tamanho
        self.setFixedSize(342, 365)










if __name__ == '__main__':
    qt = QApplication(sys.argv)
    you = Youtube_Download()
    you.show()
    qt.exec_()
