#  By:AryaMedapati

import matplotlib.pyplot as plt
import matplotlib as mpl

# Below is empty heat map with covered graph
# x = np.arange(100)
# y = np.arange(100)

# fig, (ax, ax2) = plt.subplots(nrows=2, sharex=True)

# extent = [x[0]-(x[1]-x[0])/2., x[-1]+(x[1]-x[0])/2.,0,1]
# ax.imshow(y[np.newaxis,:], cmap="bone_r", aspect="auto", extent=extent)
# ax.set_yticks([])
# ax.set_xlim(extent[0], extent[1])

# ax2.set_visible(False)
# ax2.plot(x,y)
# ax.set_xticklabels(['stink','bad','trend','strong'])

# plt.tight_layout()
# plt.show()

#Below is working color bar with labels

fig, ax = plt.subplots(figsize=(6, 1))
fig.subplots_adjust(bottom=0.5)

cmap = mpl.cm.plasma
labels = ('Dreadful', 'Poor', 'Mediocre', 'Good', 'Excellent', 'Phenomenal')

cb1 = mpl.colorbar.ColorbarBase(ax, cmap=cmap, orientation='horizontal')
cb1.set_label('Color Bar/Heat Map')
cb1.ax.set_xticklabels(labels)
plt.show()
