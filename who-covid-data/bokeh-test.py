import pandas as pd
from bokeh.plotting import figure, show
from bokeh.models import YearsTicker

# Data variables
df = pd.read_csv("covid-19-global-data.csv")
df_arg = df.loc[df["Country"] == "Argentina", :]


#df_arg = df.loc[(df['Country'] == 'Argentina') & (df['Date_reported'])]

# Plot variables
x = pd.date_range(start='2019-1-1', periods=7, freq='YE')
y = pd.to_numeric((df_arg['Cumulative_cases']))



# from here we create the plot
plot1 = figure(x_axis_type="datetime", title="covid cases Argentina", plot_height=350, plot_width=800)#title="cumulative cases Argentina", x_axis_label='Date reported', y_axis_label='cumulative cases')
plot1.xaxis.ticker = YearsTicker(interval=1)
plot1.line(x, y)

# Here we show the plot
show(plot1)

