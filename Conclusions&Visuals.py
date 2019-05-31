import pandas as pd 
import matplotlib as plt
from matplotlib import pyplot
df_08 = pd.read_csv("clean_08.csv")
df_18 = pd.read_csv("clean_18.csv")

# Are more unique models using alternative sources of fuel? By how much ?
# df_08_fuels_counts = df_08.fuel.value_counts()
# df_18_fuels_counts = df_18.fuel.value_counts()
# df_08_unique_models_alternative_fuel = df_08.query('fuel in ["CNG", "ethanol"]').model.nunique()
# df_18_unique_models_alternative_fuel = df_18.query('fuel in ["Electricity", "Ethanol"]').model.nunique()
## PLOT: 
# combine1 = pd.DataFrame({'year':['2008', '2018'], 'number':[df_08_unique_models_alternative_fuel, df_18_unique_models_alternative_fuel]})
# ax = combine1.plot.bar(x='year', y='number', rot=0)
# plt.pyplot.title('Number of models use alternative fuels in 2008 & 2018')
# plt.pyplot.show()

# How much have vehilce classes improved in fuel economy?
df_08.veh_class.value_counts()
df_18.veh_class.value_counts()
mean_of_08_VC_cmb_mpg = df_08.groupby('veh_class').cmb_mpg.mean()
mean_of_18_VC_cmb_mpg = df_18.groupby('veh_class').cmb_mpg.mean()
increase = mean_of_18_VC_cmb_mpg - mean_of_08_VC_cmb_mpg
increase.dropna(inplace=True)
## PLOT:
plt.pyplot.subplots(figsize=(8, 5))
plt.pyplot.bar(increase.index, increase)
plt.pyplot.title('Improvements in Fuel Economy from 2008 to 2018 by Vehicle Class')
plt.pyplot.xlabel('Vehicle Class')
plt.pyplot.ylabel('Increase in Average Combined MPG')
plt.pyplot.show()