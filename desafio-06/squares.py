import math

def squares(a, b):
    # Encontra o menor inteiro x tal que x^2 >= a
    lower_bound = math.ceil(math.sqrt(a))
    
    # Encontra o maior inteiro x tal que x^2 <= b
    upper_bound = math.floor(math.sqrt(b))
    
    # Conta os inteiros entre lower_bound e upper_bound (inclusive)
    count = max(0, upper_bound - lower_bound + 1)
    
    return count

#Exemplo de teste
a = 3
b = 9
print(squares(3, 9))  # Output: 2 (4 e 9 são quadrados perfeitos no intervalo de 3 a 9)
