MAKEFLAGS += --no-builtin-rules
MAKEFLAGS += --no-builtin-variables

input/programme.tex: \
	talks/talks.yaml \
	templates/programme.tex
	../../jinja.py -c $< -o $@ templates/programme.tex

input/certificates.tex: \
	talks/talks.yaml \
	templates/certificates.tex
	../../jinja.py -c $< -o $@ templates/certificates.tex

#	pandoc --mathjax --from markdown+smart --pdf-engine xelatex -to tex --metadata land=sk-SK

output/%.pdf: input/%.tex
	@texfot xelatex -file-line-error -jobname=$(subst .pdf,,$@) -halt-on-error -interaction=nonstopmode $<


all: \
	output/programme.pdf \
	output/certificate.pdf ;
