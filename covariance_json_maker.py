import pandas as pd
import numpy as np
from shapely.geometry import Point, mapping
from scipy.stats import chi2
import json

# Function to calculate the oriented ellipse
def calculate_ellipse(center, cov_matrix, scale):
    # Calculate the eigenvalues and eigenvectors
    eigenvalues, eigenvectors = np.linalg.eigh(cov_matrix)
    
    # Eigenvalues give the length of the ellipse axes
    axis_length = np.sqrt(eigenvalues * scale)

    # Eigenvectors give the orientation of the ellipse
    angle = np.arctan2(*eigenvectors[:,0][::-1])

    # Generate ellipse points
    t = np.linspace(0, 2 * np.pi, 100)
    ellipse = np.array([center + np.array([
        axis_length[0] * np.cos(t) * np.cos(angle) - axis_length[1] * np.sin(t) * np.sin(angle),
        axis_length[0] * np.cos(t) * np.sin(angle) + axis_length[1] * np.sin(t) * np.cos(angle)
    ]).T for t in t])

    return ellipse

# Load CSV data
df = pd.read_csv('complete_data.csv')

# Calculate the centroid
centroid = df[['longitude', 'latitude']].mean().values

# Calculate covariance matrix of the coordinates
cov_matrix = np.cov(df['longitude'], df['latitude'])

# Prepare the GeoJSON structure
geojson = {
    "type": "FeatureCollection",
    "features": []
}

# Add centroid to GeoJSON
centroid_feature = {
    "type": "Feature",
    "geometry": mapping(Point(centroid[0], centroid[1])),
    "properties": {"name": "centroid"}
}
geojson["features"].append(centroid_feature)

# Sigma values for confidence ellipses (1, 2, 3-sigma)
sigma_values = chi2.ppf([0.6827, 0.9545, 0.9973], 2)

# Add ellipses to GeoJSON
for scale in sigma_values:
    # Calculate ellipse points
    ellipse = calculate_ellipse(centroid, cov_matrix, scale)
    
    # Convert ellipse points to a Polygon and add to GeoJSON
    ellipse_feature = {
        "type": "Feature",
        "geometry": {
            "type": "Polygon",
            "coordinates": [ellipse.tolist()]
        },
        "properties": {"name": f"{np.sqrt(scale)}-sigma ellipse"}
    }
    geojson["features"].append(ellipse_feature)

# Save GeoJSON to a file
with open('ellipses.geojson', 'w') as f:
    json.dump(geojson, f)

# print("Centroid and ellipses have been saved to 'ellipses.geojson'.")
