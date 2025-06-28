# Lista de puzzles prontos (3x3, 4x4, 5x5)
puzzles = [
    # 3x3
    {
        "nome": "3x3 - Puzzle 1",
        "inicio": [1, 2, 3, 4, 0, 5, 7, 8, 6],
        "objetivo": [1, 2, 3, 4, 5, 6, 7, 8, 0]
    },
    {
        "nome": "3x3 - Puzzle 2",
        "inicio": [1, 2, 3, 4, 5, 6, 0, 7, 8],
        "objetivo": [1, 2, 3, 4, 5, 6, 7, 8, 0]
    },
    # 4x4
    {
        "nome": "4x4 - Puzzle 1",
        "inicio": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0, 15],
        "objetivo": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]
    },
    {
        "nome": "4x4 - Puzzle 2",
        "inicio": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 0, 13, 14, 15],
        "objetivo": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]
    },
    # 5x5
    {
        "nome": "5x5 - Puzzle 1",
        "inicio": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 0, 24],
        "objetivo": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 0]
    },
    {
        "nome": "5x5 - Puzzle 2",
        "inicio": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 0, 23, 24],
        "objetivo": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 0]
    }
]

def escolher_puzzle_pronto(tamanho):
    """
    Mostra apenas os puzzles do tamanho escolhido.
    """
    puzzles_filtrados = [p for p in puzzles if len(p['inicio']) == tamanho * tamanho]
    if not puzzles_filtrados:
        print("Não há puzzles prontos para esse tamanho.")
        return None, None
    print("\nPuzzles disponíveis:")
    for idx, puzzle in enumerate(puzzles_filtrados):
        print(f"{idx+1}. {puzzle['nome']} - Inicial: {puzzle['inicio']} | Objetivo: {puzzle['objetivo']}")
    escolha = int(input("Escolha o número do puzzle: ")) - 1
    return puzzles_filtrados[escolha]['inicio'], puzzles_filtrados[escolha]['objetivo']