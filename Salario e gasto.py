# salario e gastos

salario_mensal = input('Digite o valor do seu salário mensal: ')
salario_mensal = float(salario_mensal)

gasto_mensal = input('Digite o valor do seu gasto mensal em média: ')
gasto_mensal = float(gasto_mensal)

salario_total = salario_mensal * 12
gasto_total = gasto_mensal * 12

montante_economizado = salario_total - gasto_total
print(f'O montante que você pode economizar ao fim do ano é de {montante_economizado}')

