import sys
import math

def answer(L):
    n = len(L)
    m = len(L[0])
    S = ""
    dist = 0

    for i in range(m):
        charset = list(map(lambda x: x[i], L))
        min = math.inf
        dna = ""
        for char in charset:
            cnt = n - charset.count(char)
            if cnt < min:
                min = cnt
                dna = char
            elif cnt == min and char < dna:
                dna = char
        S += dna
        dist += min

    return S, dist


def test():
    cases = [
        [
            5, 8,
            ["TATGATAC",
             "TAAGCTAC",
             "AAAGATCC",
             "TGAGATAC",
             "TAAGATGT"],
            ("TAAGATAC", 7)
         ],
        [
            4, 10,
            ["ACGTACGTAC",
            "CCGTACGTAG",
            "GCGTACGTAT",
            "TCGTACGTAA"],
            ("ACGTACGTAA", 6)
        ],
        [
            6, 10,
            [
                "ATGTTACCAT",
                'AAGTTACGAT',
                "AACAAAGCAA",
                "AAGTTACCTT",
                "AAGTTACCAA",
                "TACTTACCAA"
            ],
            ("AAGTTACCAA", 12)
        ]
    ]

    for i, (N, M, L, expected) in enumerate(cases):
        shortest, dist = answer(L)
        if shortest != expected[0] or dist != expected[1]:
            print(f'case #{i+1} is wrong!\nDNA and hamming distance are expected to be {expected[0]} and {expected[1]} respectively, but {shortest} and {dist} are given.')


# test()

def sol():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    L = [input().rstrip() for _ in range(N)]
    for ans in answer(L):
        print(ans)

sol()
