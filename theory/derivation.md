# Analytical solution

Governing equation $d^2T/dx^2 = 0$, with $T(0) = T_L$ and $T(L) = T_R$.

1. $dT/dx = C_1$            3. $T(0) = T_L$ gives $C_2 = T_L$
2. $T(x) = C_1 x + C_2$    4. $T(L) = T_R$ gives $C_1 = (T_R - T_L)/L$

$$T(x) = T_L + \frac{T_R - T_L}{L}\,x$$

Baseline ($L = 1$ m, $T_L = 100$ °C, $T_R = 20$ °C): $T(x) = 100 - 80x$, so $T(0.5) = 60$ °C.
