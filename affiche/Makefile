# (c) Feth Arezki - Majerti, feth@majerti.fr
# No copyright.
#
# Produces flat PNG from SVGs. Uses white as background. Exported area: page.
#
# Usage: 'make'.
# 	you can specify a value of 300 DPI with 'make DPI=300'
#
# Requisites:
# 	inkscape (no graphic display needed)
# 	convert, from imagemagick.
#

DPI=600
SVG=$(wildcard *.svg)
PNGS=$(SVG:.svg=-$(DPI)dpi.png)

all: $(PNGS)
	@echo See $^
.PHONY: all

svgpng=inkscape \
	--without-gui --export-background=white --export-area-page --export-dpi=$1 --file=$2 --export-png=$3

flatten=convert -background white -flatten +matte $1 $2

clean:
	-rm $(PNGS)

.PHONY: clean
.IGNORE: clean

help:
	@echo By default, builds PNGs at 600 dpi by default.
	@echo For instance, call "make DPI=200"

%-$(DPI)dpi.png: %.svg
	$(call svgpng,$(DPI),$<,alpha_$@)
	$(call flatten,alpha_$@, $@)
	-rm alpha_$@

