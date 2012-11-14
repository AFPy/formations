#!/bin/sh
git clone git@github.com:AFPy/formations.git gh-pages
cd gh-pages
git checkout gh-pages
rm -Rf basic
../bin/impress -i ../basic/index.rst -o basic
git add -A
git commit -m "update docs"
git push origin gh-pages
cd ..
rm -Rf gh-pages
