# python3


def read_input():
    return (input().rstrip(), input().rstrip())


def poly_hash(S, p, x):
    hash = 0
    for c in reversed(S):
        hash = (hash * x + ord(c)) % p
    return hash


def precompute_hashes(T, P_len, p, x):
    T_len = len(T)
    H = [None] * (T_len - P_len + 1)
    S = T[P_len:]
    H[T_len - P_len] = poly_hash(S, p, x)

    y = 1
    for _ in range(P_len):
        y = y * x % p

    for i in range(T_len - P_len - 1, -1, -1):
        H[i] = (x * H[i + 1] + ord(T[i]) - y * ord(T[i + P_len])) % p
    return H


def print_occurrences(output):
    print(" ".join(map(str, output)))


def get_occurrences(P, T):
    p = 1000000007
    x = 263

    positions = []
    p_hash = poly_hash(P, p, x)

    for i in range(len(T) - len(P) + 1):
        t_hash = poly_hash(T[i : i + len(P)], p, x)
        if p_hash == t_hash and T[i : i + len(P)] == P:
            positions.append(i)
    return positions


if __name__ == "__main__":
    print_occurrences(get_occurrences(*read_input()))
