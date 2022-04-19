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


def get_occurrences(pattern, text):
    prime = 1000000007
    multiplier = 263

    positions = []
    p_hash = poly_hash(pattern, prime, multiplier)
    hashes = precompute_hashes(text, len(pattern), prime, multiplier)

    for i in range(len(text) - len(pattern) + 1):
        if p_hash != hashes[i]:
            continue
        if text[i : i + len(pattern)] == pattern:
            positions.append(i)
    return positions


if __name__ == "__main__":
    print_occurrences(get_occurrences(*read_input()))
