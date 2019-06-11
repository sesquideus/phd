mond: mond.cpp
	g++ mond.cpp -o mond

mond.out: mond
	./mond > mond.out

mond.png: mond.out mond.gp
	gnuplot mond.gp > mond.png
