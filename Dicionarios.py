nome_dicio = {'nome': 'jadson', 'idade': 27, 'cidade': 'Camaragibe'}
print(nome_dicio['cidade'])
print(type(nome_dicio))


""" criando dicionario usando dict() """
dicio = dict(primeiro=1, segundo=2, terceiro=3)
print(dicio)


""" criando dicionario usando a função zip() """
dicio_3 = dict(zip(['casa','carro','rua'],[23, 'ford', 'Amaral']))
print(dicio_3)



print(nome_dicio.keys())
print(nome_dicio.values())


nome_dicio['lugar'] = 'casa amarela'
print(nome_dicio)


for chave in nome_dicio:
    print(chave)