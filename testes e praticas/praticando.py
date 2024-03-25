dicionario = {
    'nome': 'jadson',
    'sobrenome':'Pereira',
    'idade': 27
}

print(dicionario['nome'])


listaNumeros = [6,42,1,8,61,6,84]
listaNumeros.sort()
print(listaNumeros)

somaTotal = sum(listaNumeros)
print(somaTotal)


frase = "jadson" 
frase.replace("jad", 'PEr')
print(frase.replace('jad', 'PER'))
print(frase.find('son'))

cont = 0
while (cont < 10):
    cont+=1
    print(cont)
    break
else:
    print(f'fim contagem {cont}')


listNums = [x*2 for x in range(10, 101)]
print(listNums)