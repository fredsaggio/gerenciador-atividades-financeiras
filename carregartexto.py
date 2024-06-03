def lerArquivo(arquivo):
    with open('arquivostexto/' + arquivo + '.txt', 'r', encoding='utf-8') as arquivooo:
        lerArquivo = arquivooo.read()
    return print(lerArquivo)  