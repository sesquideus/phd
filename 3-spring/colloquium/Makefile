MAKEFLAGS += --no-builtin-rules
MAKEFLAGS += --no-builtin-variables

presentation.pdf: presentation.tex
	texfot xelatex -file-line-error -jobname=$(subst .pdf,,$@) -halt-on-error -interaction=nonstopmode presentation.tex
	texfot xelatex -file-line-error -jobname=$(subst .pdf,,$@) -halt-on-error -interaction=nonstopmode presentation.tex
	texfot xelatex -file-line-error -jobname=$(subst .pdf,,$@) -halt-on-error -interaction=nonstopmode presentation.tex
