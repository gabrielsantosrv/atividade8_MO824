PI_g1 = 131
PI_g2 = 1031
PI_h1 = 193
PI_h2 = 1093

def l_function(n, u, pi1, pi2):
    return 1 + ((pi1 * (u - 1) + pi2) % n)

def g_function(n, u):
    l = l_function(n, u, PI_g1, PI_g2)
    if l != u:
        return l
    return 1 + (l % n)

def h_function(n, u):
    l = l_function(n, u, PI_h1, PI_h2)
    g = g_function(n, u)

    if l != u and l != g:
        return l
    elif 1 + (l % n) != u and 1 + (l % n) != g:
        return 1 + (l % n)

    return 1 + ((l + 1) % n)

def generate_triples(n):
    triples = []
    for i in range(1, n+1):
        g = g_function(n, i)
        h = h_function(n, i)
        triples.append(tuple(sorted([i, g, h])))

    return triples


def read_input(filepath):
    coefficients = {}
    with open(filepath) as file:
        size = int(file.readline())
        for i in range(1, size+1):
            values = file.readline().split()
            j = i
            for value in values:
                coefficients[(i, j)] = float(value)
                j += 1

    return coefficients



