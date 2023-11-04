import geopandas as gpd

# Load the GeoJSON into a GeoDataFrame
gdf = gpd.read_file("porthales_of_salem.geojson")

# List of keys to remove
keys_to_remove = ['UNITTYPE', 'RIMELEV', 'MAINTAINEDBY', 'UNITID', 'CREATED_USER','LOCATION','CREATED_DATE','LAST_EDITED_USER','LAST_EDITED_DATE','PROJECTNO','PERMIT','ORIFICEDIAMETER','WARRANTYDATE','CONDITION','CONDITIONDATE','EXPECTEDLIFE','IPSUNITID','HANSENID']

# Drop the unwanted keys (make sure they exist in the dataframe to avoid KeyError)
gdf = gdf.drop(columns=keys_to_remove, errors='ignore')  # 'errors=ignore' will ignore any non-existing keys

# Save the modified GeoDataFrame to a new GeoJSON file
gdf.to_file("porthales-final.geojson", driver="GeoJSON")
