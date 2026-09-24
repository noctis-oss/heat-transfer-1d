"""Finite-difference solver for steady 1D heat conduction in a bar."""

import numpy as np


def solve_temperature(n_nodes, length, t_left, t_right):
    """Solve d2T/dx2 = 0 on n_nodes equally spaced nodes.

    Returns the node positions x (m) and temperatures T (deg C).
    """
    if n_nodes < 3:
        raise ValueError("n_nodes must be at least 3")
    if length <= 0:
        raise ValueError("length must be positive")

    x = np.linspace(0.0, length, n_nodes)
    n_interior = n_nodes - 2

    # Coefficient matrix: 2 on the diagonal, -1 on either side.
    a = np.zeros((n_interior, n_interior))
    np.fill_diagonal(a, 2.0)
    for i in range(n_interior - 1):
        a[i, i + 1] = -1.0
        a[i + 1, i] = -1.0

    # Right-hand side: the known boundary temperatures.
    b = np.zeros(n_interior)
    b[0] += t_left
    b[-1] += t_right

    t = np.empty(n_nodes)
    t[0] = t_left
    t[-1] = t_right
    t[1:-1] = np.linalg.solve(a, b)
    return x, t


if __name__ == "__main__":
    x, t = solve_temperature(5, 1.0, 100.0, 20.0)
    print(x)
    print(t)
