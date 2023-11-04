import folium
from folium.plugins import MarkerCluster
import json

# Initialize the map with a location and zoom level
m = folium.Map(location=[44.934569, -123.034545], zoom_start=7)

# Load your GeoJSON file
with open("porthales.geojson", 'r') as f:
    geojson_data = json.load(f)

# Create a MarkerCluster object
marker_cluster = MarkerCluster().add_to(m)

# Function to create a formatted string of the GeoJSON properties as an HTML table
def format_popup(properties):
    html = '<table style="width:100%; border-collapse: collapse;" cellspacing="0" cellpadding="2">' \
           '<tbody>'
    for key, value in properties.items():
        html += f'<tr>' \
                f'<th style="text-align: left; vertical-align: top; padding: 3px; padding-right: 10px; border-bottom: 1px solid #ddd;">{key}:</th>' \
                f'<td style="text-align: left; vertical-align: top; padding: 3px; border-bottom: 1px solid #ddd;">{value}</td>' \
                f'</tr>'
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

# Add layer control to toggle on/off
folium.LayerControl().add_to(m)

# Save the map to an HTML file
m.save('porthales_of_salem.html')
