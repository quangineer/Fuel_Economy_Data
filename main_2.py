import pandas as pd

df_08 = pd.read_csv('data_08_v1.csv')
df_18 = pd.read_csv('data_18_v1.csv')


# Filter by Certification region:
df_08 = df_08.query('cert_region == "CA"')
df_18 = df_18.query('cert_region == "CA"')
df_08['cert_region'].unique()
df_18['cert_region'].unique()
df_08.drop('cert_region', axis =1, inplace=True)
df_18.drop('cert_region', axis =1, inplace=True)


# Drop Rows with Missing Values:
df_08.isnull().sum()
df_18.isnull().sum()
df_08.dropna(inplace=True)
df_18.dropna(inplace=True)
df_08.isnull().sum().any()
df_18.isnull().sum().any()


# Dedupe Data:
df_08.duplicated().sum()
df_18.duplicated().sum()
df_08.drop_duplicates(inplace=True)
df_18.drop_duplicates(inplace=True)
print (df_08.shape)
print (df_18.shape)
df_08.duplicated().sum()
df_18.duplicated().sum()
df_08.to_csv('data_08_v2.csv', index=False)
df_18.to_csv('data_18_v2.csv', index=False)
