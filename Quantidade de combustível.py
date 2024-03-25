"""
15. Faça um algoritmo que calcule a quantidade de litros de combustível gasta em 
uma viagem, utilizando um automóvel que faz 12Km por litro. Para obter o 
cálculo, o usuário deve fornecer o tempo gasto na viagem e a velocidade média 
durante ela. Desta forma, será possível obter a distância percorrida com a 
fórmula DISTANCIA = TEMPO * VELOCIDADE. Tendo o valor da distância, 
basta calcular a quantidade de litros de combustível utilizada na viagem com a 
fórmula: LITROS_USADOS = DISTANCIA / 12. O programa deve apresentar os 
valores da velocidade média, tempo gasto na viagem, a distância percorrida e a 5
quantidade de litros utilizada na viagem. 
"""

tempoDeViagem = int(input('Digite o tempo da viagem: '))
velocidadeMedia = float(input('Digite a veloicdade média da viagem: ')) 
distancia = tempoDeViagem * velocidadeMedia
litros_usados = distancia / 12

print(f'A velocidade média foi {velocidadeMedia:.0f}Km/h, o tempo gasto foi {tempoDeViagem}h, a distância pecorrida foi {distancia:.0f}Km e a quantidade de combustível utilizada foi {litros_usados:.2f}L')