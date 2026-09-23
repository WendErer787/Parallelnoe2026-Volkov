import numpy as np

N = 2000   # размер

def load(p):
    with open(p) as f:
        f.readline()
        return np.loadtxt(f, dtype=np.int64)

A = load(f"data/A{N}.txt")
B = load(f"data/B{N}.txt")
C = load(f"data/C{N}.txt")

diff = np.abs(C - A @ B).max()
print(f"Макс. разница: {diff}")
print("OK" if diff == 0 else "ОШИБКА")