import numpy as np
import pandas as pd
import pandas_bokeh as pdb

from bokeh.models.widgets import DataTable, TableColumn
from bokeh.models import ColumnDataSource



df = pd.read_csv("database.csv")

column_names = df.columns.tolist()


df2 = pd.DataFrame(df).set_index














#df['Incident Date'] = pd.to_datetime(df['Incident Year', 'Incident Month', 'Incident Day'], format='%Ymm%d')

#kind_of_incident = df.filter(like='Damage').columns.tolist() + df.filter(like='Strike').columns.tolist()
#amount_of_incidents = df[kind_of_incident].sum()
#total_values = df[kind_of_incident].sum()
#yearly_incidents = df.groupby('Incident Year')[kind_of_incident].sum()

