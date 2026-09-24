"""Check the finite-difference solver against the analytical solution."""

import sys

import numpy as np

from analytical import analytical_temperature
from finite_difference import solve_temperature

TOLERANCE = 1e-9  # deg C, absolute

# (n_nodes, length in m, left T in C, right T in C, source in K/m^2)
CASES = [
    (11, 1.0, 100.0, 20.0, 0.0),    # the original baseline
    (3, 1.0, 100.0, 20.0, 0.0),     # the smallest grid
    (21, 2.5, 100.0, 20.0, 0.0),    # a longer bar
    (11, 1.0, 50.0, 50.0, 0.0),     # equal ends
    (11, 1.0, 20.0, 100.0, 0.0),    # reversed ends
    (101, 1.0, 100.0, 30.0, 80.0),  # heat generation
    (3, 1.0, 100.0, 20.0, 80.0),    # smallest grid, source
    (21, 2.5, 100.0, 20.0, -40.0),  # heat removed
]


def main():
    failures = 0
    for n_nodes, length, t_left, t_right, source in CASES:
        x, t_numerical = solve_temperature(
            n_nodes, length, t_left, t_right, source)
        t_exact = analytical_temperature(
            x, length, t_left, t_right, source)
        max_error = np.max(np.abs(t_numerical - t_exact))
        passed = max_error <= TOLERANCE
        failures += not passed
        label = "PASS" if passed else "FAIL"
        print(f"{label}  N={n_nodes:3d}  L={length:3.1f} m  "
              f"T_L={t_left:5.1f} C  T_R={t_right:5.1f} C  "
              f"S={source:5.1f} K/m2  max error={max_error:.1e} C")

    if failures:
        print(f"{failures} check(s) FAILED.")
        return 1
    print("All checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
