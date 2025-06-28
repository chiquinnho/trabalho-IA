# algoritmos/astar.py

import time
import heapq
from algoritmos.busca_utils import generate_valid_moves, make_move, reconstruct_path

def astar(estado_inicial, estado_objetivo, heuristica):
    inicio = time.time()
    tamanho = int(len(estado_inicial) ** 0.5)
    visitados = set()
    heap = []
    heapq.heappush(heap, (heuristica(estado_inicial, estado_objetivo), 0, estado_inicial, []))
    nos_expandidos = 0

    while heap:
        f, g, estado_atual, caminho = heapq.heappop(heap)
        nos_expandidos += 1

        if estado_atual == estado_objetivo:
            fim = time.time()
            return (reconstruct_path(caminho + [estado_atual]), fim - inicio, nos_expandidos, len(caminho))

        visitados.add(tuple(estado_atual))

        for destino in generate_valid_moves(estado_atual, tamanho):
            novo_estado = make_move(estado_atual, destino)
            if tuple(novo_estado) not in visitados:
                novo_g = g + 1
                f = novo_g + heuristica(novo_estado, estado_objetivo)
                heapq.heappush(heap, (f, novo_g, novo_estado, caminho + [estado_atual]))

    fim = time.time()
    return None
