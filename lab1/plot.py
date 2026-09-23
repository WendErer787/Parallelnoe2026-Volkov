import matplotlib.pyplot as plt
import numpy as np

N = np.array([200, 400, 800, 1200, 1600, 2000], dtype=float)
t = np.array([0.955, 5.568, 55.491, 191.309, 592.232, 1510.205])  # мс

theory = t[0] * (N / N[0]) ** 3

# --- График 1: обычные координаты ---
plt.figure(figsize=(8, 5))
plt.plot(N, t, 'o-', label='эксперимент')
plt.plot(N, theory, '--', label=r'$O(N^3)$ (теория)')
plt.xlabel('N (размер матрицы)')
plt.ylabel('Время, мс')
plt.title('Зависимость времени умножения от размера матрицы')
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.savefig('plot_time.png', dpi=150)

# --- График 2: log-log ---
plt.figure(figsize=(8, 5))
plt.loglog(N, t, 'o-', label='эксперимент')
plt.loglog(N, theory, '--', label=r'$O(N^3)$ (теория)')
plt.xlabel('N (лог. шкала)')
plt.ylabel('Время, мс (лог. шкала)')
plt.title('Зависимость времени от N (log-log)')
plt.grid(True, which='both', alpha=0.3)
plt.legend()
plt.tight_layout()
plt.savefig('plot_log.png', dpi=150)

print("Готово: plot_time.png, plot_log.png")