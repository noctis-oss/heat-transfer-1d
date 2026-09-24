"""Analytical solution for steady 1D heat conduction in a bar."""

import numpy as np


def analytical_temperature(x, length, t_left,
                           t_right, source=0.0):
    """Exact temperature for d2T/dx2 = -source.

    T(x) = T_L + (T_R - T_L) x/L + S x (L - x)/2
    """
    if length <= 0:
        raise ValueError("length must be positive")
    x = np.asarray(x, dtype=float)
    return (t_left + (t_right - t_left) * x / length
            + 0.5 * source * x * (length - x))


if __name__ == "__main__":
    LENGTH = 1.0      # m
    T_LEFT = 100.0    # deg C
    T_RIGHT = 20.0    # deg C

    for x in (0.0, 0.25, 0.5, 0.75, 1.0):
        t = analytical_temperature(x, LENGTH, T_LEFT, T_RIGHT)
        print(f"x = {x:4.2f} m  ->  T = {t:5.1f} C")
