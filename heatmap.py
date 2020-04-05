By: AryaMedapati

x = np.arange(100)
y = np.arange(100)

fig, (ax, ax2) = plt.subplots(nrows=2, sharex=True)

extent = [x[0]-(x[1]-x[0])/2., x[-1]+(x[1]-x[0])/2.,0,1]
ax.imshow(y[np.newaxis,:], cmap="bone_r", aspect="auto", extent=extent)
ax.set_yticks([])
ax.set_xlim(extent[0], extent[1])

ax2.set_visible(False)
ax2.plot(x,y)
ax.set_xticklabels(['stink','bad','trend','strong'])

plt.tight_layout()
plt.show()
