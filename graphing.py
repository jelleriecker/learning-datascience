import pandas as pd
import matplotlib.pyplot as plt

# Reading the data
df = pd.read_csv("/home/jelle/git/learning-datascience/wildlife-planes/database.csv")  

# Filter columns containing 'Damage' or 'Strike'
kind_of_incident = df.filter(like='Damage').columns.tolist() + df.filter(like='Strike').columns.tolist()
amount_of_incidents = df[kind_of_incident].sum()

# Calculate the total values for each kind of incident
total_values = df[kind_of_incident].sum()

# Create labels with total values
labels = [f'{col}: {total_values[col]}' for col in kind_of_incident]

# Group by 'Incident Year' and sum the incidents
yearly_incidents = df.groupby('Incident Year')[kind_of_incident].sum()

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(yearly_incidents.index, yearly_incidents.values)
plt.xlabel('Year')
plt.ylabel('Number of Incidents')
plt.title('Number of Incidents per Year')
plt.grid(True)
plt.xticks(np.arange(min(yearly_incidents.index), max(yearly_incidents.index)+1, 5.0))

# Adding a legend
plt.legend(labels, loc='upper left')

#plt.legend(['Aircraft Damage', 'Radome Damage', 'Windshield Damage', 'Nose Damage', 'Engine1 Damage', 'Engine2 Damage', 'Engine3 Damage', 'Engine4 Damage', 'Propeller Damage', 'Wing or Rotor Damage', 'Fuselage Damage', 'Landing Gear Damage', 'Tail Damage', 'Lights Damage', 'Other Damage', 'Radome Strike', 'Windshield Strike', 'Nose Strike', 'Engine1 Strike', 'Engine2 Strike', 'Engine3 Strike', 'Engine4 Strike', 'Propeller Strike', 'Wing or Rotor Strike', 'Fuselage Strike', 'Landing Gear Strike', 'Tail Strike', 'Lights Strike', 'Other Strike'], loc='upper left')

plt.show()

#print(kind_of_incident)