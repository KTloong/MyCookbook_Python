import matplotlib.pyplot as plt

import geopandas
boros = geopandas.read_file(r"C:\Users\kingl\Desktop\SHP\1520.shp")
boros.set_index('FID_', inplace=True)
boros.sort_index()
boros.plot()
plt.show()
