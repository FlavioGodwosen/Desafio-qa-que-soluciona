def countingValleys(path):
    valleys = 0
    altitude = 0
    in_valley = False

    for step in path:
        if step == 'U':
            altitude += 1
        elif step == 'D':
            altitude -= 1
        
        #Verifique se estamos entrando em um vale
        if altitude < 0 and not in_valley:
            in_valley = True
        
        # Verifique se estamos saindo de um vale
        if altitude == 0 and in_valley:
            valleys += 1
            in_valley = False

    return valleys

# Pedir ao usuário para digitar o caminho
path = input("Digite o caminho (ex: 'DDUUDDUDUUUD'): ")
resultado = countingValleys(path)
print(f"Número de vales: {resultado}")

