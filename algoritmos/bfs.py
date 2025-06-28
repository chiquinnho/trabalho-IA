# algoritmos/bfs.py

import time
from collections import deque
from algoritmos.busca_utils import generate_valid_moves, make_move, reconstruct_path

def bfs(estado_inicial, estado_objetivo):
    inicio = time.time()
    tamanho = int(len(estado_inicial) ** 0.5)
    visitados = set()
    fila = deque()
    fila.append((estado_inicial, []))
    nos_expandidos = 0

    while fila:
        estado_atual, caminho = fila.popleft()
        nos_expandidos += 1

        if estado_atual == estado_objetivo:
            fim = time.time()
            return (reconstruct_path(caminho + [estado_atual]), fim - inicio, nos_expandidos, len(caminho))

        visitados.add(tuple(estado_atual))
        for destino in generate_valid_moves(estado_atual, tamanho):
            novo_estado = make_move(estado_atual, destino)
            if tuple(novo_estado) not in visitados:
                fila.append((novo_estado, caminho + [estado_atual]))

    fim = time.time()
    return None
