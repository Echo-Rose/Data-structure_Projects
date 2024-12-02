from queue import Queue

# 깊이 우선 탐색(DFS) - 인접행렬 방식 (DFS.py)
def DFS(vtx, adj, s, visited):
    print(vtx[s], end=' ')
    visited[s] = True
    for v in range(len(vtx)):
        if adj[s][v] != 0:
            if not visited[v]:
                DFS(vtx, adj, v, visited)

# 너비 우선 탐색(BFS) - 인접 리스트 방식 (BFS.py)
def BFS_AL(vtx, aList, s):
    n = len(vtx)
    visited = [False] * n
    Q = Queue()
    Q.put(s)
    visited[s] = True
    while not Q.empty():
        s = Q.get()
        print(vtx[s], end=' ')
        for v in aList[vtx[s]]:
            if not visited[vertex_index[v]]:
                Q.put(vertex_index[v])
                visited[vertex_index[v]] = True


# 연결성분 검사 (CC_DFS.py)
def find_connected_component(vtx, adj):
    n = len(vtx)
    visited = [False] * n
    groups = []
    for v in range(n):
        if not visited[v]:
            color = bfs_cc(vtx, adj, v, visited)
            groups.append(color)
    return groups

def bfs_cc(vtx, adj, s, visited):
    group = [s]
    Q = Queue()
    Q.put(s)
    visited[s] = True
    while not Q.empty():
        s = Q.get()
        for v in range(len(vtx)):
            if not visited[v] and adj[s][v] != 0:
                Q.put(v)
                visited[v] = True
                group.append(v)
    return group


# DFS를 이용한 신장 트리(ST_DFS.py)
def ST_DFS(vtx, adj, s, visited):
    visited[s] = True
    for v in range(len(vtx)):
        if adj[s][v] != 0:
            if not visited[v]:
                print("(", vtx[s], vtx[v], ")", end=' ')
                ST_DFS(vtx, adj, v, visited)

# 그래프의 vertex와 edge 정보를 차례대로 입력 받아 리스트로 표현하시오.
vertex_input = input("vertex : ")
edge_input = input("edge : ")

vertex = vertex_input.split(', ')
edges = [tuple(edge.split('-')) for edge in edge_input.split(', ')]

# 입력받은 그래프의 adjacent vertex 리스트는 key를 사용하여 표현하시오.
adjList = {v: [] for v in vertex}
for (v1, v2) in edges:
    adjList[v1].append(v2)
    adjList[v2].append(v1)
n = len(vertex)
vertex_index = {vertex[i]: i for i in range(n)}
adjMat = [[0] * n for _ in range(n)]
for (v1, v2) in edges:
    i, j = vertex_index[v1], vertex_index[v2]
    adjMat[i][j] = adjMat[j][i] = 1

#depth first search와 breadth first search 한 결과를 출력하시오.
print('DFS : ', end="")
DFS(vertex, adjMat, 0, [False] * len(vertex))
print()
print('BFS : ', end="")
BFS_AL(vertex, adjList, 0)
print()

# connected component를 구해서 결과를 BFS 로 출력하시오.
colorGroup = find_connected_component(vertex, adjMat)
print("Number of connected components =", len(colorGroup))
for idx, group in enumerate(colorGroup, start=1):
    nodes = [vertex[i] for i in group]
    print(f"Connected component {idx} : {', '.join(nodes)}")

# spanning tree를 구해서 A vertex를 기준으로 tree를 구성하는 edge 들을 차례로 출력하시오.
print('spanning tree(DFS) : ', end="")
ST_DFS(vertex, adjMat, 0, [False] * len(vertex))
print()

# vertex 예시 A, B, C, D, E, F, G, H
# edge 예시 A-B, A-C, B-D, C-D, C-E, D-F, E-H, E-G, G-H