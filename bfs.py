def bfs(graph,s):
    Q = [s] #Initialize a queue
    visited = set([s]) #visited set keeps track of which nodes have been seen
    parent = {s:None}
    level = {s:0}
    while Q != []:
        u = Q.pop(0) #take next node u from queue
        for v in graph[u]: # explore all neighbor nodes v of node u
            if v not in visited: #only consider neighbors that haven't been seen yet
                Q.append(v)
                visited.add(v)
                parent[v] = u
                level[v] = level[u]+1
    return level