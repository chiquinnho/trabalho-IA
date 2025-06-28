# algoritmos/gerar_graficos.py

import json
import matplotlib.pyplot as plt
import os

def gerar_graficos():
    with open('graficos/resultados.json', 'r') as f:
        dados = json.load(f)

    # Agrupar resultados por tipo de puzzle
    resultados_por_tipo = {}
    for d in dados["resultados"]:
        tipo = d["tipo_puzzle"]
        if tipo not in resultados_por_tipo:
            resultados_por_tipo[tipo] = []
        resultados_por_tipo[tipo].append(d)

    if os.path.exists("graficos/imagens") and not os.path.isdir("graficos/imagens"):
        os.remove("graficos/imagens")

    os.makedirs("graficos/imagens", exist_ok=True)

    def plotar_grafico(titulo, algoritmos, dados, cor, nome_arquivo):
        plt.figure(figsize=(10, 6))
        plt.bar(algoritmos, dados, color=cor)
        plt.title(titulo)
        plt.xlabel('Algoritmos')
        plt.ylabel(titulo)
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.savefig(f'graficos/imagens/{nome_arquivo}.png')
        plt.close()

    # Para cada tipo de puzzle, gera gráficos separados
    for tipo, resultados in resultados_por_tipo.items():
        algoritmos = [r["algoritmo"] for r in resultados]
        tempos = [r["tempo_execucao"] for r in resultados]
        passos = [r["passos"] for r in resultados]
        profundidade = [r["profundidade"] for r in resultados]
        nos_expandidos = [r["nos_expandidos"] for r in resultados]

        tipo_formatado = tipo.lower().replace("-", "_")

        plotar_grafico(f"{tipo} - Tempo de Execução (s)", algoritmos, tempos, "blue", f"{tipo_formatado}_tempo")
        plotar_grafico(f"{tipo} - Número de Passos", algoritmos, passos, "green", f"{tipo_formatado}_passos")
        plotar_grafico(f"{tipo} - Profundidade da Solução", algoritmos, profundidade, "orange", f"{tipo_formatado}_profundidade")
        plotar_grafico(f"{tipo} - Nós Expandidos", algoritmos, nos_expandidos, "red", f"{tipo_formatado}_nos_expandidos")

if __name__ == "__main__":
    gerar_graficos()
