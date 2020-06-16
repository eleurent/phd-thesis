"""
====
XKCD
====

Shows how to create an xkcd-like plot.
"""
import matplotlib.pyplot as plt
import numpy as np

def rectangle(ax, A, B, label):
    x, y = [A[0], A[0], B[0], B[0], A[0]], [A[1], B[1], B[1], A[1], A[1]]
    ax.plot(x, y, c="black")
    ax.text((A[0]+B[0])/2, (A[1]+B[1])/2,
        label,
        ha='center')

with plt.xkcd():
    # Based on "The Data So Far" from XKCD by Randall Munroe
    # https://xkcd.com/373/
    model_based = 0
    model_free = 0.6
    case_study = 1.2
    sample_efficiency = 0
    safety = 1
    chap23 = np.array([(sample_efficiency + safety) / 2, case_study])
    chap4 = np.array([sample_efficiency, model_free])
    chap5 = np.array([safety, model_free])
    chap6 = np.array([sample_efficiency, model_based])
    chap7 = np.array([safety, model_based])
    margins = np.array([0.3, 0.2])
    big_margins = np.array([0.6, 0.2])

    fig = plt.figure()
    ax = fig.add_axes((0.25, 0.12, 0.7, 0.8))
    rectangle(ax, chap23 - big_margins, chap23 + big_margins, "Chapters 2 and 3")
    rectangle(ax, chap4 - margins, chap4 + margins, "Chapter 4")
    rectangle(ax, chap5 + margins, chap5 - margins, "Chapter 5")
    rectangle(ax, chap6 + margins, chap6 - margins, "Chapter 6")
    rectangle(ax, chap7 - margins, chap7 + margins, "Chapter 7")
    ax.arrow(chap4[0] + margins[0], chap4[1], (chap5 - chap4)[0] - 2 * margins[0] - 0.1, (chap5 - chap4)[1],
             head_width=0.05, facecolor="black")
    ax.arrow(chap6[0] + margins[0], chap6[1], (chap7 - chap6)[0] - 2 * margins[0] - 0.1, (chap5 - chap4)[1],
             head_width=0.05, facecolor="black")
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.set_xticks([sample_efficiency, safety])
    ax.set_xticklabels(['Sample\nefficiency', 'Safety'])
    ax.set_xlim([-0.5, 1.5])
    ax.yaxis.set_ticks_position('left')
    ax.set_yticks([model_based, model_free, case_study])
    ax.set_yticklabels(['Model-based\nMethods', 'Model-Free\nMethods', 'Case study'])
    ax.set_ylim([-0.5, 1.5])

    ax.set_title("Thesis Outline")

    # fig.text(
    #     0.5, 0.05,
    #     '"The Data So Far" from xkcd by Randall Munroe',
    #     ha='center')

plt.savefig("outline.pdf")
plt.show()
