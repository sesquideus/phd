.SECONDEXPANSION:

thesis.pdf: *.tex thesis.bib \
	$$(wildcard pictures/*.pdf)
	@echo -e '$(c_action)Compiling XeLaTeX file $(c_filename)$@$(c_action), primary run:$(c_default)'
	@texfot xelatex -file-line-error -jobname=$(subst .pdf,,$@) -halt-on-error -interaction=nonstopmode ./thesis.tex
	bibtex thesis
	@texfot xelatex -file-line-error -jobname=$(subst .pdf,,$@) -halt-on-error -interaction=nonstopmode ./thesis.tex
	@texfot xelatex -file-line-error -jobname=$(subst .pdf,,$@) -halt-on-error -interaction=nonstopmode ./thesis.tex

cover.pdf: *.tex
	@texfot xelatex -file-line-error -jobname=$(subst .pdf,,$@) -halt-on-error -interaction=nonstopmode ./cover.tex
	@texfot xelatex -file-line-error -jobname=$(subst .pdf,,$@) -halt-on-error -interaction=nonstopmode ./cover.tex

pictures/%.pdf: pictures/%.gp
	gnuplot $<

clean:
	rm -f thesis.pdf thesis.toc thesis.aux thesis.blg thesis.bbl thesis.toc thesis.out

all: thesis.pdf
