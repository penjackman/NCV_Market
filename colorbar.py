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

#Below is working color bar with labels and arrow

fig, ax = plt.subplots(figsize=(6, 1))
fig.subplots_adjust(bottom=0.5)

cmap = mpl.cm.plasma
# labels = ('Dreadful', 'Poor', 'Mediocre', 'Good', 'Excellent', 'Phenomenal')
norm = mpl.colors.Normalize(vmin=0 ,vmax=10)
trans = ax.get_yaxis_transform()
final = round(score, 2)
ann = ax.annotate(str(final), xy=(score/10,-0.2), xycoords=trans, xytext=(score/10, -0.3), textcoords='axes fraction', color='orange',
arrowprops=dict(color='orange', shrink=0.0, width=0.5, headwidth=3.5, headlength=3.5), 
horizontalalignment='center', verticalalignment='baseline',)

cb1 = mpl.colorbar.ColorbarBase(ax, cmap=cmap, norm=norm, orientation='horizontal')
# cb1.ax.set_xticklabels(labels)
plt.show()

cb1 = mpl.colorbar.ColorbarBase(ax, cmap=cmap, norm=norm, orientation='horizontal')
# cb1.ax.set_xticklabels(labels)
plt.show()
