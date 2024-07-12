Utilizamos um dicionário num_to_words para mapear números para suas representações em palavras.

Para diferentes intervalos de minutos, aplicamos as convenções especificadas:

Se m == 0, a hora é exatamente a hora cheia.
Se m == 15, m == 30 ou m == 45, utilizamos as palavras especiais para "quarter" e "half".
Se m < 30, utilizamos "past" para representar os minutos após a hora.
Se m > 30, utilizamos "to" para representar os minutos faltando para a próxima hora.
A função ajusta a próxima hora corretamente quando m está no intervalo de 31 a 59 minutos.