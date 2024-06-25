def escadaria(n):
    for i in range(1, n + 1):
        linha = ' ' * (n - i) + '#' * i
        print(linha)

# Pedir ao usuário para inserir o número de degraus
n = int(input("Digite o número de degraus: "))

# Chamar a função escadaria com o valor fornecido pelo usuário
escadaria(n)
