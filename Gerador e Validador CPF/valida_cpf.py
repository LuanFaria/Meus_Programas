#By:Luan Faria
import re

def validar_cpf(cpf):
    from time import sleep

    soma_total = 0
    contador = 1
    cpf_gerado = []
    cpf_final = []
    while 1:
        cpf_gerado.clear()
        cpf_final.clear()
        cpf = str(cpf)
        cpf = re.sub(r'[^0-9]', '', cpf)
        if cpf.upper() == 'S':
            break

        cpf = list(cpf)
        for c in cpf:
            cpf_final.append(int(c))
        for c in cpf:
            cpf_gerado.append(int(c))
            if len(cpf_gerado) == 9:
                break
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
        sleep(1)
        if cpf_gerado == cpf_final:
            return 'Válido'
        else:
            return 'Inválido'