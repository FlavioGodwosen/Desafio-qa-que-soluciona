def mediana(counts, d):
    """
    Função auxiliar para encontrar a mediana a partir do array de contagens.
    """
    count = 0
    posicao_mediana1 = d // 2
    posicao_mediana2 = posicao_mediana1 + 1 if d % 2 == 0 else posicao_mediana1
    
    mediana1 = 0
    mediana2 = 0
    
    for i, c in enumerate(counts):
        count += c
        if count >= posicao_mediana1 and mediana1 == 0:
            mediana1 = i
        if count >= posicao_mediana2:
            mediana2 = i
            break
            
    if d % 2 == 0:
        return (mediana1 + mediana2) / 2
    else:
        return mediana2

def notificacoesDeAtividade(expenditure, d):
    notifications = 0
    counts = [0] * 201  # As restrições do problema limitam os gastos ao intervalo 0-200.
    
    # Inicializa o array de contagens com os primeiros `d` dias
    for i in range(d):
        counts[expenditure[i]] += 1
    
    for i in range(d, len(expenditure)):
        # Encontra a mediana dos últimos `d` dias
        med = mediana(counts, d)
        
        # Verifica se o gasto de hoje é pelo menos duas vezes a mediana
        if expenditure[i] >= 2 * med:
            notifications += 1
        
        # Atualiza as contagens para a janela deslizante
        counts[expenditure[i]] += 1
        counts[expenditure[i - d]] -= 1
    
    return notifications

# Teste 

print(notificacoesDeAtividade([2, 3, 4, 2, 3, 6, 8, 4, 5], 5))
print(notificacoesDeAtividade([1, 2, 3, 4, 4], 4))
print(notificacoesDeAtividade([10, 20, 30, 40, 50, 60, 70, 80, 90], 5))
print(notificacoesDeAtividade([1, 2, 100, 2, 2, 2, 2, 2], 4))