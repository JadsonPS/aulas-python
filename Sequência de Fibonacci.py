"""
    Sequência de Fibonacci
"""


valor1 = 0
valor2 = 1
fibo = 0
for i in range(14):
    print(valor1)
    fibo = valor1 + valor2
    valor1 = valor2
    valor2 = fibo
