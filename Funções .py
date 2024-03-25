def soma(A, B):
    """ print(A + B) """
    return A + B



result = 1
while (result <= 1000):
    result += soma(1, result)
    print(result)