set terminal pdf size 16cm, 12cm font "Minion Pro, 20"
set title "Pareto distribution, normalized to count"
set xlabel "Mass (kg)"
set ylabel "Probability density"
set grid
set key top right box lw 1 height 0.5 width 0.5 spacing 1.3

set xrange [0.001:1]
set logscale x
set yrange [0:1200]

set samples 100000

f(x, xm, s) = (x < xm ? 0 : (s-1) * xm**(s-1) / (x ** s))
g(x, xm, s) = (x < xm ? 0 : (0.01/x)** s)
h(x, xm, s) = (s == 2 ? 0.01**s * (log(x) - log(xm)) : x < xm ? 0 : 0.01**s * 1/(2-s) * (x ** (2-s) - xm**(2-s)))

plot \
    f(x, 1e-3, 1.6) title "s = 1.6" with lines lw 2, \
    f(x, 1e-3, 1.8) title "s = 1.8" with lines lw 2, \
    f(x, 1e-3, 2.0) title "s = 2.0" with lines lw 2, \
    f(x, 1e-3, 2.2) title "s = 2.2" with lines lw 2

set yrange [0:170]
plot \
    g(x, 1e-3, 1.6) title "s = 1.6" with lines lw 2, \
    g(x, 1e-3, 1.8) title "s = 1.8" with lines lw 2, \
    g(x, 1e-3, 2.0) title "s = 2.0" with lines lw 2, \
    g(x, 1e-3, 2.2) title "s = 2.2" with lines lw 2

set yrange [0:0.002]
plot \
    h(x, 1e-3, 1.6) title "s = 1.6" with lines lw 2, \
    h(x, 1e-3, 1.8) title "s = 1.8" with lines lw 2, \
    h(x, 1e-3, 2.0) title "s = 2.0" with lines lw 2, \
    h(x, 1e-3, 2.2) title "s = 2.2" with lines lw 2

