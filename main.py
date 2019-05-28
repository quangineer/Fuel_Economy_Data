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

df_08.drop(['Stnd', 'Underhood ID', 'FE Calc Appr', 'Unadj Cmb MPG'], axis=1, inplace=True)
df_18.drop(['Stnd', 'Underhood ID', 'Stnd Description', 'Comb CO2'], axis=1, inplace=True)
df_08 = df_08.rename(columns={"Sales Area":"Cert Region"})
df_08.rename(columns=lambda x: x.strip().lower().replace(" ", "_"), inplace=True)
df_18.rename(columns=lambda x: x.strip().lower().replace(" ", "_"), inplace=True)
(df_08.columns == df_18.columns).all() # confirm column labels for 2008 and 2018 datasets are identical
# save new datasets for next section
df_08.to_csv('data_08_v1.csv', index=False)
df_18.to_csv('data_18_v1.csv', index=False)

