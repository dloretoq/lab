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


def initialize_single_source(V, s):
    dist, prev = {}, {}
    for v in V:
        dist[v] = maxint
        prev[v] = None
    dist[s] = 0
    return dist, prev


def dijkstra(V, E, s):
    dist, prev = initialize_single_source(V, s)
    Q = list(V)
    while Q:
        u = min(Q, key=lambda v: dist[v])
        Q.remove(u)
        for v in E[u]:
            alt = dist[u] + 1
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
    return dist, prev


def dist_dijkstra(V, E, s, t):
    dist, prev = dijkstra(V, E, s)
    return dist, prev, dist[t], t


def print_path(s, t, prev, L):
    if s == t:
        L.append(s)
        return L
    elif prev[t] is None:
        return None
    else:
        L.append(t)
        return print_path(s, prev[t], prev, L)


def min_dist(r):
    _, _, d, _ = r
    return d


def caminoAChicas(N, M, X0, Y0, X1, Y1, X2, Y2, X3, Y3, X4, Y4, X5, Y5, X6, Y6):
    V, E = build_graph(N, M, X5, Y5, X6, Y6)
    dist_source, prev_source = dijkstra(V, E, (X0, Y0))
    dist_coffee, prev_coffee = dijkstra(V, E, (X1, Y1))
    dist_snack, prev_snack, d, target = min(
        [dist_dijkstra(V, E, (X2, Y2), (x, y)) for x in range(X3, X4 + 1) for y in range(Y3, Y4 + 1)], key=min_dist)
    p1 = print_path((X0, Y0), (X1, Y1), prev_source, [])
    p2 = print_path((X1, Y1), (X2, Y2), prev_coffee, [])
    p3 = print_path((X2, Y2), target, prev_snack, [])
    p1.reverse()
    p2.reverse()
    p3.reverse()
    final_path = p1[:-1] + p2[:-1] + p3
    return str(final_path) + "," + str(len(final_path))


print caminoAChicas(8, 8, 2, 1, 7, 2, 2, 7, 6, 6, 7, 7, 3, 3, 5, 4)
