# phd-thesis
![Build LaTeX](https://github.com/eleurent/phd-thesis/workflows/Build%20LaTeX/badge.svg)

The template is inspired from [@Naereen/phd-thesis](https://github.com/Naereen/phd-thesis), also released under the MIT License.

## How to build the PDF?

I recommend using [latexmk](https://www.ctan.org/pkg/latexmk/) to build this project.

```latexmk -pdf PhD_thesis__Edouard_Leurent.tex```

LaTeX editors such as [Texstudio](https://www.texstudio.org/) can be configured to latexmk as the default compiler.
It is also used in the [latex-action](https://github.com/xu-cheng/latex-action) of the automatic [build workflow](/.github/workflows/main.yml).
