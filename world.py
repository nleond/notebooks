import pandas as pd
import geopandas

world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))

world.head()

world.plot()
print(world.geometry.name)

world = world.rename(columns={'geometry': 'borders'}).set_geometry('borders')

print(world.geometry.name)

world['centroid_column'] = world.centroid

world = world.set_geometry('centroid_column')

#world.plot()