import numpy as np, os

N = 2000   # размер
rng = np.random.default_rng(42)

os.makedirs("data", exist_ok=True)

def save(path, M):
    with open(path, "w") as f:
        f.write(f"{M.shape[0]}\n")
        for row in M:
            f.write(" ".join(str(int(x)) for x in row) + "\n")

save(f"data/A{N}.txt", rng.integers(-9, 10, (N, N)))
save(f"data/B{N}.txt", rng.integers(-9, 10, (N, N)))
print(f"Готово: data/A{N}.txt, data/B{N}.txt")