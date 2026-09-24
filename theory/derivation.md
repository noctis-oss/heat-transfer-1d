# Analytical solution

Governing equation $d^2T/dx^2 = 0$, with $T(0) = T_L$ and $T(L) = T_R$.

1. $dT/dx = C_1$            3. $T(0) = T_L$ gives $C_2 = T_L$
2. $T(x) = C_1 x + C_2$    4. $T(L) = T_R$ gives $C_1 = (T_R - T_L)/L$

$$T(x) = T_L + \frac{T_R - T_L}{L}\,x$$

Baseline ($L = 1$ m, $T_L = 100$ °C, $T_R = 20$ °C): $T(x) = 100 - 80x$, so $T(0.5) = 60$ °C.

## With uniform heat generation

A volumetric heat generation rate $\dot q$ (W/m³) in a bar of thermal conductivity
$k$ gives $d^2T/dx^2 = -S$ with $S = \dot q/k$ (K/m²), and the same boundary conditions.

1. $dT/dx = -Sx + C_1$
2. $T(x) = -\tfrac{S}{2}x^2 + C_1 x + C_2$
3. $T(0) = T_L$ gives $C_2 = T_L$; $T(L) = T_R$ gives $C_1 = (T_R - T_L)/L + SL/2$

$$T(x) = T_L + \frac{T_R - T_L}{L}\,x + \frac{S}{2}\,x\,(L - x)$$

The parabola is zero at both ends and adds $SL^2/8$ at the midpoint.
Case of Lab 11: $k = 50$ W/(m·K), $\dot q = 4000$ W/m³, so $S = 80$ K/m²;
with $L = 1$ m, $T_L = 100$ °C, $T_R = 30$ °C: $T(0.5) = 65 + 80/8 = 75$ °C.
