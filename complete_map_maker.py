import folium
import json
from folium.plugins import MarkerCluster

# Initialize the map with a location and zoom level
m = folium.Map(location=[44.934569, -123.034545], zoom_start=7)

# Load your point GeoJSON file
with open("porthales.geojson", 'r') as f:
    geojson_data = json.load(f)

# Create a FeatureGroup for the porthales layer, off by default
porthales_group = folium.FeatureGroup(name='Porthales', show=True)
# Create a MarkerCluster object
marker_cluster = MarkerCluster()

# Function to create a formatted string of the GeoJSON properties as an HTML table
def format_popup(properties):
    html = '<table style="width:100%; border-collapse: collapse;" cellspacing="0" cellpadding="2"><tbody>'
    for key, value in properties.items():
        html += f'<tr><th style="text-align: left; vertical-align: top; padding: 3px; padding-right: 10px; border-bottom: 1px solid #ddd;">{key}:</th><td style="text-align: left; vertical-align: top; padding: 3px; border-bottom: 1px solid #ddd;">{value}</td></tr>'
    html += '</tbody></table>'
    return html

# Loop through the features in the GeoJSON file
for feature in geojson_data['features']:
    if feature['geometry']['type'] == 'Point':
        # Extract the latitude and longitude from the GeoJSON file
        lon, lat = feature['geometry']['coordinates']
        # Extract properties
        properties = feature['properties']
        # Create a formatted string for the popup
        popup_content = format_popup(properties)
        # Add a marker to the cluster with the popup
        folium.Marker(
            [lat, lon],
            popup=popup_content
        ).add_to(marker_cluster)

# Add the MarkerCluster to the porthales group, then add the group to the map
porthales_group.add_child(marker_cluster)
m.add_child(porthales_group)

# Load your ellipses GeoJSON file
with open("ellipses.geojson", 'r') as g:
    ellipses_geojson_data = json.load(g)

# Function to style the ellipses
def style_function(feature):
    return {
        'fillColor': '#blue',  # Fill color of the ellipse
        'color': 'blue',       # Border color of the ellipse
        'weight': 2,           # Border width
        'fillOpacity': 0.2,    # Fill opacity
    }

# Add each ellipse as a separate layer, off by default
for feature in ellipses_geojson_data['features']:
    # Create a FeatureGroup for this ellipse, off by default
    ellipse_group = folium.FeatureGroup(name=f"Ellipse {feature['properties']['name']}", show=False)
    # Create a GeoJson object for the ellipse and add it to its FeatureGroup
    folium.GeoJson(
        feature,
        style_function=style_function
    ).add_to(ellipse_group)
    # Add the FeatureGroup to the map
    m.add_child(ellipse_group)

# Add layer control to toggle layers on/off
folium.LayerControl().add_to(m)

# Save the map to an HTML file
m.save('complete_map.html')
