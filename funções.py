def media(valor1=1, valor2=1, valor3=1):
    return (valor1 + valor2 + valor3) / 3

""" print(media(10, 8, 6), end=" ")
print('essa foi a media') """

def multiRetor(A, B):
    return A, B


respota, valor = multiRetor('aaaskdjflaskj', 456456)
""" print(respota) """

def umaLinha(texto): return texto + " uma linha"

""" print(umaLinha('jadson')) """

def calculo_media(*args):
    soma = sum(args)
    media = soma / len(args)
    return media


def person(**kwargs):
    print(kwargs, type(kwargs))


person(nome = 'jadson', idade = 27)