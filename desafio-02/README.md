Inicialização:

Começamos com zero vales, altitude no nível do mar, e in_valley como False.

Para cada passo:

Se o passo for 'U' (subida), incrementamos a altitude.
Se o passo for 'D' (descida), decrementamos a altitude.
Verificamos se entramos em um vale (altitude < 0 e not in_valley).
Verificamos se saímos de um vale (altitude == 0 e in_valley), e incrementamos valleys se for o caso.

input("Digite o caminho (ex: 'DDUUDDUDUUUD'): "): Solicita que o usuário digite a sequência de passos.

countingValleys(path): Calcula o número de vales percorridos com base na entrada do usuário.

print(f"Número de vales: {resultado}"): Imprime o resultado.
