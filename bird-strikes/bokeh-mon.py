import numpy as np
import pandas as pd
import pandas_bokeh as pdb
from bokeh.plotting import figure, show

from bokeh.models.widgets import DataTable, TableColumn
from bokeh.models import ColumnDataSource



df = pd.read_csv("database.csv")

#column_names = df.columns.tolist()

x = df['Incident Day']
y = df['Engine1 Strike']

plot1 = figure(title="Bird Strikes", x_axis_label='Year', y_axis_label='Fatalities')
plot1.line(x, y, legend_label="Bird Strikes", line_width=2)

show(plot1)
