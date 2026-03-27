import pandas as pd
data = {
    "State": ["Maharashtra", "Gujarat", "Karnataka", "Tamil Nadu", "Rajasthan"],
    "Area": [307713, 196244, 191791, 130058, 342239],  # in sq km
    "Population": [124000000, 70000000, 68000000, 75000000, 81000000]
}
df = pd.DataFrame(data)
print("\nState Information:\n")
print(df)
largest_area = df.loc[df['Area'].idxmax()]
print("\nState with Largest Area:")
print(largest_area['State'])
largest_pop = df.loc[df['Population'].idxmax()]
print("\nState with Largest Population:")
print(largest_pop['State'])
df['Density'] = df['Population'] / df['Area']
print("\nPopulation Density of States:\n")
print(df[['State', 'Density']])
highest_density = df.loc[df['Density'].idxmax()]
print("\nState with Highest Population Density:")
print(highest_density['State'])