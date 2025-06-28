# algoritmos/heuristicas.py

def pecas_fora_do_lugar(estado_atual, estado_objetivo):
    """Conta quantas peças estão fora do lugar."""
    return sum(1 for i in range(len(estado_atual)) if estado_atual[i] != 0 and estado_atual[i] != estado_objetivo[i])

def distancia_manhattan(estado_atual, estado_objetivo):
    """Soma das distâncias de Manhattan para cada peça."""
    tamanho = int(len(estado_atual) ** 0.5)
    distancia = 0
    for valor in range(1, tamanho * tamanho):
        i = estado_atual.index(valor)
        j = estado_objetivo.index(valor)
        x1, y1 = divmod(i, tamanho)
        x2, y2 = divmod(j, tamanho)
        distancia += abs(x1 - x2) + abs(y1 - y2)
    return distancia
