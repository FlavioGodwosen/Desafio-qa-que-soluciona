Inicialização:

Começamos com zero vales, altitude no nível do mar, e in_valley como False.

Para cada passo:

Se o passo for 'U' (subida), incrementamos a altitude.
Se o passo for 'D' (descida), decrementamos a altitude.
Verificamos se entramos em um vale (altitude < 0 e not in_valley).
Verificamos se saímos de um vale (altitude == 0 e in_valley), e incrementamos valleys se for o caso.

Testes executados:


Teste 1:
Entrada: path = "DDUUDDUDUUUD"
Saída Esperada: 2

Teste 2:
Entrada: path = "UDUUUDUDDD"
Saída Esperada: 0

Teste 3:
Entrada: path = 'DUDUDUDUDUDUDU" 
Saída Esperada: 7

Teste 4:
Entrada: path = 'DDUUUUDDDUUUDDDU" 
Saída Esperada: 3