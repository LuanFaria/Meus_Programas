# By:Luan Faria
from pytube import YouTube

titulo = 'Youtube Download '
tamanho = len(titulo) + 4
print('\033[34m-' * tamanho)
print('  {}'.format(titulo))
print('-' * tamanho)
print('\033[m')
c = 0
while c != 1:
    link = input('Coloque o link aqui: ')
    yt = YouTube(link)
    print()

    n = ' '
    while n not in '12':
        n = str(input('Para baixar video aperte [1]\n'
                      'Para baixar audio aperte [2]\n'
                      '\n'
                      'Aqui: '))
        print()
    if n == '1':
        print('O video ({}) está sendo baixado...'.format(yt.title))
        video = yt.streams.first()
        video.download()
    else:
        print('O Audio ({}) ... está sendo baixado...'.format(yt.title))
        audio = yt.streams.get_audio_only()
        audio.download()

    print('\033[32mDownload com sucesso!\033[m')
    print('---------------------------------------------------------------------')
    print()

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja baixar outro Vídeo/Musica?\n'
                              '[S/N]: ')).upper()
        if continuar == 'N':
            c = 1
