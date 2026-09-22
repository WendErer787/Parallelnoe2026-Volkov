import numpy as np, os

N = int(os.environ.get("N", 512))     #меняеть размер
rng = np.random.default_rng(42)

os.makedirs("data", exist_ok=True)

def save(path, M):
    with open(path, "w") as f:
        f.write(f"{M.shape[0]}\n")
        for row in M:
            f.write(" ".join(f"{x:.10f}" for x in row) + "\n")

save("data/A.txt", rng.uniform(-10, 10, (N, N)))
save("data/B.txt", rng.uniform(-10, 10, (N, N)))
print(f"Готово: матрицы {N}x{N}")