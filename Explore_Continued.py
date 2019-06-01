import pandas as pd 

df_08 = pd.read_csv("clean_08.csv")
df_18 = pd.read_csv("clean_18.csv")

# Before the merge, we have to change the name of all columns in df_08 to distinguish from 2018 columns. 
df_08.rename(lambda x: x[:10] + "_2008", axis=1, inplace=True)

# Merge 2 datasets:
df_combined = df_08.merge(df_18, left_on='model_2008', right_on='model', how='inner')

# print (df_08.model_2008.value_counts())
# # print (df_08.query('model_2008=="AUDI A6"')[['model_2008','displ_2008','cyl_2008']])
# print (df_18.query('model=="AUDI A6"')[['model','displ','cyl']])
# print (df_combined.query('model=="AUDI A6"').model)
# print (df_combined.query('model=="AUDI A6"')[['model_2008','displ_2008','cyl_2008','model','displ','cyl']])


# print (df_08.shape[0])
# print (df_18.shape[0])
# print (df_combined.shape[0])

# print (df_combined.model_2008.value_counts())
# Using query to count the frequency of value in a column
a = df_combined.query('model_2008 == "AUDI A6"').count()
print (a)

# After merge, check how many columns in total?
# print (df_combined.columns.nunique()) #26

# Now Question is: For all of the models that were produced in 2008 that are still being produced now, how much has the mpg
# improved and which vehicle improved the most?

# (df_08.model_2008.shape[0] == df_18.model.shape[0])  ## False 987 # 832

# Create a new dataframe, model_mpg, that contain the mean combined mpg values in 2008 and 2018 for each unique model
model_mpg = df_combined.groupby('model').mean()[['cmb_mpg_2008', 'cmb_mpg']]

# Create a new column with the change in mean combine mpg
model_mpg['mpg_change'] = model_mpg['cmb_mpg'] - model_mpg['cmb_mpg_2008']
#  Find the vehicle that improved the most
max_change = model_mpg['mpg_change'].max()
# print (model_mpg[model_mpg['mpg_change'] == max_change])

# we can use idxmax function to find the index of the row containing a column's maximum value
# idx = model_mpg.mpg_change.idxmax()
# model_mpg.loc[idx]