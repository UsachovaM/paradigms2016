import numpy as np
from math import log2, ceil

def read_matr(a, n, k):
    for i in range(k):
        if i<n:
            s=np.array(list(map(int, input().split())), dtype=int)
            s1=np.array(([0]*(k-n)), dtype=int)
            s=np.concatenate((s,s1), axis=0)
            a=np.concatenate((a,s), axis=0)
        else:
            s1=np.array(([0]*(k)), dtype=int)
            a=np.concatenate((a,s1), axis=0)
    return a

def strassen(a,b,m):
    if m==1:
        return np.dot(a,b)
    else:
        m=int(m/2)
        a11 = a[:m, :m]
        a12 = a[:m, m:]
        a21 = a[m:, :m]
        a22 = a[m:, m:]
        b11 = b[:m, :m]
        b12 = b[:m, m:]
        b21 = b[m:, :m]
        b22 = b[m:, m:]
        p1 = strassen(a11+a22, b11+b22, m)
        p2 = strassen(a21+a22, b11, m)
        p3 = strassen(a11, b12-b22, m)
        p4 = strassen(a22, b21-b11, m)
        p5 = strassen(a11+a12, b22, m)
        p6 = strassen(a21-a11, b11+b12, m)
        p7 = strassen(a12-a22, b21+b22, m)
        c11 = p1 + p4 - p5 + p7
        c12 = p3 + p5
        c21 = p2 + p4
        c22 = p1 - p2 + p3 + p6
        return np.vstack((np.hstack((c11, c12)), np.hstack((c21, c22))))

def main():
    a = np.empty((0), dtype=int)
    b = np.empty((0), dtype=int)
    n = int(input())
    k=2**(ceil(log2(n)))
    a = read_matr(a, n, k)
    b = read_matr(b, n, k)
    a = a.reshape((k,k))
    b = b.reshape((k,k)) 
    for row in strassen(a, b, k)[:n, :n]:
        print(*row)
