import numpy as np
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 2, figsize=(10,6))
x=np.linspace(1,10,1000)
y=np.sin(x)
ax[0].plot(x, y)
ax[0].text(0.3, 0.4, 'Data: (0.3, 0.4)', transform=ax[0].transData)
ax[0].text(0.5, 0.5, 'Axes: (0.5, 0.5)', transform=ax[0].transAxes)
ax[0].text(0.8, 0.8, 'Figure: (0.3, 0.5)', transform=fig.transFigure)


ax[1].plot(x,y)

ax[1].text(0.3, 0.4, 'Data: (0.3, 0.4,)', transform=ax[1].transData)
ax[1].text(0.5, 0.5, 'Axes: (0.5, 0.5)', transform=ax[1].transAxes)
ax[1].text(0.8, 0.8, 'Figure: (0.3, 0.5,)', transform=fig.transFigure)
ax[1].set_xlim(-5,5)
ax[1].set_ylim(-2,2)

plt.show()


