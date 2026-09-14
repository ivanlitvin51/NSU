import random
import math
import sys
import matplotlib.pyplot as plt
from collections import deque

# Настройка кодировки для корректного вывода в терминале Windows
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass

# Фиксируем сид для воспроизводимости результатов (по условию задания)
RANDOM_SEED = 42
random.seed(RANDOM_SEED)


# =========================================================================
# Часть 1. Вычисление числа pi методом Монте-Карло
# =========================================================================

def run_monte_carlo_pi(num_points):
    """
    Моделирует случайные броски точек в единичный квадрат [0, 1] x [0, 1].
    Точка попадает в сектор четверти круга, если x^2 + y^2 <= 1.
    Возвращает динамику приближения pi на каждом шаге.
    """
    hits = 0
    pi_history = []

    for step in range(1, num_points + 1):
        # Координаты точки, равномерно распределенной в [0, 1] x [0, 1]
        x = random.random()
        y = random.random()

        # Проверка принадлежности четверти единичного круга
        if x * x + y * y <= 1.0:
            hits += 1

        # S_сектора / S_квадрата = (pi / 4) / 1 => pi ≈ 4 * (hits / step)
        current_pi_estimate = 4.0 * hits / step
        pi_history.append(current_pi_estimate)

    return pi_history


TOTAL_POINTS = 100_000
estimates = run_monte_carlo_pi(TOTAL_POINTS)
abs_errors = [abs(est - math.pi) for est in estimates]

# График зависимости абсолютной ошибки от числа испытаний в лог-шкале
plt.figure(figsize=(8, 4.5))
plt.plot(range(1, TOTAL_POINTS + 1), abs_errors, color='steelblue', lw=0.9)
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Количество испытаний n (log scale)')
plt.ylabel('Абсолютная ошибка |pi_est - pi| (log scale)')
plt.title('Погрешность оценки числа pi методом Монте-Карло')
plt.grid(True, which='both', linestyle='--', alpha=0.35)
plt.tight_layout()
plt.savefig('pi_error.png', dpi=120)
plt.close()

print(f"Оценка pi: {estimates[-1]:.6f}, итоговая ошибка: {abs_errors[-1]:.6f}")


# =========================================================================
# Часть 2. Моделирование вероятности перколяции на решетке
# =========================================================================

def generate_lattice(rows, cols, prob):
    """
    Создает случайную решетку: True — проходимая клетка (с вероятностью prob),
    False — заблокированная клетка.
    """
    return [[random.random() < prob for _ in range(cols)] for _ in range(rows)]


def check_percolation(board, rows, cols):
    """
    Проверяет наличие непрерывного пути из открытых клеток от верхней
    строки к нижней с помощью обхода в ширину (BFS).
    Переходы возможны только по 4 направлениям (соседи по ребру).
    """
    visited = [[False] * cols for _ in range(rows)]
    queue = deque()

    # Стартуем со всех доступных открытых клеток в верхней строке (строка 0)
    for c in range(cols):
        if board[0][c]:
            queue.append((0, c))
            visited[0][c] = True

    # Четыре направления перемещения (вверх, вниз, влево, вправо)
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while queue:
        r, c = queue.popleft()

        # Достигли нижней границы поля — путь найден (ранний выход)
        if r == rows - 1:
            return True

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            # Проверяем границы сетки, проходимость клетки и отсутствие посещения
            if 0 <= nr < rows and 0 <= nc < cols:
                if not visited[nr][nc] and board[nr][nc]:
                    visited[nr][nc] = True
                    queue.append((nr, nc))

    return False


# Параметры моделирования
GRID_SIZE = 40       # Размер решетки 40x40
EXPERIMENTS = 100    # Число испытаний на каждое значение p
p_values = [round(step * 0.05, 2) for step in range(21)]  # p от 0.0 до 1.0 с шагом 0.05
percolation_rates = []

for p in p_values:
    successes = 0
    for _ in range(EXPERIMENTS):
        grid = generate_lattice(GRID_SIZE, GRID_SIZE, p)
        if check_percolation(grid, GRID_SIZE, GRID_SIZE):
            successes += 1
    percolation_rates.append(successes / EXPERIMENTS)

# Построение графика вероятности протекания
plt.figure(figsize=(8, 4.5))
plt.plot(p_values, percolation_rates, marker='s', markersize=4, color='darkorange', label='Эксперимент (40x40)')
# Теоретический порог для 2D квадратной решетки узлов p_c ≈ 0.5927
plt.axvline(0.5927, color='navy', linestyle='--', linewidth=1.2, label='Порог p_c ≈ 0.5927')
plt.xlabel('Вероятность открытой клетки (p)')
plt.ylabel('Вероятность перколяции P(p)')
plt.title(f'Перколяция на решетке {GRID_SIZE}x{GRID_SIZE} ({EXPERIMENTS} экспериментов на точку)')
plt.legend()
plt.grid(True, alpha=0.35)
plt.tight_layout()
plt.savefig('percolation.png', dpi=120)
plt.close()

print("\nРезультаты моделирования перколяции:")
for p, rate in zip(p_values, percolation_rates):
    print(f"p = {p:.2f} -> P = {rate:.2f}")