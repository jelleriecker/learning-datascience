from bokeh.plotting import figure, show

import pandas as pd

covid_df = pd.read_csv("covid-19-global-data.csv")

x=covid_df["Cumulative_cases"]
y=covid_df.loc[covid_df["Contry"] == Argentina]


output_file("bokeh.html")
fig1 = figure()
fig1.line(x,y)


show()
