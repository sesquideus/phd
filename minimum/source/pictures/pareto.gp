set terminal pdf size 16cm, 12cm font "Minion Pro, 20"
set xlabel "Mass (kg)"
set ylabel "Probability density"
set grid
set key top right box lw 1 height 0.5 width 0.5 spacing 1.3

xmin = 1e-6
xmax = 1e-1

set xrange [xmin:xmax]
set logscale x
set format x "10^{%L}"
set format y "%f"
set samples 10000

f(x, s) = (x < xmin ? 0 : (s-1) * xmin**(s-1) / (x ** s))
g(x, s) = (x < xmin ? 0 : (1e-3/x)**s)
h(x, s) = (x < xmin ? 0 : (0.001)**s / (xmin**(s-1) * (s-1)))
#0.01**s * 1/(1-s) * (x ** (1-s) - xm**(1-s)))

set title "Pareto distribution, normalized to total count"
plot \
    f(x, 1.6) title "s = 1.6" with lines lw 2, \
    f(x, 1.8) title "s = 1.8" with lines lw 2, \
    f(x, 2.0) title "s = 2.0" with lines lw 2, \
    f(x, 2.2) title "s = 2.2" with lines lw 2

set title "Pareto distribution, normalized to number at x_{min}"
set yrange [0:1000]
plot \
    g(x, 1.6) title "s = 1.6" with lines lw 2, \
    g(x, 1.8) title "s = 1.8" with lines lw 2, \
    g(x, 2.0) title "s = 2.0" with lines lw 2, \
    g(x, 2.2) title "s = 2.2" with lines lw 2

set yrange [0:0.002]
plot \
    h(x, 1.6) title "s = 1.6" with lines lw 2, \
    h(x, 1.8) title "s = 1.8" with lines lw 2, \
    h(x, 2.0) title "s = 2.0" with lines lw 2, \
    h(x, 2.2) title "s = 2.2" with lines lw 2

