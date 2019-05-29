import pandas as pd 
import matplotlib as plt
from matplotlib import pyplot
df_08 = pd.read_csv("clean_08.csv")
df_18 = pd.read_csv("clean_18.csv")

# print(df_08.greenhouse_gas_score.head())
# print (df_08.hist(column='greenhouse_gas_score'))
# print (df_08.head(10))

df_08.greenhouse_gas_score.hist(color='k', label='greenhouse gas score 2008')
df_18.greenhouse_gas_score.hist(color='b', label='greenhouse gas score 2018')
plt.pyplot.legend(loc='upper right')
plt.pyplot.title('Greenhouse Gas Score')
plt.pyplot.xlabel('Score')
plt.pyplot.ylabel('Count')
plt.pyplot.show()

plt.pyplot.hist(df_08.greenhouse_gas_score, alpha=0.5, label='greenhouse gas score 2008')
plt.pyplot.hist(df_18.greenhouse_gas_score, alpha=0.5, label='greenhouse gas score 2018')
plt.pyplot.legend(loc='upper right')
plt.pyplot.show()