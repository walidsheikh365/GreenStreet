# Author: GreenStreetT
# Date 10/11/2021
# Data exploration file for Coursework 1

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the two prepared data files
df1 = pd.read_csv('Prepared_Data1.csv')
df2 = pd.read_csv('Prepared_Data2.csv')

# Calculate open space area in a borough as a percentage of total borough area
df1['OpenSpaceArea_%'] = 100 * (df1['OpenSpaceArea_m2'] / df1['TotalArea_m2'])

# Calculate canopy cover area in a borough as a percentage of total borough area
df1['CanopyCover_%'] = 100 * (df1['Canopy_m2'] / df1['TotalArea_m2'])

# Calculate total area in Greater London and round it to 2 decimal places
LondonArea_m2 = round(df1['TotalArea_m2'].sum(), 2)

# Calculate total open space area in Greater London and its percentage of total area, rounded to 2 decimals
LondonOpenSpace_m2 = round(df1['OpenSpaceArea_m2'].sum(), 2)
LondonOpenSpace_per = 100 * (LondonOpenSpace_m2 / LondonArea_m2)

# Calculate total canopy cover in Greater London and its percentage of open space area, rounded to 2 decimals
LondonCanopy_m2 = round(df1['Canopy_m2'].sum(), 2)
LondonCanopy_per = 100 * (LondonCanopy_m2 / LondonArea_m2)

# Calculate the total area for each open space area primary use type and its percentage of total open space area
PrimaryUseTotal_m2 = df2.groupby(['PrimaryUse']).sum()['OpenSpaceArea_m2']
PrimaryUseTotal_per = 100 * (PrimaryUseTotal_m2 / LondonOpenSpace_m2)

# Calculate correlation between canopy cover and open space area percentages (Pearson's R method)
CanopyOpenSpace_Corr = round(df1['CanopyCover_%'].corr(df1['OpenSpaceArea_%']), 2)
print("The Pearson's R value for correlation between canopy cover and open space is", CanopyOpenSpace_Corr)

# Plot the correlation between canopy cover and open space area percentages with green circle markers
plt.figure(1)
plt.plot(df1['CanopyCover_%'], df1['OpenSpaceArea_%'], 'go')
plt.xlabel('Borough Canopy Cover %')
plt.ylabel('Borough Open Space Area %')
plt.title('Canopy Cover and Open Space Area Relationship in London Boroughs')
plt.savefig('Open Space and Canopy Correlation.png')
plt.show()

# Plot a bar chart showing percentages of primary use open space types for London
plt.figure(2).set_size_inches(18, 10)
labels = df2['PrimaryUse'].sort_values().unique()
plt.barh(labels, PrimaryUseTotal_per, height=0.5, color='green')
plt.xlabel('London Open Space Area %')
plt.title('Open Space Primary Use Percentages for London Open Spaces')
plt.savefig('Open Space Primary Use Percentages.png')
plt.show()

# Plot a grouped bar chart showing percentages of open space area and canopy cover for each borough
plt.figure(3)
labels = df1['Borough']

# label locations and bar widths
x = np.arange(len(labels))
width = 0.35

fig, ax = plt.subplots()
bars_OpenSpace = ax.bar(x - width/2, df1['OpenSpaceArea_%'], width, label='Open Space Area %', color='red')
bars_Canopy = ax.bar(x + width/2, df1['CanopyCover_%'], width, label='Canopy Cover %', color='green')

# labels for axes, title and legend
ax.set_ylabel('Percentage of Total Borough Area (%)')
ax.set_title('Percentage of Open Space Area and Canopy Cover for Boroughs')
ax.set_xticks(x)
plt.xticks(rotation=90)
ax.set_xticklabels(labels)
ax.legend()

fig.tight_layout()
fig.savefig('Open Space and Canopy Boroughs.png')
plt.show()

# Plot a bar chart showing percentages of primary use open space types for London
# Westminster as an example, can be later made into a user input
borough = 'Westminster'
plt.figure(4)
df_borough = df2.loc[df2['Borough'] == borough]

# Calculate total open space area in the selected borough
borough_OpenSpace_m2 = df_borough['OpenSpaceArea_m2'].sum()

# Calculate open space area primary use percentages for the borough
borough_OpenSpace_per = 100 * (df_borough['OpenSpaceArea_m2'] / borough_OpenSpace_m2)
labels = df_borough['PrimaryUse']

plt.bar(labels, borough_OpenSpace_per, color='green')
plt.xticks(rotation=90)
plt.ylabel('Borough Open Space Area %')
plt.title('Primary Use Percentages for ' + borough)
plt.tight_layout()
plt.savefig(borough + ' Open Spaces.png')
plt.show()


