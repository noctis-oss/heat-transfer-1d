# Heat Transfer 1D

Steady 1D heat conduction in a homogeneous bar, solved analytically and with finite differences.

## Problem

$$\frac{d^2T}{dx^2} = 0, \quad T(0) = T_L, \quad T(L) = T_R$$

## Baseline without heat generation (v1.0)

L = 1 m   ·   T_L = 100 °C   ·   T_R = 30 °C

## How to run

    python3 -m venv .venv
    source .venv/bin/activate
    python -m pip install -r requirements.txt
    python src/verify_case.py
    python src/run_case.py

| Folder   | Holds                              |
|----------|------------------------------------|
| theory/  | the derivation                     |
| src/     | solver, exact solution, checks     |
| results/ | the temperature table (generated)  |
| figures/ | the comparison figure (generated)  |

## Contact

Questions or corrections: open an issue on this repository.

## Reproducing the published result (v1.0)

Use the Python version recorded for your run on macOS; the exact packages are in `requirements-lock.txt`.

    git clone git@github.com:<you>/heat-transfer-1d.git heat-transfer-1d-reproduction
    cd heat-transfer-1d-reproduction
    git switch --detach v1.0
    python3 -m venv .venv
    source .venv/bin/activate
    python -m pip install -r requirements-lock.txt
    python src/verify_case.py
    python src/run_case.py
    git status --short

Expected midpoint temperature: 65.0 °C. `git status --short` prints nothing.

## Heat-generation case (v1.1)

The equation is now $d^2T/dx^2 = -S$, where $S = \dot q/k$.
L = 1 m, T_L = 100 C, T_R = 30 C, S = 80 K/m², 101 nodes.
Expected midpoint: 75.0 C. With S = 0 (v1.0), it is 65.0 C.
Run `python src/verify_case.py` and `python src/run_case.py`.
