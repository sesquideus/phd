MAKEFLAGS += --no-builtin-rules
MAKEFLAGS += --no-builtin-variables

referee.pdf: referee.tex content.tex
	@texfot xelatex -file-line-error -jobname=$(subst .pdf,,$@) -halt-on-error -interaction=nonstopmode referee.tex

%.emd: %.md
	../../jinja.py $< -c meta.yaml -o $@

%.tex: %.emd
	~/dgs/core/pandoc-convert.py latex sk $< $@
