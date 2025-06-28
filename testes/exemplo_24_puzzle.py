# testes/exemplo_24_puzzle.py

import time
from algoritmos.bfs import bfs
from algoritmos.dfs import dfs
from algoritmos.ids import ids
from algoritmos.astar import astar
from algoritmos.gulosa import gulosa
from algoritmos.heuristicas import pecas_fora_do_lugar, distancia_manhattan
from algoritmos.busca_utils import estado_objetivo

def testar_algoritmo(nome, algoritmo, estado_inicial, estado_objetivo, heuristica=None):
    print(f"\nExecutando {nome}...")
    inicio = time.time()
    if heuristica:
        resultado = algoritmo(estado_inicial, estado_objetivo, heuristica)
    else:
        resultado = algoritmo(estado_inicial, estado_objetivo)
    fim = time.time()

    if resultado:
        caminho, tempo_alg, nos, profundidade = resultado
        print(f"{nome} finalizado:")
        print(f"- Tempo: {fim - inicio:.4f}s")
        print(f"- Nós expandidos: {nos}")
        print(f"- Profundidade: {profundidade}")
        print(f"- Passos: {len(caminho)}")
    else:
        print(f"{nome} não encontrou solução.")

def main():
    estado_inicial = [1, 2, 3, 4, 5,
                      6, 7, 8, 9, 10,
                      11, 12, 13, 14, 0,
                      16, 17, 18, 19, 15,
                      21, 22, 23, 24, 20]
    objetivo = estado_objetivo(5)

    testar_algoritmo("BFS", bfs, estado_inicial, objetivo)
    testar_algoritmo("DFS", dfs, estado_inicial, objetivo)
    testar_algoritmo("IDS", ids, estado_inicial, objetivo)
    testar_algoritmo("A* (Manhattan)", astar, estado_inicial, objetivo, distancia_manhattan)
    testar_algoritmo("Gulosa (Peças Fora)", gulosa, estado_inicial, objetivo, pecas_fora_do_lugar)

if __name__ == "__main__":
    main()
