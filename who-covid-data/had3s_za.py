from bokeh.io import output_file
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource
import pandas as pd
 
# Load CSV data using pandas
df = pd.read_csv("covid-19-global-data.csv")
x = pd.to_datetime(df["Date_reported"])
#y = pd.to_numeric(df["Cumulative_cases"])
df_arg = df.loc[df["Country"] == "Argentina", :]
y = pd.to_numeric((df_arg["Cumulative_cases"]))
output_file("had3s_za.html")
fig1 = figure()
fig1.line(x,y)
show(fig1)