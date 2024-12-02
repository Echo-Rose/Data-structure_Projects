# 코드 11.16: Floyd 알고리즘 - 최단 경로 출력 기능 추가
INF = 9999


def printA(A):
    vsize = len(A)
    print("====================================")
    for i in range(vsize):
        for j in range(vsize):
            if (A[i][j] == INF):
                print(" INF ", end='')
            else:
                print("%4d " % A[i][j], end='')
        print("")


def shortest_path_floyd(vertex, adj):
    vsize = len(vertex)  # 정점의 개수

    A = list(adj)  # 2차원 배열(리스트의 리스트)의 복사
    for i in range(vsize):
        A[i] = list(adj[i])

    # 최단거리 역추적을 위한 이전 노드의 초기화
    P = [[-1 if adj[i][j] == INF or i == j else i for j in range(vsize)] for i in range(vsize)]

    for k in range(vsize):
        for i in range(vsize):
            for j in range(vsize):
                if A[i][k] + A[k][j] < A[i][j]:
                    A[i][j] = A[i][k] + A[k][j]
                    P[i][j] = P[k][j]  # 경로 업데이트
        printA(A)  # 진행상황 출력용

    return A, P

# 경로추적 함수
def construct_path(P, start, end):
    path = []
    if P[start][end] == -1:
        return path  # 경로가 존재하지 않음
    while end != start:
        path.insert(0, end)
        end = P[start][end]
    path.insert(0, start)
    return path


if __name__ == "__main__":
    # Shortest Path를 위한 Weighted Graph
    vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    weight = [[0, 7, INF, INF, 3, 10, INF],
              [7, 0, 4, 10, 2, 6, INF],
              [INF, 4, 0, 2, INF, INF, INF],
              [INF, 10, 2, 0, 11, 9, 4],
              [3, 2, INF, 11, 0, 13, 5],
              [10, 6, INF, 9, 13, 0, INF],
              [INF, INF, INF, 4, 5, INF, 0]]

    print("Shortest Path By Floyd's Algorithm")
    A, P = shortest_path_floyd(vertex, weight)

    # 사용자 입력에 따른 최단 경로 출력
    start_vertex = input("Start Vertex: ").strip()
    end_vertex = input("End Vertex: ").strip()

    if start_vertex in vertex and end_vertex in vertex:
        start = vertex.index(start_vertex)
        end = vertex.index(end_vertex)
        path = construct_path(P, start, end)
        if path:
            path_str = " -> ".join(vertex[i] for i in path)
            print(f"* Shortest Path: {path_str}")
            print(f"* Distance of the Shortest Path: {A[start][end]}")
        else:
            print("No path exists between the given vertices.")
    else:
        print("Invalid vertices entered.")
