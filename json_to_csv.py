import json
import pandas as pd

# Load GeoJSON file
with open('porthales.geojson', 'r') as f:
    geojson = json.load(f)

# Check if the file contains 'features' and it's a list
if not isinstance(geojson.get('features', None), list):
    raise ValueError("GeoJSON does not seem to be valid, or it doesn't contain features list.")

# Extract feature properties (and optionally geometry)
features = geojson['features']
data_rows = []

for feature in features:
    properties = feature['properties']  # This is a dictionary of all properties
    # Optionally, extract geometry (e.g., if it's a Point)
    geometry = feature.get('geometry', None)
    if geometry and geometry['type'] == 'Point':
        # For Point, extract the coordinates
        properties['longitude'], properties['latitude'] = geometry['coordinates']
    elif geometry and geometry['type'] in ['LineString', 'Polygon']:
        # If you want to extract other types of geometry, handle them here
        pass

    data_rows.append(properties)

# Convert to a pandas DataFrame
df = pd.DataFrame(data_rows)

# Write to a CSV file
df.to_csv('complete_data.csv', index=False)


