import pandas as pd 
import matplotlib as plt
from matplotlib import pyplot
df_08 = pd.read_csv("clean_08.csv")
df_18 = pd.read_csv("clean_18.csv")

# print(df_08.greenhouse_gas_score.head())
# (df_08.hist(column='greenhouse_gas_score'))
# plt.pyplot.show()
# print (df_08.head(10))

# OPTION 1 (NOT RECOMMENDED) Visual for Greenhouse gas score:
# df_08.greenhouse_gas_score.hist(color='k', label='greenhouse gas score 2008')
# df_18.greenhouse_gas_score.hist(color='b', label='greenhouse gas score 2018')
# plt.pyplot.legend(loc='upper right')
# plt.pyplot.title('Greenhouse Gas Score')
# plt.pyplot.xlabel('Score')
# plt.pyplot.ylabel('Count')
# plt.pyplot.show()

# # OPTION 2 (RECOMMENDED) Visual for Greenhouse gas score: it is easy to compare
# plt.pyplot.hist(df_08.greenhouse_gas_score, alpha=0.5, label='greenhouse gas score 2008')
# plt.pyplot.hist(df_18.greenhouse_gas_score, alpha=0.5, label='greenhouse gas score 2018')
# plt.pyplot.legend(loc='upper right')
# plt.pyplot.xlabel('Score')
# plt.pyplot.ylabel('Count')
# plt.pyplot.show()

# OPTION 1 (NOT RECOMMENDED) Visual for combined mpg changed from 2008 to 2018: it will plot 2 separate graphs leading to incomparable situation:
# df_08.hist(column='cmb_mpg', color='b', label='combined mpg 2008')
# df_18.hist(column='cmb_mpg', color='y', label='combined mpg 2018')
# plt.pyplot.legend(loc='upper right')
# plt.pyplot.title('Combined miles per gallon cmb_mpg')
# plt.pyplot.xlabel('Combined miles per gallon')
# plt.pyplot.ylabel('Count')
# plt.pyplot.show()

# OPTION 2 (NOT RECOMMENDED) Visual for combined mpg changed from 2008 to 2018: 
# df_08.cmb_mpg.hist(color='b', label='combined mpg 2008')
# df_18.cmb_mpg.hist(color='y', label='combined mpg 2018')
# plt.pyplot.legend(loc='upper right')
# plt.pyplot.title('Combined miles per gallon cmb_mpg')
# plt.pyplot.xlabel('Combined miles per gallon')
# plt.pyplot.ylabel('Count')
# plt.pyplot.show()

# # OPTION 3 (RECOMMENDED) Visual for combined mpg changed from 2008 to 2018: it is easy to compare
# plt.pyplot.hist(df_08.cmb_mpg, alpha=0.5, label='combined mpg 2008')
# plt.pyplot.hist(df_18.cmb_mpg, alpha=0.5, label='combined mpg 2018')
# plt.pyplot.legend(loc='upper right')
# plt.pyplot.xlabel('Combined miles per gallon')
# plt.pyplot.ylabel('Count')
# plt.pyplot.show()

###### Scatterplot ######
# Option 1 (not recommended) because it will create two separate scatter plots which is incomparable:
# df_08.plot.scatter(x='displ', y='cmb_mpg')
# df_18.plot.scatter(x='displ', y='cmb_mpg')
# plt.pyplot.show()

# Option 2(RECOMMENDED) correlation between displacement and combined mpg
# plt.pyplot.scatter(x=df_08.displ, y=df_08.cmb_mpg, alpha=0.5, label='correlation between displacement and combined mpg in 2008')
# plt.pyplot.scatter(x=df_18.displ, y=df_18.cmb_mpg, alpha=0.5, label='correlation between displacement and combined mpg in 2018')
# plt.pyplot.legend(loc='upper right')
# plt.pyplot.xlabel('displacement')
# plt.pyplot.ylabel('Combined miles per gallon')
# plt.pyplot.show()

# Option 1(RECOMMENDED) correlation between greenhouse gas score and combined mpg
plt.pyplot.scatter(x=df_08.greenhouse_gas_score, y=df_08.cmb_mpg, alpha=0.5, label='correlation between greenhouse gas score and combined mpg in 2008')
plt.pyplot.scatter(x=df_18.greenhouse_gas_score, y=df_18.cmb_mpg, alpha=0.5, label='correlation between greenhouse gas score and combined mpg in 2018')
plt.pyplot.legend(loc='upper left')
plt.pyplot.xlabel('Greenhouse Gas Score')
plt.pyplot.ylabel('Combined miles per gallon')
plt.pyplot.show()