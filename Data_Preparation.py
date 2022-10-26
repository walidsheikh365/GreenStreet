# Author: GreenStreet
# Date 10/11/2021
# Data preparation file for Coursework 1

import pandas as pd

# Read the two datasets, open spaces and canopy cover respectively
df1 = pd.read_csv('OpenSpace.csv')
df2 = pd.read_csv('CanopyCover.csv')

# Retain only the columns that are needed for data exploration
df1 = df1[['Borough', 'PrimaryUse', 'AreaHa']]
df2 = df2[['la_nm', 'lsoa_kmsq', 'canopy_kmsq']]

# Convert hectares to square meters in df1
df1['AreaHa'] = 10000 * df1['AreaHa']

# Rename columns to more suitable names
df1 = df1.rename(columns={'AreaHa': 'OpenSpaceArea_m2'})
df2 = df2.rename(columns={'la_nm': 'Borough', 'lsoa_kmsq': 'SubArea_m2', 'canopy_kmsq': 'Canopy_m2'})

# Sort by borough, alphabetically
df1 = df1.sort_values(['Borough'])
df2 = df2.sort_values(['Borough'])

# Split up shared open spaces between boroughs to each borough equally through a new data frame
# Search for instances of ';' in borough name for each open area
df3 = df1.loc[df1['Borough'].str.contains(';')]

for index, row in df3.iterrows():
    # count the instances of ';' and add one to divide area by
    num_boroughs = row['Borough'].count(';') + 1

    # divide the area to split between the boroughs
    split_area = row['OpenSpaceArea_m2'] / num_boroughs

    # find all indices of ';', and store in an array
    indices = []
    for index2 in range(len(row['Borough'])):
        if row['Borough'][index2] == ';':
            indices.append(index2)

    # use a for-loop to make news rows for the split open space per borough
    for index2 in range(num_boroughs):

        # for the first index, slice the borough name from the beginning to the first ';'
        if index2 == 0:
            borough_name = row['Borough'][:indices[index2]]

        # for the last index, slice the borough name from the last '; ' (including the space) to string end
        elif index2 == (num_boroughs - 1):
            borough_name = row['Borough'][indices[index2 - 1] + 2:]

        # for the borough names between first and last, slice the name between '; ' (including space) and ';'
        else:
            borough_name = row['Borough'][indices[index2 - 1] + 2:indices[index2]]

        # make a new rough for the split area per borough, and append to df1
        new_row = {'Borough': borough_name, 'PrimaryUse': row['PrimaryUse'], 'OpenSpaceArea_m2': split_area}
        df1 = df1.append(new_row, ignore_index=True)

# Remove the redundant, shared open spaces from df1
df1 = df1.loc[~df1['Borough'].str.contains(';')]

# Remove the 'Outside Greater London' Category from df1
df1 = df1.loc[~df1['Borough'].str.contains('Outside')]

# Aggregate Statistics
# Sum up all the open space areas by borough and then primary use in a new data frame
df4 = round(df1.groupby(['Borough', 'PrimaryUse']).sum()['OpenSpaceArea_m2'], 2)

# Sum up total area of open spaces by borough (for later exploration with canopy cover)
df1 = round(df1.groupby(['Borough']).sum()['OpenSpaceArea_m2'], 2)

# Sum up all the sub areas and respective canopy areas by borough
df2 = round(df2.groupby(['Borough']).sum(), 2)

# Rename columns to appropriate names
df2 = df2.rename(columns={'SubArea_m2': 'TotalArea_m2'})

# Concatenate data for total open space area and canopy cover per borough
prep_df1 = pd.concat([df1, df2], axis=1)

# Reassign name as a convention
prep_df2 = df4

# Export as csv files
prep_df1.to_csv('Prepared_Data1.csv')
prep_df2.to_csv('Prepared_Data2.csv')



