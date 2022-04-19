# python3


def read_input():
    return (input().rstrip(), input().rstrip())


def poly_hash(S, p, x):
    hash = 0
    for c in reversed(S):
        hash = (hash * x + ord(c)) % p
    return hash


def precompute_hashes(T, P, p, x):
    H = [None] * (len(T) - len(P) + 1)
    S = T[len(T) - len(P) :]
    H[len(T) - len(P)] = poly_hash(S, p, x)

    y = 1
    for _ in range(len(P)):
        y = (y * x) % p

    for i in reversed(range(len(T) - len(P))):
        H[i] = (x * H[i + 1] + ord(T[i]) - y * ord(T[i + len(P)])) % p
    return H


def print_occurrences(output):
    print(" ".join(map(str, output)))


def get_occurrences(P, T):
    p = 1000000007
    x = 263

    positions = []
    p_hash = poly_hash(P, p, x)
    H = precompute_hashes(T, P, p, x)

    for i in range(len(T) - len(P) + 1):
        if p_hash == H[i] and T[i : i + len(P)] == P:
            positions.append(i)
    return positions


if __name__ == "__main__":
    print_occurrences(get_occurrences(*read_input()))
