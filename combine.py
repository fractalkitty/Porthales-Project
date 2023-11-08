# Purpose: Combine a GeoJSON file with a CSV file
import pandas as pd
import geopandas as gpd

# Load the GeoJSON
gdf = gpd.read_file("Public_Storm_Manhole.geojson")

# Load the CSV
pdf = pd.read_csv("porthales.csv")

# Merge the CSV data into the GeoJSON data
# Specify 'left_on' and 'right_on' to use different key column names
joined_gdf = gdf.merge(pdf, left_on="UNITID", right_on="ID")

# Save the merged GeoDataFrame to a new GeoJSON file
joined_gdf.to_file("porthales_of_salem.geojson", driver="GeoJSON")
