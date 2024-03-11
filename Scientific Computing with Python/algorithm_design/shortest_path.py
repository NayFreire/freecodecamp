my_graph = {
    'A': [('B', 3), ('D', 1)], #A is linked with B by 3 units of mesure and D by 1 unit of mesure
    'B': [('A', 3), ('C', 4)], 
    'C': [('B', 4), ('D', 7)], 
    'D': [('A', 1), ('C', 7)]  
}

print(my_graph)

def shortest_path(graph, start):
    unvisited = [] #To visit all the nodes, we nee to know which ones have been visited...
    distances = {}
    for node in graph:
        unvisited.append(node) #...that's why we add then all to the unvisited list
        if node == start:
            distances[node] = 0 #the starting node has no distance, cause it's the start
        else:
            distances[node] = float('inf') #in the beginning, every node is infinitly away from the start node*/
    print(f'Unvisited: {unvisited}\nDistances: {distances}')

shortest_path(my_graph, 'A')