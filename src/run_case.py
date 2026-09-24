"""Run one case: solve, compare with the exact solution, save CSV and figure."""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")  # write image files; never open a window
import matplotlib.pyplot as plt
import numpy as np

from analytical import analytical_temperature
from finite_difference import solve_temperature

# ---- Case parameters: this is the only place to change them ----
N_NODES = 101
LENGTH = 1.0      # m
T_LEFT = 100.0    # deg C
T_RIGHT = 30.0    # deg C, measured at the cold end
SOURCE = 80.0     # K/m^2, heat generation q/k
# -----------------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent
CSV_PATH = PROJECT_ROOT / "results" / "temperature.csv"
FIGURE_PATH = PROJECT_ROOT / "figures" / "temperature_comparison.png"


def main():
    x, t_numerical = solve_temperature(N_NODES, LENGTH, T_LEFT, T_RIGHT, SOURCE)
    t_exact = analytical_temperature(x, LENGTH, T_LEFT, T_RIGHT, SOURCE)
    max_error = np.max(np.abs(t_numerical - t_exact))
    midpoint = analytical_temperature(LENGTH / 2, LENGTH, T_LEFT, T_RIGHT,
                                      SOURCE)

    CSV_PATH.parent.mkdir(exist_ok=True)
    np.savetxt(CSV_PATH, np.column_stack([x, t_numerical, t_exact]),
               delimiter=",", fmt="%.6f", comments="",
               header="x_m,T_numerical_C,T_analytical_C")

    FIGURE_PATH.parent.mkdir(exist_ok=True)
    x_fine = np.linspace(0.0, LENGTH, 200)
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(x_fine, analytical_temperature(x_fine, LENGTH, T_LEFT, T_RIGHT,
                                       SOURCE),
            label="Analytical")
    ax.plot(x, t_numerical, "o", label=f"Finite differences ({N_NODES} nodes)")
    ax.set_xlabel("Position x (m)")
    ax.set_ylabel("Temperature T (°C)")
    ax.set_title("Steady 1D conduction in a bar")
    ax.legend()
    fig.tight_layout()
    fig.savefig(FIGURE_PATH, dpi=150, metadata={"Software": None})
    plt.close(fig)

    print(f"Nodes: {N_NODES}   L = {LENGTH} m   "
          f"T_L = {T_LEFT} C   T_R = {T_RIGHT} C   S = {SOURCE} K/m^2")
    print(f"Midpoint temperature: {midpoint:.1f} C")
    print(f"Maximum |numerical - analytical|: {max_error:.1e} C")
    print(f"Wrote {CSV_PATH.relative_to(PROJECT_ROOT)}")
    print(f"Wrote {FIGURE_PATH.relative_to(PROJECT_ROOT)}")


if __name__ == "__main__":
    main()
