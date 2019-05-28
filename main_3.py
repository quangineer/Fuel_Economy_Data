import pandas as pd 

df_08 = pd.read_csv('data_08_v2.csv')
df_18 = pd.read_csv('data_18_v2.csv')

df_08['cyl'].value_counts() #Count the number of each unique value in a column

df_18['cyl'].value_counts() #Count the number of each unique value in a column

# Extract int from strings in the 2008 cyl column:

df_08['cyl']= df_08['cyl'].str.extract('(\d+)').astype(int)

# Convert 2018 cyl column to int:
df_18['cyl']= df_18['cyl'].astype(int)

df_08.to_csv('data_08_v3.csv', index=False)
df_18.to_csv('data_18_v3.csv', index=False)