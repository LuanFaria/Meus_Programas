import os

# caminho = '/home

caminho = input('Digite o caminho: ')
procurar = input('Procurar por: ')
print()


def formatar_tamanho(tamanho):

    if tamanho < 1024:
        texto = 'b'

    elif 1024 <= tamanho < 1024 ** 2:
        tamanho = tamanho / 1024
        texto = 'Kb'

    elif 1024 ** 2 <= tamanho < 1024 ** 3:
        tamanho /= 1024 ** 2
        texto = 'Mb'

    else:
        tamanho /= 1024 ** 3
        texto = 'Tb'

    return '{:.2f}{}'.format(tamanho, texto)


contador = 0

for raiz, diretorios, arquivos in os.walk(caminho):
    for arquivo in arquivos:
        if procurar in arquivo:
            try:
                contador += 1
                caminho_completo = os.path.join(raiz, arquivo)
                nome_arquivo, ext_arquivo = os.path.splitext(caminho_completo)
                tamanho = os.path.getsize(caminho_completo)

                print('Arquivo: {}'.format(arquivo))
                print('Caminho: {}'.format(caminho_completo))
                print('Extensão: {}'.format(ext_arquivo))
                print('Tamanho: {}'.format(formatar_tamanho(tamanho)))
                print('- '*30)

            except PermissionError:
                print('\033[31mSem permissão.\033[m')
            except FileExistsError:
                print('\033[31mArquivo não encontrado.\033[m')
            except:
                print('\033[31mErro desconhecido.\033[m')

print()
if contador > 1:
    print('\033[32mForam encontrados {} arquivos.'.format(contador))
elif contador == 1:
    print('\033[32mFoi encontrado apenas 1 arquivo.')
else:
    print('\033[31mNão foi encontrado nenhum arquivo com esse nome.')
