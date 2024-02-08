import pandas as pd
from bokeh.plotting import figure, show 
from bokeh.models import YearsTicker, Range1d

# Data variables
df = pd.read_csv("covid-19-global-data.csv")
df_arg = df.loc[df["Country"] == "Argentina", :]

#df_arg = df.loc[(df['Country'] == 'Argentina') & (df['Date_reported'])]

# Plot variables
x1 = pd.to_datetime(df_arg['Date_reported'])
y1 = pd.to_numeric(df_arg['Cumulative_cases'])

# from here we create the plot
plot1 = figure(x_axis_type="datetime", title="covid cases Argentina", height=800, width=800)
plot1.xaxis.axis_label = "Year"
#plot1.xaxis.ticker = YearsTicker()
plot1.yaxis.axis_label = "Cases"
plot1.line(x1, y1)

# Here we show the plot
show(plot1)

