# Their solution is still slightly better.
def cycleInGraph(edges):
    # Optimal, I'm sure, atleast timewise. Don't think I can do it iteratively
    n = len(edges)
    riplist = []
    for i in range(n):
        visited = [False for _ in range(n)]
        riplist = dfs(i, visited, [], edges, riplist)
        if type(riplist) == bool:
            return True
    return False
        
def dfs(cur, visited, path, edges, riplist):
    if visited[cur]:
        return True
    if cur in riplist:
        return riplist
    path.append(cur)
    visited[cur] = True
    for edge in edges[cur]:
        riplist = dfs(edge, visited, path, edges, riplist)
        if type(riplist) == bool:
            return True
    path.pop()
    visited[cur] = False
    riplist.append(cur)
    return riplist
    
