.SECONDEXPANSION:

%.tex: $$*.md
	pandoc $< --to latex --smart \
	--bibliography ../../kvik.bib --output $@

%.pdf: out-$$*.tex $$*.tex
	@texfot xelatex -file-line-error -jobname=$(subst .pdf,,$@) -halt-on-error -interaction=nonstopmode $<
	biber $*
	@texfot xelatex -file-line-error -jobname=$(subst .pdf,,$@) -halt-on-error -interaction=nonstopmode $<
	@texfot xelatex -file-line-error -jobname=$(subst .pdf,,$@) -halt-on-error -interaction=nonstopmode $<

grant.pdf: aim.pdf status.pdf method.pdf annotation.pdf money.pdf 
	pdfunite $^ grant.pdf
