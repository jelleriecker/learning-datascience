import pandas as pd
from bokeh.plotting import figure, show

# Data variables
df = pd.read_csv("covid-19-global-data.csv")
df_arg = df.loc[df["Country"] == "Argentina", :]


#df_arg = df.loc[(df['Country'] == 'Argentina') & (df['Date_reported'])]

# Plot variables
x = pd.to_datetime(df_arg['Date_reported'])
y = pd.to_numeric((df_arg['Cumulative_cases']))

print(x, y)

# from here we create the plot
plot1 = figure()#title="cumulative cases Argentina", x_axis_label='Date reported', y_axis_label='cumulative cases')
plot1.line(x, y)# legend_label="cases", line_width=2)

# Here we show the plot
show(plot1)
