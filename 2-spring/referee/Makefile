MAKEFLAGS += --no-builtin-rules
MAKEFLAGS += --no-builtin-variables

%.pdf: %.tex
	@texfot xelatex -file-line-error -jobname=$(subst .pdf,,$@) -halt-on-error -interaction=nonstopmode $(subst output,input,$(subst .pdf,.tex,$@))

%.emd: %.md
	../../jinja.py $< -o $@

%.tex: %.emd
	~/dgs/core/pandoc-convert.py latex sk $< $@
