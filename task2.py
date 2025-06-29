import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad


# 1. Визначаємо функцію
def f(x):
    return x ** 2


# 2. Межі інтегрування
a = 0  # нижня межа
b = 2  # верхня межа

# 3. Метод Монте-Карло
N = 100000  # Кількість випадкових точок
x_rand = np.random.uniform(a, b, N)  # випадкові x
y_rand = f(x_rand)  # значення функції у випадкових точках
monte_carlo_result = (b - a) * np.mean(y_rand)  # оцінка інтегралу

print(f"Інтеграл методом Монте-Карло: {monte_carlo_result:.6f}")

# 4. Перевірка точного значення за допомогою quad
quad_result, quad_error = quad(f, a, b)
print(f"Інтеграл (quad): {quad_result:.6f}")
print(f"Похибка (quad): {quad_error:.2e}")

# 5. Побудова графіка
x_plot = np.linspace(-0.5, 2.5, 400)  # діапазон для побудови
y_plot = f(x_plot)

fig, ax = plt.subplots()
ax.plot(x_plot, y_plot, 'r', linewidth=2)  # малюємо функцію

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування осей і підписів
ax.set_xlim([x_plot[0], x_plot[-1]])
ax.set_ylim([0, max(y_plot) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Вертикальні лінії меж інтегрування
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')

ax.set_title('Графік інтегрування f(x) = x^2 від 0 до 2')
plt.grid()
plt.show()

# 6. Висновки
print("\nВисновки:")
error_monte_carlo = abs(monte_carlo_result - quad_result)
print(f"Різниця між методом Монте-Карло і quad: {error_monte_carlo:.6f}")
