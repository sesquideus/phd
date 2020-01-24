.SECONDEXPANSION:

input/%.tex: \
	source/%.tex
	./jinja.py $< -c source/context.yaml -o $@

input/%.pdf: source/%.gp
	@echo -e '$(c_action)[gnuplot] Rendering file $(c_filename)$<$(c_action) to PDF file $(c_filename)$@$(c_action):$(c_default)'
	@mkdir -p $(dir $@)
	gnuplot -e "set output '$@'; set fit quiet;" $<

output/thesis.pdf: \
	input/thesis.tex \
	$$(subst source/,input/,$$(wildcard source/*.tex)) \
	$$(wildcard pictures/*.pdf) \
	source/thesis.bib
	@mkdir -p $(dir $@)
	@echo -e '$(c_action)Compiling XeLaTeX file $(c_filename)$@$(c_action), primary run:$(c_default)'
	@texfot xelatex -file-line-error -jobname=$(subst .pdf,,$@) -halt-on-error -interaction=nonstopmode $(subst output,input,$(subst .pdf,.tex,$@))
	biber output/thesis.bcf
	@texfot xelatex -file-line-error -jobname=$(subst .pdf,,$@) -halt-on-error -interaction=nonstopmode $(subst output,input,$(subst .pdf,.tex,$@))
	@texfot xelatex -file-line-error -jobname=$(subst .pdf,,$@) -halt-on-error -interaction=nonstopmode $(subst output,input,$(subst .pdf,.tex,$@))

output/cover.pdf: *.tex
	@mkdir -p $(dir $@)
	@texfot xelatex -file-line-error -jobname=$(subst .pdf,,$@) -halt-on-error -interaction=nonstopmode ./cover.tex
	@texfot xelatex -file-line-error -jobname=$(subst .pdf,,$@) -halt-on-error -interaction=nonstopmode ./cover.tex


clean:
	rm -rf output/

distclean: clean
	rm -rf input/

all: thesis.pdf
