MAKEFLAGS += --no-builtin-rules
MAKEFLAGS += --no-builtin-variables

input/programme.tex: \
	talks/talks.yaml \
	templates/programme.tex
	../../jinja.py -c $< -o $@ templates/programme.tex

#	pandoc --mathjax --from markdown+smart --pdf-engine xelatex -to tex --metadata land=sk-SK

output/programme.pdf: input/programme.tex
	@texfot xelatex -file-line-error -jobname=$(subst .pdf,,$@) -halt-on-error -interaction=nonstopmode input/programme.tex
