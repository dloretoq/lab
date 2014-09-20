from itertools import product


def generate_edges(V, M):
    E = {}
    for v in V:
        E[v] = []
        (x, y) = v
        # up
        if y - 1 >= 0:
            E[v].append((x, y - 1))
        # down
        if y + 1 < M:
            E[v].append((x, y + 1))
        # left
        if x - 1 >= 0:
            E[v].append((x - 1, y))
        # right
        if y - 1 > 0:
            E[v].append((x + 1, y))
    return E


def build_graph(N, M):
    V = list(product(range(N), range(M)))
    E = generate_edges(V, M)
    return V, E


def caminoAChicas(N, M, X0, Y0, X1, Y1, X2, Y2, X3, Y3, X4, Y4, X5, Y5, X6, Y6):
    return ""

# caminoAChicas(8,8,2,1,7,2,2,7,6,6,7,7,3,3,5,4)
print build_graph(2, 2)