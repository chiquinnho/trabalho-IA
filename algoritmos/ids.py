# algoritmos/ids.py

import time
from algoritmos.busca_utils import generate_valid_moves, make_move, reconstruct_path

def ids(estado_inicial, estado_objetivo):
    inicio = time.time()
    tamanho = int(len(estado_inicial) ** 0.5)
    profundidade_max = 50
    nos_expandidos_total = 0

    def dls(estado, caminho, profundidade, limite, visitados):
        nonlocal nos_expandidos_total
        if estado == estado_objetivo:
            return caminho + [estado]
        if profundidade > limite:
            return None

        visitados.add(tuple(estado))
        nos_expandidos_total += 1

        for destino in generate_valid_moves(estado, tamanho):
            novo_estado = make_move(estado, destino)
            if tuple(novo_estado) not in visitados:
                resultado = dls(novo_estado, caminho + [estado], profundidade + 1, limite, visitados)
                if resultado:
                    return resultado
        return None

    for limite in range(profundidade_max):
        visitados = set()
        resultado = dls(estado_inicial, [], 0, limite, visitados)
        if resultado:
            fim = time.time()
            return (reconstruct_path(resultado), fim - inicio, nos_expandidos_total, len(resultado) - 1)

    fim = time.time()
    return None
