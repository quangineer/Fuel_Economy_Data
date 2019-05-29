# dropping rows and columns in pandas dataframe

import pandas as pd

# create a dataframe:
data = {'company_name': ['EA', 'BAPE', 'NUKE', 'CHES', 'TERRA', 'BROOK', 'TOT'], 'population': [1200, 300, 800, 200, 100, 50, 20], 'dob': [1993, 2010, 1990, 1980, 1985, 2019, 2011]}
df = pd.DataFrame(data, index = ['Vancouver', 'Tokyo', 'Newyork', 'Birmingham', 'NovaIsland', 'Cakiloving', 'Sydney'])
# print (df)

# drop row: you have to call the index out loud to drop, default axis = 0
df.drop('Sydney')
# print (df)
#            company_name  population   dob
# Vancouver            EA        1200  1993
# Tokyo              BAPE         300  2010
# Newyork            NUKE         800  1990
# Birmingham         CHES         200  1980
# NovaIsland        TERRA         100  1985
# Cakiloving        BROOK          50  2019
# Sydney              TOT          20  2011

df.drop('Sydney', inplace=True) # df=df.drop('Sydney')
# print (df)
#            company_name  population   dob
# Vancouver            EA        1200  1993
# Tokyo              BAPE         300  2010
# Newyork            NUKE         800  1990
# Birmingham         CHES         200  1980
# NovaIsland        TERRA         100  1985
# Cakiloving        BROOK          50  2019

# drop a column: axis = 1 denotes that we are referring to a column, NOT A ROW:
df.drop('dob', axis=1, inplace=True)
# print (df)

# drop a row by row number:
df.drop(df.index[2], inplace=True)
# OR df.drop('Newyork', inplace=True)
# print (df)

#select ranges like python function:
print (df[:3])

