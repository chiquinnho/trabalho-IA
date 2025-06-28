# Relatório do Projeto N-Puzzle

## Introdução

O problema do n-puzzle é um clássico problema de busca em inteligência artificial, onde o objetivo é reorganizar uma configuração inicial de peças em um tabuleiro para alcançar uma configuração final desejada. Este projeto aborda a resolução do n-puzzle para 8, 15 e 24 peças, utilizando diferentes algoritmos de busca, tanto informados quanto não informados.

## Algoritmos Implementados

### 1. Busca em Largura (BFS)
A Busca em Largura explora todos os nós em um nível antes de passar para o próximo nível. É garantido encontrar a solução mais curta, mas pode consumir muita memória.

### 2. Busca em Profundidade (DFS)
A Busca em Profundidade explora o máximo possível ao longo de um ramo antes de retroceder. Embora consuma menos memória, não garante a solução mais curta e pode ficar presa em ciclos.

### 3. Aprofundamento Iterativo (IDS)
O Aprofundamento Iterativo combina a profundidade da DFS com a completude da BFS. Ele é eficiente em termos de memória e garante encontrar a solução mais curta.

### 4. A* (A Estrela)
O algoritmo A* utiliza heurísticas para guiar a busca, permitindo encontrar soluções de forma mais eficiente. Ele combina o custo do caminho já percorrido com uma estimativa do custo restante.

### 5. Gulosa
A Busca Gulosa utiliza uma heurística para escolher o próximo nó a ser explorado, focando em minimizar o custo estimado para alcançar o objetivo. Embora rápida, não garante a solução ótima.

## Heurísticas Utilizadas

- **Distância de Manhattan**: Soma das distâncias verticais e horizontais de cada peça até sua posição correta.
- **Peças Fora do Lugar**: Conta o número de peças que estão em posições diferentes de suas posições finais.

## Resultados

Os resultados dos testes foram coletados e armazenados em um arquivo JSON, que inclui métricas como tempo de execução, número de passos, profundidade da solução e nós expandidos. Os gráficos gerados a partir desses dados são apresentados na seção de resultados.

## Comparação de Algoritmos

Os algoritmos foram comparados com base em suas eficiências em termos de tempo de execução e recursos utilizados. A tabela abaixo resume os resultados obtidos:

| Algoritmo | Tempo (s) | Passos | Profundidade | Nós Expandidos |
|-----------|-----------|--------|--------------|----------------|
| BFS       |           |        |              |                |
| DFS       |           |        |              |                |
| IDS       |           |        |              |                |
| A*       |           |        |              |                |
| Gulosa    |           |        |              |                |

## Conclusão

Os resultados demonstraram que, embora a BFS e o A* sejam mais lentos em alguns casos, eles garantem soluções ótimas. A DFS, por outro lado, pode ser mais rápida, mas não é confiável para encontrar a solução mais curta. As heurísticas utilizadas no A* e na busca gulosa mostraram-se eficazes em reduzir o tempo de busca, mas a escolha da heurística pode impactar significativamente o desempenho.

## Imagens

As imagens dos gráficos gerados a partir dos resultados estão disponíveis na pasta `imagens` dentro do diretório `relatorio`. Esses gráficos ilustram a comparação de desempenho entre os diferentes algoritmos.

## Referências

- [Artigos sobre algoritmos de busca](https://www.example.com)
- [Documentação sobre heurísticas](https://www.example.com)

Este relatório fornece uma visão geral do projeto e dos resultados obtidos, servindo como base para futuras melhorias e implementações.