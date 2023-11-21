graph ={
        'A':{'B','G'},
        'B':{'A','C','J','G'},
        'C':{'B','D','E'},
        'D':{'C','E','F'},
        'E':{'C','D','F','H','I'},
        'F':{'D','E','I'},
        'G':{'A', 'B', 'H'},
        'H':{'E','G','I', 'J'},
        'I':{'H', 'E', 'F'},
        'J':{'B', 'H'}
    }
visitados = set()
def dfs(visitados, grafo, origem, grau):
    if origem not in visitados:
        profundidae = grau
        print(f'Profundidade:{profundidae}  Nó: {origem}')
        visitados.add(origem)
        profundidae+=1
        for vizinho in grafo[origem]:
          dfs(visitados, grafo, vizinho, profundidae)

dfs(visitados,graph,'J',0)