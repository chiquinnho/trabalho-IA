# n-puzzle README.md

# N-Puzzle Solver

Este projeto implementa uma solução para o problema do n-puzzle (8, 15 e 24 peças) utilizando diversos algoritmos de busca, tanto sem informação (BFS, DFS, IDS) quanto com informação (A*, Gulosa). O objetivo é encontrar a solução do quebra-cabeça de forma eficiente e visualizá-la.

## Estrutura do Projeto

O projeto é organizado da seguinte forma:

```
n-puzzle/
├── algoritmos/          # Implementações dos algoritmos de busca
│   ├── bfs.py          # Busca em Largura
│   ├── dfs.py          # Busca em Profundidade
│   ├── ids.py          # Aprofundamento Iterativo
│   ├── astar.py        # Algoritmo A*
│   ├── gulosa.py       # Algoritmo Guloso
│   ├── heuristicas.py   # Funções heurísticas
│   └── busca_utils.py   # Funções utilitárias
│
├── testes/             # Scripts de teste para cada tipo de puzzle
│   ├── exemplo_8_puzzle.py
│   ├── exemplo_15_puzzle.py
│   └── exemplo_24_puzzle.py
│
├── graficos/           # Geração de gráficos comparativos
│   ├── gerar_graficos.py
│   ├── resultados.json
│   └── imagens/        # Gráficos exportados
│
├── relatorio/          # Relatório do projeto
│   ├── relatorio.md
│   ├── tabelas.csv
│   └── imagens/        # Gráficos utilizados no relatório
│
├── video/              # Roteiro para apresentação
│   └── roteiro_apresentacao.md
│
├── README.md           # Documentação do projeto
└── main.py             # Menu interativo para execução
```

## Como Instalar

1. Clone o repositório:
   ```
   git clone <URL_DO_REPOSITORIO>
   cd n-puzzle
   ```

2. Instale as dependências necessárias (se houver).

## Como Rodar

Para executar o projeto, utilize o seguinte comando:

```
python main.py
```

Siga as instruções no menu interativo para escolher o tipo de puzzle e o algoritmo desejado.

## Algoritmos Implementados

- **Busca em Largura (BFS)**
- **Busca em Profundidade (DFS)**
- **Aprofundamento Iterativo (IDS)**
- **Algoritmo A*** (com heurísticas)
- **Algoritmo Guloso** (com heurísticas)

## Geração de Gráficos

Os gráficos comparativos podem ser gerados executando o script `gerar_graficos.py` na pasta `graficos/`. Os resultados são armazenados em `resultados.json`.

## Como Rodar os Testes

Os testes para cada tipo de puzzle podem ser executados individualmente. Por exemplo, para o 8-puzzle, execute:

```
python testes/exemplo_8_puzzle.py
```

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

## Licença

Este projeto está licenciado sob a MIT License. Veja o arquivo LICENSE para mais detalhes.