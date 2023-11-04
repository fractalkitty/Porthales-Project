import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.io import output_notebook
from bokeh.models import ColumnDataSource
from bokeh.transform import factor_cmap

# Load data
df = pd.read_csv('porthales.csv')

# Aggregate data by 'Risk Level'
risk_level_counts = df['Risk Level'].value_counts().reset_index()
risk_level_counts.columns = ['Risk Level', 'Count']

# Sort data to ensure bars are in descending order
risk_level_counts.sort_values('Count', inplace=True, ascending=False)

# Define the output file (uncomment the line below if working with files)
output_file("risk_levels.html")

# Or define output to Jupyter notebook (uncomment the line below if working in a notebook)
# output_notebook()

# Create a ColumnDataSource from the DataFrame
source = ColumnDataSource(risk_level_counts)

# Create the figure

p = figure(x_range=risk_level_counts['Risk Level'], height=850, title="Risk Level Counts",
           toolbar_location=None, tools="")

# ... [your previous code for creating the vbar glyph] ...

# Rotate the x-axis labels
p.xaxis.major_label_orientation = 45 

# Add a vbar glyph to the figure
p.vbar(x='Risk Level', top='Count', width=0.9, source=source,
       legend_field="Risk Level",
       line_color='white',
       fill_color=factor_cmap('Risk Level', palette='Spectral6', factors=risk_level_counts['Risk Level']))

# Set some properties to make the plot look better
p.xgrid.grid_line_color = None
p.legend.orientation = "horizontal"
p.legend.location = "top_center"

# Show the plot
show(p)
