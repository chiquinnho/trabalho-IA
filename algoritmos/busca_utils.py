# algoritmos/busca_utils.py

import time

def print_board(state):
    """Imprime o estado atual do puzzle em formato de grade."""
    size = int(len(state) ** 0.5)
    for i in range(size):
        row = state[i * size:(i + 1) * size]
        print(" | ".join(f"{num:2}" for num in row))
    print("\n")

def ler_estado_inicial(tamanho):
    """
    Lê o estado inicial do usuário, linha por linha.
    Exemplo para 3x3:
    1 2 3
    4 0 5
    7 8 6
    """
    estado = []
    print(f"Digite o estado inicial ({tamanho} linhas, separados por espaço):")
    for _ in range(tamanho):
        linha = list(map(int, input().split()))
        if len(linha) != tamanho:
            raise ValueError("Número incorreto de elementos na linha.")
        estado.extend(linha)
    return estado

def estado_objetivo(tamanho):
    """Retorna o estado objetivo padrão para o puzzle."""
    return list(range(1, tamanho * tamanho)) + [0]

def generate_valid_moves(state, tamanho):
    """Retorna os índices para onde o zero pode se mover."""
    index = state.index(0)
    moves = []
    row, col = divmod(index, tamanho)

    if row > 0: moves.append(index - tamanho)        # cima
    if row < tamanho - 1: moves.append(index + tamanho)  # baixo
    if col > 0: moves.append(index - 1)             # esquerda
    if col < tamanho - 1: moves.append(index + 1)   # direita

    return moves

def make_move(state, destino):
    """Realiza o movimento do zero para a posição indicada e retorna o novo estado."""
    index_zero = state.index(0)
    novo_estado = state[:]
    novo_estado[index_zero], novo_estado[destino] = novo_estado[destino], novo_estado[index_zero]
    return novo_estado

def reconstruct_path(caminho):
    """Reconstrói o caminho da solução."""
    return list(reversed(caminho))
