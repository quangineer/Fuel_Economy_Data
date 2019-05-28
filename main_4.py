import pandas as pd
df_08 = pd.read_csv('data_08_v3.csv')
df_18 = pd.read_csv('data_18_v3.csv')

# Figure out what happens? To fix air_pollution_score column, there is a problem associated with a cell in this Series. The cell has an index 582 in which
# the value is 6/4. This is because a vehicle can operate on more than one type of fuel, thus this cell hold two values to reflect on it. Each value is 
# separated by '/'. 

# First, we need to know which row containing this cells in both df_08 and df_18:
# We call this variable hb_08 and hb_18 to demonstrate this kind of car is hybrids (hb)

hb_08 = df_08[df_08['fuel'].str.contains('/')]  # pull out all the cell that has the value containing '/'
hb_18 = df_18[df_18['fuel'].str.contains('/')]

