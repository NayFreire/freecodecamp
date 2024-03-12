my_graph = {
    'A': [('B', 3), ('D', 1)], #A is linked with B by 3 units of mesure and D by 1 unit of mesure
    'B': [('A', 3), ('C', 4)], 
    'C': [('B', 4), ('D', 7)], 
    'D': [('A', 1), ('C', 7)]  
}

print(my_graph)

def shortest_path(graph, start, target=''):
    unvisited = list(graph)
    #To visit all the nodes, we nee to know which ones have been visited that's why we add then all to the unvisited list
    distances = {key: 0 if key == start else float('inf') for key in graph}
    ''' This commented code is the same as the dictionary comprehension user in the variable 'distances'
    for node in graph:
        unvisited.append(node) #...
        if node == start:
            distances[node] = 0 #the starting node has no distance, cause it's the start
        else:
            distances[node] = float('inf') #in the beginning, every node is infinitly away from the start node'''
    
    paths = {key: [] for key in graph}
    paths[start].append(start) #the path[start] has the start node in its list cause it is a path to itself

    while unvisited:
        current = min(unvisited, key=distances.get)
        for node, distance in graph[current]:
            if distance + distances[current] < distances[node]:
                distances[node] = distance + distances[current]
                if paths[node] and paths[node][-1] == node:
                    paths[node] = paths[current][:]
                else:
                    paths[node].extend(paths[current])
                paths[node].append(node)
        unvisited.remove(current)

    targets_to_print = [target] if target else graph
    for node in targets_to_print:
        if node == start:
            continue
        print(f'\n{start}-{node} distance: {distances[node]}\nPath: {" -> ".join(paths[node])}')
    
    return distances, paths

shortest_path(my_graph, 'A', 'C')