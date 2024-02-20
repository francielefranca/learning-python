# exercicio - teoria dos grafos 2023.2

# algoritmo: coloracao gulosa sequencial

def coloracao_gulosa(G, K):
    cor = {}

    for v in K:
        coloracao_vizinhos = {cor[u] for u in G[v] if u in cor}

        for color in range(len(K)):
            if color not in coloracao_vizinhos:
                cor[v] = color
                break

    return cor

#aplicando a funcao
grafo = {
    'H': ['E'],
    'E': ['H', 'L'],
    'L': ['H', 'E', 'D', 'F'],
    'D': ['E', 'L'],
    'F': ['H', 'E', 'L', 'D']
}

vertices = ['H', 'E', 'L', 'D', 'F']
cores = coloracao_gulosa(grafo, vertices)

print("Coloracao dos vértices:")
for v, c in cores.items():
    print(f"Vértice {v}: cor {c}")
