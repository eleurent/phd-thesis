# phd-thesis
![Build LaTeX](https://github.com/eleurent/phd-thesis/workflows/Build%20LaTeX/badge.svg)

This repository hold the source code of my PhD Thesis, entitled

<p align="center"><em>Safe and Efficient Reinforcement Learning for Behavioural Planning in Autonomous Driving</em>.</p>

The pdf  is available at the following links:
* Default version :construction: for display on a screen :computer:;
* Print version :construction: for printing on paper :book:.

## Defense

I defended on the 30th of October 2020, in front of the jury composed of:

* Lucian Buşoniu
* Jorge Villagra
* Luce Brotcorne
* Marc Deisenroth
* Denis Efimov
* Odalric-Ambrym Maillard

The slides :newspaper: that I used are also [available online](https://eleurent.github.io/phd-defense/), and [open-source](https://github.com/eleurent/phd-defense).


## How to build the PDF?

I recommend using [latexmk](https://www.ctan.org/pkg/latexmk/) to build this project.

```latexmk -pdf PhD_thesis__Edouard_Leurent.tex```

It is used _e.g._ in the [latex-action](https://github.com/xu-cheng/latex-action) of the automatic [build workflow](/.github/workflows/main.yml).
LaTeX editors such as [Texstudio](https://www.texstudio.org/) can be configured to use latexmk as the default compiler.

## Credits

The template is inspired from [@Naereen/phd-thesis](https://github.com/Naereen/phd-thesis), also released under the MIT License.