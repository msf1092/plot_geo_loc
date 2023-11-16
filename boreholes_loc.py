# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 21:59:30 2023

@author: qdmofa
"""

import pyproj
import cartopy.crs as ccrs
import matplotlib.pyplot as plt

# Define the current projection (UTM zone 35V, for example) and the target projection (WGS84)
proj_current = pyproj.Proj(proj='utm', zone=35, ellps='WGS84')
proj_wgs84 = pyproj.Proj(proj='latlong', datum='WGS84')

# Function to convert coordinates
def convert_coordinates(x, y):
    lon, lat = pyproj.transform(proj_current, proj_wgs84, x, y)
    return lon, lat

# Borehole coordinates
boreholes = {
    'S010': convert_coordinates(230004.9357 , 6818890.2970),
    'S020': convert_coordinates(230006.7493 , 6818889.4553)
}

# CPT loggings coordinates
cpt_loggings = {
    'CP040': convert_coordinates(230008.3853 , 6818890.6054),
    'CP030': convert_coordinates(230009.7135 , 6818886.9771),
    'CV020': convert_coordinates(230006.9272 , 6818887.4631)
}

# Create a figure with horizontal orientation
fig = plt.figure(figsize=(10, 5))

# Create a GeoAxes in the tile's projection
ax = plt.axes(projection=ccrs.PlateCarree())

# Add the satellite image
ax.stock_img()

# Plot boreholes
for name, coord in boreholes.items():
    ax.plot(coord[0], coord[1], 'bo', markersize=10, transform=ccrs.PlateCarree())
    #plt.text(coord[0], coord[1], name, fontsize=12, ha='right', transform=ccrs.PlateCarree())

# Plot CPT loggings
for name, coord in cpt_loggings.items():
    ax.plot(coord[0], coord[1], 'r^', markersize=10, transform=ccrs.PlateCarree())
    #plt.text(coord[0], coord[1], name, fontsize=12, ha='right', transform=ccrs.PlateCarree())

plt.show()
#%%
import pyproj
import cartopy.crs as ccrs
import matplotlib.pyplot as plt

# Define the current projection (UTM zone 35V, for example) and the target projection (WGS84)
proj_current = pyproj.Proj(proj='utm', zone=35, ellps='WGS84')
proj_wgs84 = pyproj.Proj(proj='latlong', datum='WGS84')

# Function to convert coordinates
def convert_coordinates(x, y):
    lon, lat = pyproj.transform(proj_current, proj_wgs84, x, y)
    return lon, lat

# Borehole coordinates
boreholes = {
    'S010': convert_coordinates(230004.9357 , 6818890.2970),
    'S020': convert_coordinates(230006.7493 , 6818889.4553)
}

# CPT loggings coordinates
cpt_loggings = {
    'CP040': convert_coordinates(230008.3853 , 6818890.6054),
    'CV020': convert_coordinates(230006.9272 , 6818887.4631),
    'CV050': convert_coordinates(230003.1215, 6818891.1387)
}

# Create a figure with horizontal orientation
fig = plt.figure(figsize=(5, 3))

# Create a GeoAxes in the tile's projection
ax = plt.axes(projection=ccrs.PlateCarree())

# Set the extent of the map to the minimum and maximum longitude and latitude of your points
min_lon = min(lon for lon, lat in list(boreholes.values()) + list(cpt_loggings.values())) - 0.00002
min_lat = min(lat for lon, lat in list(boreholes.values()) + list(cpt_loggings.values())) - 0.00002
max_lon = max(lon for lon, lat in list(boreholes.values()) + list(cpt_loggings.values())) + 0.00002
max_lat = max(lat for lon, lat in list(boreholes.values()) + list(cpt_loggings.values())) + 0.00002

ax.set_extent([min_lon, max_lon, min_lat, max_lat], crs=ccrs.PlateCarree())

# Add the satellite image
ax.stock_img()

# Add a north arrow
x, y, arrow_length = 0.95, 0.28, 0.2
ax.annotate('N', xy=(x, y), xytext=(x, y-arrow_length),
            arrowprops=dict(facecolor='black', width=5, headwidth=15),
            ha='center', va='center', fontsize=20,
            xycoords=ax.transAxes)

# Add gridlines with labels
gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True)
gl.top_labels = False
gl.right_labels = False

# Plot boreholes
for name, coord in boreholes.items():
    ax.plot(coord[0], coord[1], 'bo', markersize=10, transform=ccrs.PlateCarree())
    plt.text(coord[0], coord[1], name, fontsize=12, ha='right', transform=ccrs.PlateCarree())

# Plot CPT loggings
for name, coord in cpt_loggings.items():
    ax.plot(coord[0], coord[1], 'r^', markersize=10, transform=ccrs.PlateCarree())
    plt.text(coord[0], coord[1], name, fontsize=12, ha='right', transform=ccrs.PlateCarree())

# Save the figure before you call plt.show()
# plt.savefig('C:/Users/qdmofa/OneDrive - TUNI.fi/Fincone II-adjunct/Asli/FINCONE II - Dissemination/X-ray microtomography/Article/Figures/Boreholes locations/figure.svg', format='svg')
# plt.savefig('path_to_your_folder/figure.eps', format='eps')
plt.savefig('C:/Users/qdmofa/OneDrive - TUNI.fi/Fincone II-adjunct/Asli/FINCONE II - Dissemination/X-ray microtomography/Article/Figures/Boreholes locations/figure.png', format='png')



plt.show()
#%% Showing the UTM coordinates at the gridlines (it did not work here, on my computer!)
import matplotlib.ticker as mticker
import pyproj
import cartopy.crs as ccrs
import matplotlib.pyplot as plt

# Define the current projection (UTM zone 35V, for example) and the target projection (WGS84)
proj_current = pyproj.Proj(proj='utm', zone=35, ellps='WGS84')
proj_wgs84 = pyproj.Proj(proj='latlong', datum='WGS84')

# Function to convert coordinates
def convert_coordinates(x, y):
    lon, lat = pyproj.transform(proj_current, proj_wgs84, x, y)
    return lon, lat

# Borehole coordinates
boreholes = {
    'S010': convert_coordinates(230004.9357 , 6818890.2970),
    'S020': convert_coordinates(230006.7493 , 6818889.4553)
}

# CPT loggings coordinates
cpt_loggings = {
    'CP040': convert_coordinates(230008.3853 , 6818890.6054),
    'CV020': convert_coordinates(230006.9272 , 6818887.4631),
    'CV050': convert_coordinates(230003.1215, 6818891.1387)
}

# Create a figure with horizontal orientation
fig = plt.figure(figsize=(10, 5))

# Create a GeoAxes in the tile's projection
ax = plt.axes(projection=ccrs.PlateCarree())

# Set the extent of the map to the minimum and maximum longitude and latitude of your points
min_lon = min(lon for lon, lat in list(boreholes.values()) + list(cpt_loggings.values())) - 0.00002
min_lat = min(lat for lon, lat in list(boreholes.values()) + list(cpt_loggings.values())) - 0.00002
max_lon = max(lon for lon, lat in list(boreholes.values()) + list(cpt_loggings.values())) + 0.00002
max_lat = max(lat for lon, lat in list(boreholes.values()) + list(cpt_loggings.values())) + 0.00002

ax.set_extent([min_lon, max_lon, min_lat, max_lat], crs=ccrs.PlateCarree())

# Add the satellite image
ax.stock_img()

# Add gridlines without labels
gl = ax.gridlines(draw_labels=False)

# Manually add UTM labels
xticks = mticker.FixedLocator([min_lon, max_lon])
yticks = mticker.FixedLocator([min_lat, max_lat])
ax.xaxis.set_major_locator(xticks)
ax.yaxis.set_major_locator(yticks)
ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, pos: f'{x}E'))
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda y, pos: f'{y}N'))

# Plot boreholes
for name, coord in boreholes.items():
    ax.plot(coord[0], coord[1], 'bo', markersize=10, transform=ccrs.PlateCarree())
    plt.text(coord[0], coord[1], name, fontsize=12, ha='right', transform=ccrs.PlateCarree())

# Plot CPT loggings
for name, coord in cpt_loggings.items():
    ax.plot(coord[0], coord[1], 'r^', markersize=10, transform=ccrs.PlateCarree())
    plt.text(coord[0], coord[1], name, fontsize=12, ha='right', transform=ccrs.PlateCarree())

plt.show()
#%% LaTEX (it did not work!)
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import cartopy.crs as ccrs
import pyproj

# Enable LaTeX for all text
matplotlib.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
})

# Define the current projection (UTM zone 35V, for example) and the target projection (WGS84)
proj_current = pyproj.Proj(proj='utm', zone=35, ellps='WGS84')
proj_wgs84 = pyproj.Proj(proj='latlong', datum='WGS84')

# Function to convert coordinates
def convert_coordinates(x, y):
    lon, lat = pyproj.transform(proj_current, proj_wgs84, x, y)
    return lon, lat

# Borehole coordinates
boreholes = {
    'S010': convert_coordinates(229506.5845 , 6818890.5484),
    'S020': convert_coordinates(229504.7704 , 6818891.3904)
}

# CPT loggings coordinates
cpt_loggings = {
    'CP040': convert_coordinates(230008.3853 , 6818890.6054),
    'CP030': convert_coordinates(230009.7135 , 6818886.9771),
    'CV020': convert_coordinates(230006.9272 , 6818887.4631)
}

# Create a figure with horizontal orientation
fig = plt.figure(figsize=(10, 5))

# Create a GeoAxes in the tile's projection
ax = plt.axes(projection=ccrs.PlateCarree())

# Set the extent of the map to the minimum and maximum longitude and latitude of your points
min_lon = min(lon for lon, lat in list(boreholes.values()) + list(cpt_loggings.values())) - 0.01
min_lat = min(lat for lon, lat in list(boreholes.values()) + list(cpt_loggings.values())) - 0.01
max_lon = max(lon for lon, lat in list(boreholes.values()) + list(cpt_loggings.values())) + 0.01
max_lat = max(lat for lon, lat in list(boreholes.values()) + list(cpt_loggings.values())) + 0.01

ax.set_extent([min_lon, max_lon, min_lat, max_lat], crs=ccrs.PlateCarree())

# Add the satellite image
ax.stock_img()

# Add a north arrow at the southeast of the plot
x, y, arrow_length = 0.95, 0.05, 0.1
ax.annotate('$\\mathbf{N}$', xy=(x, y), xytext=(x, y+arrow_length),
            arrowprops=dict(facecolor='black', width=1, headwidth=10, alpha=0.7),
            ha='center', va='center', fontsize=20,
            xycoords=ax.transAxes)

# Plot boreholes
for name, coord in boreholes.items():
    ax.plot(coord[0], coord[1], 'bo', markersize=10, transform=ccrs.PlateCarree())
    plt.text(coord[0], coord[1], f'$\\textbf{{{name}}}$', fontsize=12, ha='right', transform=ccrs.PlateCarree())

# Plot CPT loggings
for name, coord in cpt_loggings.items():
    ax.plot(coord[0], coord[1], 'r^', markersize=10, transform=ccrs.PlateCarree())
    plt.text(coord[0], coord[1], f'$\\textbf{{{name}}}$', fontsize=12, ha='right', transform=ccrs.PlateCarree())

plt.show()

