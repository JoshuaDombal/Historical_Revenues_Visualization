# This file creates a visualization from an excel file of Revenue Data


import matplotlib.pyplot as plt
import pandas as pd
import csv
import seaborn as sns


file = 'Historical_Revenues.xlsx'

xl = pd.ExcelFile(file)

print(xl.sheet_names)


dataframe = xl.parse('Pivot Table Raw Data')
"""
print(dataframe.info())

dataframe.plot(kind='scatter', x=')
plt.show()

"""

# Shows Fiscal Year with highest Revenue
a = sns.barplot(x="Fiscal Year", y="Amount", data=dataframe)
for item in a.get_xticklabels():
    item.set_rotation(80)
plt.show()



################################################################################


#sns.boxplot(x="Fiscal Year", y="Amount", data=dataframe)
#plt.show()


# Shows Sum of Categories
# Helps show which category had the most revenue overall
b = sns.barplot(x="Category", y="Amount", data=dataframe)
plt.show()




#print(data.head())

#colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral', 'red']

#data['Type of Fund'].value_counts().plot(kind='pie', title='TOF', colors=colors)
#plt.show()