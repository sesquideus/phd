MAKEFLAGS += --no-builtin-rules
MAKEFLAGS += --no-builtin-variables

presentation.pdf: presentation.tex
	xelatex -file-line-error -jobname=$(subst .pdf,,$@) -halt-on-error -interaction=nonstopmode presentation.tex
	xelatex -file-line-error -jobname=$(subst .pdf,,$@) -halt-on-error -interaction=nonstopmode presentation.tex
	xelatex -file-line-error -jobname=$(subst .pdf,,$@) -halt-on-error -interaction=nonstopmode presentation.tex
