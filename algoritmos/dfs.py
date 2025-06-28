# algoritmos/dfs.py

import time
from algoritmos.busca_utils import generate_valid_moves, make_move, reconstruct_path

def dfs(estado_inicial, estado_objetivo, limite_profundidade=30):
    inicio = time.time()
    tamanho = int(len(estado_inicial) ** 0.5)
    visitados = set()
    nos_expandidos = 0

    def dfs_recursivo(estado_atual, caminho, profundidade):
        nonlocal nos_expandidos
        if estado_atual == estado_objetivo:
            return caminho + [estado_atual]
        if profundidade > limite_profundidade:
            return None

        visitados.add(tuple(estado_atual))
        nos_expandidos += 1

        for destino in generate_valid_moves(estado_atual, tamanho):
            novo_estado = make_move(estado_atual, destino)
            if tuple(novo_estado) not in visitados:
                resultado = dfs_recursivo(novo_estado, caminho + [estado_atual], profundidade + 1)
                if resultado:
                    return resultado
        return None

    resultado = dfs_recursivo(estado_inicial, [], 0)
    fim = time.time()

    if resultado:
        return (reconstruct_path(resultado), fim - inicio, nos_expandidos, len(resultado) - 1)
    return None
