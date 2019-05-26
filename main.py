import pandas as pd

df_08 = pd.read_csv ('all_alpha_08.csv')
df_18 = pd.read_csv ('all_alpha_18.csv')

#2008
#df_08.info()
#sum(df_08.duplicated())
#df_08.isnull().sum()
#df_08.Fuel.unique()
#2018
#df_18.info()
#df_18.duplicated().sum()
#df_18.isnull().sum()
#df_18["Fuel"].unique()