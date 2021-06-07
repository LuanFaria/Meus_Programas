#!/home/luan/Documentos/Python/Meus_Programas/Gerador e Validador CPF
from gerador_cpf import gerar_cpf
from valida_cpf import validar_cpf
from PyQt5.QtWidgets import QApplication, QMainWindow
from CPF import *
import sys

class Gera_Valida(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__(None)
        super().setupUi(self)

        # Fixar nesse tamanho
        self.setFixedSize(471, 98)

        # Botões
        self.btn_gerar.clicked.connect(self.gera)
        self.btn_validar.clicked.connect(self.valida)
        self.setStyleSheet(
            '* {background: LightGrey}'  # Formatação em CSS
        )


    def valida(self):
        cpf = self.input_cpf.text()

        if validar_cpf(cpf) == 'Válido':
            self.label_retorno.setText(str(validar_cpf(cpf)))
            self.label_retorno.setStyleSheet(
                '* {background: LightGrey;color:green}'  # Formatação em CSS
            )
        else:
            self.label_retorno.setText(str(validar_cpf(cpf)))
            self.label_retorno.setStyleSheet(
                '* {background: LightGrey;color:red}'  # Formatação em CSS
            )

    def gera(self):
        cpf = str(gerar_cpf())
        self.input_cpf.setText(cpf)

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    gv = Gera_Valida()
    gv.show()
    qt.exec_()
