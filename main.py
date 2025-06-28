from algoritmos.bfs import bfs
from algoritmos.dfs import dfs
from algoritmos.ids import ids
from algoritmos.astar import astar
from algoritmos.gulosa import gulosa
from algoritmos.heuristicas import pecas_fora_do_lugar, distancia_manhattan
from algoritmos.busca_utils import ler_estado_inicial, estado_objetivo, print_board
from algoritmos.puzzles import escolher_puzzle_pronto

def main():
    print("\n===== RESOLUÇÃO DO N-PUZZLE =====")
    print("Qual tipo de busca deseja realizar?")
    print("1. Busca SEM informação (não-informada)")
    print("2. Busca COM informação (informada)")
    tipo_busca = input("Digite a opção: ")

    if tipo_busca == '1':
        # Busca sem informação: só 3x3 e 4x4
        print("\nEscolha o tipo de puzzle:")
        print("1. 8-Puzzle (3x3)")
        print("2. 15-Puzzle (4x4)")
        tipo = input("Digite a opção: ")
        if tipo not in ['1', '2']:
            print("Opção inválida.")
            return
        tamanho = {'1': 3, '2': 4}[tipo]
        print("\nEscolha o algoritmo de busca:")
        print("1. BFS (Busca em Largura)")
        print("2. DFS (Busca em Profundidade)")
        print("3. IDS (Aprofundamento Iterativo)")
        algoritmo = input("Digite a opção: ")
        if algoritmo not in ['1', '2', '3']:
            print("Opção inválida.")
            return
    elif tipo_busca == '2':
        # Busca com informação: 3x3, 4x4 e 5x5
        print("\nEscolha o tipo de puzzle:")
        print("1. 8-Puzzle (3x3)")
        print("2. 15-Puzzle (4x4)")
        print("3. 24-Puzzle (5x5)")
        tipo = input("Digite a opção: ")
        if tipo not in ['1', '2', '3']:
            print("Opção inválida.")
            return
        tamanho = {'1': 3, '2': 4, '3': 5}[tipo]
        print("\nEscolha o algoritmo de busca:")
        print("1. A* (Heurística)")
        print("2. Gulosa (Heurística)")
        algoritmo = input("Digite a opção: ")
        if algoritmo not in ['1', '2']:
            print("Opção inválida.")
            return
    else:
        print("Opção inválida.")
        return

    print("\nComo deseja fornecer o estado inicial?")
    print("1. Digitar manualmente")
    print("2. Escolher de puzzles.py")
    opcao = input("Escolha a opção: ")

    if opcao == '1':
        estado_inicial = ler_estado_inicial(tamanho)
        objetivo = estado_objetivo(tamanho)
    elif opcao == '2':
        estado_inicial, objetivo = escolher_puzzle_pronto(tamanho)
        if estado_inicial is None or objetivo is None:
            print("Nenhum puzzle disponível para esse tamanho.")
            return
    else:
        print("Opção inválida.")
        return

    heuristica_func = None
    if tipo_busca == '2':
        print("\nEscolha a heurística:")
        print("1. Peças fora do lugar")
        print("2. Distância de Manhattan")
        heuristica_op = input("Digite a opção: ")
        if heuristica_op == '1':
            heuristica_func = pecas_fora_do_lugar
        elif heuristica_op == '2':
            heuristica_func = distancia_manhattan
        else:
            print("Heurística inválida.")
            return

    print("\nEstado inicial:")
    print_board(estado_inicial)
    print("Objetivo:")
    print_board(objetivo)

    print("\nExecutando algoritmo...")
    if tipo_busca == '1':
        if algoritmo == '1':
            resultado = bfs(estado_inicial, objetivo)
        elif algoritmo == '2':
            resultado = dfs(estado_inicial, objetivo)
        elif algoritmo == '3':
            resultado = ids(estado_inicial, objetivo)
    elif tipo_busca == '2':
        if algoritmo == '1':
            resultado = astar(estado_inicial, objetivo, heuristica_func)
        elif algoritmo == '2':
            resultado = gulosa(estado_inicial, objetivo, heuristica_func)

    if resultado:
        caminho, tempo, nos_expandidos, profundidade = resultado
        print("\n===== RESULTADO =====")
        print(f"Tempo de execução: {tempo:.4f} segundos")
        print(f"Nós expandidos: {nos_expandidos}")
        print(f"Profundidade da solução: {profundidade}")
        print("\nCaminho até a solução:")
        for passo in reversed(caminho):
            print_board(passo)
    else:
        print("Nenhuma solução encontrada.")

if __name__ == "__main__":
      main()