from collections import deque

graf = {
    'Ostrava': ['Olomouc', 'Liberec'],
    'Liberec': ['Ostrava', 'Praha'],
    'Praha': ['Liberec', 'Plzeň', 'Brno', 'České Budějovice'],
    'Brno': ['Praha'],
    'Olomouc': ['Ostrava', 'Brno'],
    'České Budějovice': ['Praha', 'Plzeň'],
    'Plzeň': ['Praha', 'České Budějovice']
}

def bfs(graph, start):
    visited = set()
    res = {}
    queue = deque([(start, 0)])
    visited.add(start)
    while queue:
        vertex, dist = queue.popleft()
        for soused in graph[vertex]:
            if soused not in visited:
                visited.add(soused)
                queue.append((soused, dist+1))
                res[soused] = dist
    return res


start_mesto = 'Ostrava'
dos_mesta = bfs(graf, start_mesto)

in_order = ['Praha', 'Liberec', 'Plzeň', 'České Budějovice', 'Brno', 'Olomouc']

print(f'Z města {start_mesto} jsou dosažitelná tato města:')
for mesto in in_order:
    if mesto in dos_mesta:
        distance = dos_mesta[mesto]
        if distance == 0:
            print(f'         {mesto} je přímo spojené s městem {start_mesto}.')
        else:
            print(f'         {mesto} je dosažitelné přes {distance} měst.')
