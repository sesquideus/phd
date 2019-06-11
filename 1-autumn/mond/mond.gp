set terminal png size 1000,1000
plot 'mond.out' using 1:2 with linespoints

set polar
set size square
set output 'polar.png'
plot 'mond.out' using 1:(1/$2) with points pointsize 1 pointtype 6
