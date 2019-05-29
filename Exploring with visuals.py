import pandas as pd 
import matplotlib as plt
df_08 = pd.read_csv("clean_08.csv")
df_18 = pd.read_csv("clean_18.csv")

# print(df_08.greenhouse_gas_score.head())
# print (df_08.hist(column='greenhouse_gas_score'))
# print (df_08.head(10))

df_08.greenhouse_gas_score.hist(color='k')
df_18.greenhouse_gas_score.hist(color='b')
plt.pyplot.title('Greenhouse Gas Score')
plt.pyplot.xlabel('Score')
plt.pyplot.ylabel('Count')
plt.pyplot.show()