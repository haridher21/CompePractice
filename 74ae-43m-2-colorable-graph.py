def twoColorable(edges):
    # Feels optimal
    n = len(edges)
    visited = [False for _ in range(n)]
    stack = {}
    for i in range(n): # O(N)
        if visited[i]:
            continue
        if dfs(i, visited, stack, edges, None):
            return False
    return True

def dfs(i, visited, stack, edges, prev):
    visited[i] = True
    stack[i] = prev
    for vertice in edges[i]:
        if vertice == i:
            return True
        if vertice != i and vertice in stack:
            if is_cycle_odd(stack, vertice, i):
                return True
        if visited[vertice]:
            continue
        if dfs(vertice, visited, stack, edges, i):
            return True
    del stack[i]

def is_cycle_odd(stack, vertice, prev):
    count = 2
    while stack[prev] and stack[prev] != vertice:
        prev = stack[prev]
        count += 1
    return True if count % 2 else False
    

    
# I incorrectly read the question, but say the next line was the case, then the solution below works
# Since number of edges equal number of vertices, this means
# only a single cycle will be present. If its even, its 2-colorable, else no.
# So either all nodes have 2 edges, or some will have 1 and equivalent extra
# for some other node/s.
def twoColorable_v2(edges):
    n, cycle, not_in_cycle = len(edges), 0, 0
    for i in range(n):
        if len(edges[i]) != 1:
            cycle += 1
        else:
            not_in_cycle += 1
    if not_in_cycle == n - 1: # Self loop exists
        return False
    return False if cycle % 2 else True
        
