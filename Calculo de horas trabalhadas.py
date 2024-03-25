"""
11. Faça um algoritmo que: 
a) Obtenha o valor para a variável HT (horas trabalhadas no mês); 
b) Obtenha o valor para a variável VH (valor hora trabalhada): 
c) Obtenha o valor para a variável PD (percentual de desconto); 
d) Calcule o salário bruto => SB = HT * VH; 
e) Calcule o total de desconto => TD = (PD/100)*SB; 
f) Calcule o salário líquido => SL = SB – TD; 
g) Apresente os valores de: Horas trabalhadas, Salário Bruto, Desconto, Salário 
Liquido. 
"""

HT = int(input('Digite às horas trabalhads no mês: '))
VH = int(input('Digite o valor da hora trabalhada: '))
PD = int(input('Digite o percentual de desconto: '))

SB = HT * VH
TD = (PD/100)*SB
SL = SB - TD

print(f'Horas trabalhadas: {HT}, Salário Bruto: {SB}, Desconto: {TD}, Salário Liquido: {SL}')
