import sys
from heapq import heapify, heappush

def dijsktra(grafo, origem, dest):
    inf = sys.maxsize
    data_nos = {'A':{'custo':inf,'pred':[]},
    'B':{'custo':inf,'pred':[]},
    'C':{'custo':inf,'pred':[]},
    'D':{'custo':inf,'pred':[]},
    'E':{'custo':inf,'pred':[]},
    'F':{'custo':inf,'pred':[]},
    'G': {'custo': inf, 'pred': []},
    'H': {'custo': inf, 'pred': []},
    'I': {'custo': inf, 'pred': []},
    'J': {'custo': inf, 'pred': []}
    }

    data_nos[origem]['custo'] = 0

    nos_visitados = []
    temp = origem
    for i in range(8):
        if temp not in nos_visitados:

            nos_visitados.append(temp)
            min_heap = []
            for j in grafo[temp]:
                if j not in nos_visitados:
                    custo = data_nos[temp]['custo'] + grafo[temp][j]
                    if custo < data_nos[j]['custo']:
                        data_nos[j]['custo'] = custo
                        data_nos[j]['pred'] = data_nos[temp]['pred'] + [temp]
                    heappush(min_heap,(data_nos[j]['custo'],j))
        heapify(min_heap)
        temp = min_heap[0][1]

    custo_total = str(data_nos[dest]['custo'])
    caminho_percorrido=str(data_nos[dest]['pred'] + list(dest))
    print(f'Custo do caminho mais curto: {custo_total}')
    print(f'Caminho mais curto: {caminho_percorrido}')


if __name__ == "__main__":
    grafo = {
        'A':{'B':4,'G':7},
        'B':{'A':4,'C':9,'J':5,'G':11 },
        'C':{'B':9,'D':6,'E':2},
        'D':{'C':6,'E':10,'F':5},
        'E':{'C':2,'D':10,'F':15,'H':1,'I':12},
        'F':{'D':5,'E':15,'I':12},
        'G':{'A': 7, 'B': 11, 'H': 1},
        'H':{'E':1,'G': 1,'I':3, 'J': 5},
        'I':{'H': 3, 'E': 5, 'F':12},
        'J':{'B': 5, 'H': 5},
    }

    origem = 'A'
    destino = 'F'
    dijsktra(grafo,origem,destino)


