dia_semana = ('Dom', 'Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sab') # isso é uma tupla ela é imutavel

dia = int(input('Digite um número de 1 a 7: '))

nomeDia = 'não Definido!'

match dia:
    case 1:
        nomeDia = dia_semana[0]
    case 2:
        nomeDia = dia_semana[1]
    case _:
        print('valor errado')
print(f'dia da semana é {nomeDia}')