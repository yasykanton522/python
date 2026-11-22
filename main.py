import numpy as np
from scipy import integrate, interpolate, optimize
import matplotlib.pyplot as plt


def main():
    hours = np.array([0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 23], dtype=float)
    temps = np.array([17.5, np.nan, 15.8, 17.0, 20.5, 24.0, np.nan, 26.8, 25.2, 21.0, np.nan, 18.4, 17.8], dtype=float)

    mask = ~np.isnan(temps)
    curve = interpolate.CubicSpline(hours[mask], temps[mask])

    min_res = optimize.minimize_scalar(curve, bounds=(0, 23), method="bounded")
    max_res = optimize.minimize_scalar(lambda t: -curve(t), bounds=(0, 23), method="bounded")

    mean_temp = integrate.quad(curve, 0, 23)[0] / 23

    crossings = []
    for a, b in zip(hours[:-1], hours[1:]):
        if (curve(a) - 22) * (curve(b) - 22) < 0:
            root = optimize.root_scalar(lambda t: curve(t) - 22, bracket=(a, b), method="brentq").root
            crossings.append(round(float(root), 2))

    print(f"Минимум: {min_res.fun:.2f} °C в {min_res.x:.2f} ч")
    print(f"Максимум: {-max_res.fun:.2f} °C в {max_res.x:.2f} ч")
    print(f"Средняя температура: {mean_temp:.2f} °C")
    print(f"Пересечение 22 °C: {crossings} ч")

    t_grid = np.linspace(0, 23, 200)
    plt.plot(t_grid, curve(t_grid), label="Кривая температуры")
    plt.scatter(hours[mask], temps[mask], label="Данные")
    plt.scatter([min_res.x, max_res.x], [min_res.fun, -max_res.fun], label="Мин / Макс")
    plt.axhline(22, linestyle="--", label="Норма 22 °C")
    plt.xlabel("Часы")
    plt.ylabel("Температура, °C")
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()