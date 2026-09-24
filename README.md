# Heat Transfer 1D

Steady 1D heat conduction in a homogeneous bar, solved analytically and with finite differences.

## Problem

$$\frac{d^2T}{dx^2} = 0, \quad T(0) = T_L, \quad T(L) = T_R$$

## Baseline case

L = 1 m   ·   T_L = 100 °C   ·   T_R = 20 °C

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
