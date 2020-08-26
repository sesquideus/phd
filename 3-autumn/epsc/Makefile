MAKEFLAGS += --no-builtin-rules
MAKEFLAGS += --no-builtin-variables

epsc.pdf: epsc.tex ../../kvik-beamer.tex
	texfot xelatex -file-line-error -halt-on-error -interaction=nonstopmode -jobname $(subst .pdf,,$@) $<
	texfot xelatex -file-line-error -halt-on-error -interaction=nonstopmode -jobname $(subst .pdf,,$@) $<
	texfot xelatex -file-line-error -halt-on-error -interaction=nonstopmode -jobname $(subst .pdf,,$@) $<
