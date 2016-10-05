import numpy as np
from math import log2, ceil


def find_power2(n):
    i = 1
    while i < n:
        i = i * 2
    return i


def read_matr(n):
    a = np.zeros((find_power2(n), find_power2(n)), dtype=int)
    for i in range(n):
        a[i, :n] = np.array(input().split(), dtype=int)
    return a


def divide_matr(a):
    up_a, down_a = np.vsplit(a, 2)
    a11, a12 = np.hsplit(up_a, 2)
    a21, a22 = np.hsplit(down_a, 2)
    return a11, a12, a21, a22


def strassen(a, b):
    if len(a) == 1:
        return np.dot(a, b)
    else:
        a11, a12, a21, a22 = divide_matr(a)
        b11, b12, b21, b22 = divide_matr(b)
        p1 = strassen(a11 + a22, b11 + b22)
        p2 = strassen(a21 + a22, b11)
        p3 = strassen(a11, b12 - b22)
        p4 = strassen(a22, b21 - b11)
        p5 = strassen(a11 + a12, b22)
        p6 = strassen(a21 - a11, b11 + b12)
        p7 = strassen(a12 - a22, b21 + b22)
        c11 = p1 + p4 - p5 + p7
        c12 = p3 + p5
        c21 = p2 + p4
        c22 = p1 - p2 + p3 + p6
        return np.vstack((np.hstack((c11, c12)),
                          np.hstack((c21, c22))))


def main():
    n = int(input())
    n_padded = find_power2(n)
    a = read_matr(n)
    b = read_matr(n)
    for row in strassen(a, b)[:n, :n]:
        print(*row)

if __name__ == "__main__":
    main()
