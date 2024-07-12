Função mediana:

Esta função calcula a mediana dos últimos d dias usando um array de contagem (counts), que armazena a frequência de cada valor de despesa.
O posicao_mediana1 e posicao_mediana2 ajudam a determinar a posição da mediana, considerando se d é par ou ímpar.

Função notificacoesDeAtividade:

Inicializa um array contagens de tamanho 201 (para acomodar despesas no intervalo de 0 a 200).
Preenche o contagens com os primeiros d dias de despesas.
Itera sobre os dias a partir do d-ésimo, calcula a mediana dos últimos d dias, verifica se a despesa do dia atual é pelo menos duas vezes a mediana e, se for, incrementa o contador de notificações.
Atualiza o array contagens removendo o valor de d dias atrás e adicionando o valor do dia atual para manter a janela deslizante.