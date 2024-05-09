"""
arquivo = open('meutexto.txt', 'w')
arquivo.write('Esse é meu primeiro arquivo criado com python')
arquivo.write('Ass: Jadson')
arquivo.close()
"""

arquivo = open('meutexto.txt', 'r')
print(arquivo.read())
arquivo.close()
