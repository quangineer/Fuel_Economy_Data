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


# After the step above is executed, we now have two sets of datas namely hb_08 and hb_18.
# We have to crack each 'hybrid' row and split them into two new rows in which one with value
# for the first fuel type (value before the '/'), and one with value for the second fuel type
# (value after the '/').

# Create two copies of the hb_08 dataframe:
df1 = hb_08.copy() # data on first fuel type of each hybrid vehicle
df2 = hb_08.copy() # data on second fuel type of each hybrid vehicle

# Now is the time to use python loop function along with apply and lambda function:
# 1. Create a list of columns whose values need to be split by "/":
split_columns = ['fuel', 'air_pollution_score', 'city_mpg', 'hwy_mpg', 'cmb_mpg', 'greenhouse_gas_score']

# 2. apply split function to each column of each dataframe copy:
for c in split_columns:
    df1[c] = df1[c].apply(lambda x: x.split("/")[0])
    df2[c] = df2[c].apply(lambda x: x.split("/")[1])


# Now after successfully spliting and making 2 dataframes, we combine it together to make new_rows:
new_rows = df1.append(df2)

# now we can ignore the original hybrid rows where 2 values are sticked together:
df_08.drop(hb_08.index, inplace=True)

# add in our newly separated rows:
df_08 = df_08.append(new_rows, ignore_index=True)

###### WE are HALF WAY THRU the process of split old and add new rows.
###### Still have one more dataframe of df_18 to repeat this process.

dataframe1 = hb_18.copy()
dataframe2 = hb_18.copy()
List_of_Split_Columns = ['fuel', 'city_mpg', 'hwy_mpg', 'cmb_mpg'] # make a list of columns needed to be fixed
for c in List_of_Split_Columns:
    dataframe1[c]=dataframe1[c].apply(lambda x: x.split("/")[0]) # get the first #
    dataframe2[c]=dataframe2[c].apply(lambda x: x.split("/")[1]) # get the second #
new_rows_for_df_18 = dataframe1.append(dataframe2) # combine two new datasets into one
df_18.drop(hb_18.index, inplace=True) # throw away the old datasets in which values are associated into one cell
df_18.append(new_rows_for_df_18, ignore_index=True) # append the new dataset to big dataframe


(df_18[df_18['fuel'].str.contains('/')])  # Recheck df18 to make sure everything is crystal clear as wished
(df_08[df_08['fuel'].str.contains('/')])  # Recheck df08 to make sure everything is crystal clear as wished
df_08.shape
df_18.shape

