from itertools import product
from sys import maxint


def generate_vertices(N, M):
    return list(product(range(1, N + 1), range(1, M + 1)))


def generate_edges(V, N, M, in_boss_area):
    E = {}
    for v in V:
        E[v] = []
        x, y = v

        if in_boss_area(x, y):
            continue
        # left
        if x - 1 > 0 and not in_boss_area(x - 1, y):
            E[v].append((x - 1, y))
        # right
        if x + 1 <= N and not in_boss_area(x + 1, y):
            E[v].append((x + 1, y))
        # up
        if y - 1 > 0 and not in_boss_area(x, y - 1):
            E[v].append((x, y - 1))
        # down
        if y + 1 <= M and not in_boss_area(x, y + 1):
            E[v].append((x, y + 1))
    return E


def build_graph(N, M, X5, Y5, X6, Y6):
    def in_boss_area(x, y):
        return X5 <= x <= X6 and Y5 <= y <= Y6

    V = generate_vertices(N, M)
    E = generate_edges(V, N, M, in_boss_area)

    return V, E


def dijkstra(V, E, s):
    Q = []
    dist = {s: 0}
    prev = {}

    for v in V:
        if v != s:
            dist[v] = maxint
            prev[v] = None

        Q.append(v)

    while Q:
        u = min(Q, key=lambda v: dist[v])

        Q.remove(u)

        for v in E[u]:
            alt = dist[u] + 1

            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u

    return dist, prev


def caminoAChicas(N, M, X0, Y0, X1, Y1, X2, Y2, X3, Y3, X4, Y4, X5, Y5, X6, Y6):
    V, E = build_graph(N, M, X5, Y5, X6, Y6)
    print dijkstra(V, E, (X0, Y0))
    return ""


caminoAChicas(8, 8, 2, 1, 7, 2, 2, 7, 6, 6, 7, 7, 3, 3, 5, 4)
# print build_graph(4, 4, 2, 2, 3, 3)
(V, E) = build_graph(8, 8, 3, 3, 5, 4)
