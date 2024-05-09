""" with open('ArquivoParaTeste.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write('Texto alterado para teste') """


with open('./arquivos pra testes/testeArquivo', 'r', encoding='utf-8') as arquivo:
    print(arquivo.read(), end='')


""" with open('ArquivoParaTeste.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')  """

