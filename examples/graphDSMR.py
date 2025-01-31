import pandas as pd
import matplotlib.pyplot as plt
import mplcursors

df = pd.read_csv('/home/leo/Desktop/gr-dsmr-rc/examples/channel_data.csv')

right_artist = df.plot(x = 'Time', ylim=(-1,1))

plt.locator_params(axis='y', nbins=20)

c1 = mplcursors.cursor(right_artist, hover=True)
@c1.connect("add")
def _(sel):
    sel.annotation.get_bbox_patch().set(fc="white")
    sel.annotation.arrow_patch.set(arrowstyle=None, fc="white", alpha=.5)

plt.show()