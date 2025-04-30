# BFS Traversal of a Graph

graph={
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':[],
    'E':['F'],
    'F':[]
}

visited=[]
queue=[]

def bfs(visited,queue,node):
    
    visited.append(node)
    queue.append(node)
    
    while queue:
        s=queue.pop(0)
        print(s,end=" ")
        
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
    

print("Following is the BFS traversal")
bfs(visited,queue,'A')    


# DFS Traversal of a Graph

graph={
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':[],
    'E':['F'],
    'F':[]
}

visited=set()

def dfs(visited,graph,node):
    if node not in visited:
        print(node,end=" ")
        visited.add(node)
    
        for neighbour in graph[node]:
            dfs(visited,graph,neighbour)    

print("\nDFS traversal of graph:") 
dfs(visited,graph,'A')   