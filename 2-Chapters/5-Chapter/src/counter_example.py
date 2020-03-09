import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# sns.set()
# sns.set_style("white")
plt.rc('text', usetex=True)
plt.rc('font', family='serif', size=15)

eps = 0.5
beta = eps

Q1 = np.array([[0, eps], [0, 1]])
Q2 = np.array([[eps, 2*eps], [0, 1]])

fig = plt.figure(figsize=(3, 3))
ax = fig.add_subplot(1, 1, 1)
plt.plot(Q1[0], Q1[1], marker='.', markersize=12)
plt.plot(Q2[0], Q2[1], marker='.', markersize=12)
# plt.legend(["Q1", "Q2"])
plt.text(eps+0.01, 1/2, r'$\beta$', rotation=0, horizontalalignment="left", verticalalignment="center")

plt.axis('equal')

xticks = [0, eps, 2*eps]
plt.xticks(xticks, ('0', r'$\epsilon$', r'$2\epsilon$'))
yticks = [0, 1]
plt.yticks(yticks, ('0', r'$\frac{1}{\gamma}$'))

xticks_grid = [beta]
ax.set_xticks(xticks_grid, minor=True)
ax.grid(which='minor')
plt.ylim([0, 1])
# plt.tight_layout(pad=0.4, w_pad=0.4, h_pad=0.)
plt.subplots_adjust(left=0.25, bottom=0.2)

plt.xlabel(r"$Q_c$")
plt.ylabel(r"$Q_r$")

plt.savefig("concavity_example.pdf")
plt.show()
