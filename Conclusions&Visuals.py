import pandas as pd 
import matplotlib as plt
from matplotlib import pyplot
df_08 = pd.read_csv("clean_08.csv")
df_18 = pd.read_csv("clean_18.csv")

# Are more unique models using alternative sources of fuel? By how much ?
df_08_fuels_counts = df_08.fuel.value_counts()
df_18_fuels_counts = df_18.fuel.value_counts()
df_08_unique_models_alternative_fuel = df_08.query('fuel in ["CNG", "ethanol"]').model.nunique()
df_18_unique_models_alternative_fuel = df_18.query('fuel in ["Electricity", "Ethanol"]').model.nunique()

# plt.pyplot.bar(["2008", "2018"], [df_08_unique_models_alternative_fuel, df_18_unique_models_alternative_fuel]
# plt.pyplot.title("Number of unique models using alternative fuels")
# plt.pyplot.xlabel("Year")
# plt.pyplot.ylabel("Number of unique models")
# plt.pyplot.show()
# df_08_unique_models_alternative_fuel.plot.bar(x="year", y='number')
# plt.pyplot.show()

combine1 = pd.DataFrame({'year':['2008', '2018'], 'number':[df_08_unique_models_alternative_fuel, df_18_unique_models_alternative_fuel]})
ax = combine1.plot.bar(x='year', y='number', rot=0)
plt.pyplot.title('Number of models use alternative fuels in 2008 & 2018')
plt.pyplot.show()