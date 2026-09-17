.PHONY: pdf
pdf:
	latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error -outdir=build main.tex
	cp build/main.pdf wilf-four-generators.pdf
