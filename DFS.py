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
visited = set()
def dfs(visited, graph, root, grau):
    if root not in visited:
        profund = grau
        print(f'Profundidade:{profund}  Nó: {root}')
        visited.add(root)
        profund+=1
        for neighbour in graph[root]:
          dfs(visited, graph, neighbour,profund)

dfs(visited,graph,'J',0)