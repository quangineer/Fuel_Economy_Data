import pandas as pd 

df_08 = pd.read_csv("data_08_v4.csv")
df_18 = pd.read_csv("data_18_v4.csv")

# make a list of column labels with "mpg":
mpg_columns = ["city_mpg", "hwy_mpg", "cmb_mpg"]
for c in mpg_columns:
    df_08[c] = df_08[c].astype(float)  # convert to float
    df_18[c] = df_18[c].astype(float)  # convert to float

# convert greenhouse_gas_score from float to int in 2008 dataframe
df_08["greenhouse_gas_score"] = df_08["greenhouse_gas_score"].astype(int)

# Check everything:
# print (df_08.shape)
# print (df_18.shape)
# print (df_08.dtypes == df_18.dtypes)

df_08.to_csv("clean_08.csv", index=False)
df_18.to_csv("clean_18.csv", index=False)