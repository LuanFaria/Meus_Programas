# By:Luan Faria
from random import randint
import re

def gerar_cpf():
    soma_total = 0
    contador = 1
    gerar = 1
    cpf_gerado = list()
    for g in range(0, gerar):
        cpf_gerado.clear()
        cpf_gerado = [randint(1, 3)]
        for c in range(0, 8):
            numero_gerado = randint(0, 9)
            cpf_gerado.append(numero_gerado)
        a = 11
        for c1 in range(0, 2):
            for v in cpf_gerado:
                a -= 1
                soma = v * a
                soma_total += soma
            digito = 11 - (soma_total % 11)
            a = 12
            soma = soma_total = 0
            if digito > 9:
                cpf_gerado.append(0)
            else:
                cpf_gerado.append(digito)

        # Convertendo lista para string e tratando para remover tudo que não seja numeros de 0 - 9
        cpf_final = str(cpf_gerado)
        cpf_final = re.sub(r'[^0-9]', '', cpf_final)
        return cpf_final

if __name__ == '__main__':
    print(gerar_cpf())
