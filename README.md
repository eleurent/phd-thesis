# Safe and Efficient Reinforcement Learning for Behavioural Planning in Autonomous Driving

<table>
<tr>
<td>
<img alt="Social Attention" src="https://raw.githubusercontent.com/eleurent/phd-thesis/master/2-Chapters/4-Chapter/img/head_specialization.png">
</td>
<td>
<img alt="Risk Awareness" src="https://raw.githubusercontent.com/eleurent/phd-thesis/master/2-Chapters/5-Chapter/img/two-way-square.png">
</td>
<td>
<img alt="Robust Control" src="https://raw.githubusercontent.com/eleurent/phd-thesis/master/2-Chapters/7-Chapter/img/highway-small.png">
</td>
</tr>
</table>

This repository holds the LaTeX code of my PhD Thesis.

* Read the [**pdf** file](https://tel.archives-ouvertes.fr/tel-03035705) (for display on a screen :computer:);
* or the [print version](http://www.edouardleurent.com/pdf/phd-thesis-print.pdf) (for printing on paper :book:).

![Build LaTeX](https://github.com/eleurent/phd-thesis/workflows/Build%20LaTeX/badge.svg)


# Publications in this thesis

<table>
<tr>
<td>
<strong>Robust-Adaptive Control of Linear Systems: beyond Quadratic Costs</strong><br>
Edouard Leurent, Denis Efimov, and Odalric-Ambrym Maillard<br>
NeurIPS 2020<br>
<a href="https://arxiv.org/abs/2002.10816"><img alt="Paper" src="https://img.shields.io/badge/-Paper-gray"></a>
<a href="https://eleurent.github.io/robust-beyond-quadratic/"><img alt="Code" src="https://img.shields.io/badge/-Code-gray" ></a>
</td>
</tr>
<tr>
<td>
<strong>Monte-Carlo Graph Search: the Value of Merging Similar States</strong><br>
Edouard Leurent and Odalric-Ambrym Maillard<br>
ACML 2020<br>
<a href="http://proceedings.mlr.press/v129/leurent20a.html"><img alt="Paper" src="https://img.shields.io/badge/-Paper-gray"></a>
<a href="https://eleurent.github.io/monte-carlo-graph-search/"><img alt="Code" src="https://img.shields.io/badge/-Code-gray" ></a>
</td>
</tr>
<tr>
<td>
<strong>Robust-Adaptive Interval Predictive Control for Linear Uncertain Systems</strong><br>
Edouard Leurent, Denis Efimov, and Odlaric-Ambrym Maillard<br>
CDC 2020<br>
<a href="https://arxiv.org/abs/2007.10401"><img alt="Paper" src="https://img.shields.io/badge/-Paper-gray"></a>
<a href="https://github.com/eleurent/rl-agents"><img alt="Code" src="https://img.shields.io/badge/-Code-gray" ></a>
</td>
</tr>
<tr>
<td>
<strong>Budgeted Reinforcement Learning in Continuous State Space</strong><br>
Nicolas Carrara,* Edouard Leurent,* Romain Laroche, Tanguy Urvoy, Odalric-Ambrym Maillard, and Olivier Pietquin<br>
NeurIPS 2019<br>
<a href="https://proceedings.neurips.cc/paper/2019/hash/4fe5149039b52765bde64beb9f674940-Abstract.html"><img alt="Paper" src="https://img.shields.io/badge/-Paper-gray"></a>
<a href="https://budgeted-rl.github.io/"><img alt="Code" src="https://img.shields.io/badge/-Code-gray" ></a>
</td>
</tr>
<tr>
<td>
<strong>Social Attention for Autonomous Decision-Making in Dense Traffic</strong><br>
Edouard Leurent and Jean Mercat<br>
ML4AD Workshop at NeurIPS 2019<br>
<a href="https://arxiv.org/abs/1911.12250"><img alt="Paper" src="https://img.shields.io/badge/-Paper-gray"></a>
<a href="https://eleurent.github.io/social-attention/"><img alt="Code" src="https://img.shields.io/badge/-Code-gray" ></a>
</td>
</tr>
<tr>
<td>
<strong>Interval Prediction for Continuous-Time Systems with Parametric Uncertainties</strong><br>
Edouard Leurent, Denis Efimov, Tarek Raïssi, and Wilfrid Perruquetti<br>
CDC 2019<br>
<a href="https://arxiv.org/abs/1904.04727"><img alt="Paper" src="https://img.shields.io/badge/-Paper-gray"></a>
<a href="https://eleurent.github.io/interval-prediction/"><img alt="Code" src="https://img.shields.io/badge/-Code-gray" ></a>
</td>
</tr>
<tr>
<td>
<strong>Practical Open-Loop Optimistic Planning</strong><br>
Edouard Leurent and Odalric-Ambrym Maillard<br>
ECML-PKDD 2019<br>
<a href="https://arxiv.org/abs/1904.04700"><img alt="Paper" src="https://img.shields.io/badge/-Paper-gray"></a>
<a href="https://eleurent.github.io/kl-olop/"><img alt="Code" src="https://img.shields.io/badge/-Code-gray" ></a>
</td>
</tr>
</table>
* Equal contribution.


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
