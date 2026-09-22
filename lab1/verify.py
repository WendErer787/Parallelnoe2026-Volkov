import numpy as np

def load(p):
    with open(p) as f:
        n = int(f.readline())
        return np.loadtxt(f)

A = load("data/A.txt")
B = load("data/B.txt")
C = load("data/C.txt")

err = np.abs(C - A @ B).max()
print(f"Макс. ошибка: {err:.3e}")
print("OK" if err < 1e-6 else "ОШИБКА")