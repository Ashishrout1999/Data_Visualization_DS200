# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 20:57:33 2022

@author: ashro
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Sub_Division_IMD_2017.csv')

unique_divisions = np.unique(df['SUBDIVISION'])

selected_subdivisions = ['Kerala', 'Orissa', 'Punjab', 'Tamil Nadu', 'Vidarbha',
                         'Gujarat Region']

df_years = df[df['YEAR'].isin(list(range(2001, 2011)))]
df_years = df_years[df_years['SUBDIVISION'].isin(selected_subdivisions)].reset_index(drop = True)


# ------------------- Scatter Plot ---------------------- #
df_scatter = df_years[df_years['SUBDIVISION'].isin(['Tamil Nadu'])]
df_scatter['monsoon_fall'] = df_scatter['JUN'] + df_scatter['JUL'] + df_scatter['AUG'] + df_scatter['SEP']
df_scatter['reverse_monsoon'] = df_scatter['OCT'] + df_scatter['NOV']

plt.figure(figsize = (8, 5))
plt.scatter(df_scatter['monsoon_fall'], df_scatter['reverse_monsoon'], c = 'red')
plt.grid()
plt.xlabel('Rainfall due to monsoon (mm)')
plt.ylabel('Rainfall due to reverse monsoon (mm)')
plt.title('Rainfall due to monsoon and reverse monsoon in Tamilnadu (2001 - 2010)')
plt.show()


# ------------------- Box Plot --------------------------- #
plt.figure()
sns.boxplot(x = 'SUBDIVISION', y = 'ANNUAL', data = df_years, saturation = 1)
plt.xticks(rotation = -15)
plt.xlabel('Region')
plt.ylabel('Annual Rainfall over 2001-2010 (mm)')
plt.title('Annual Rainfall Over Selected Regions (2001 - 2010)')
plt.grid()
plt.show()

# ----------------- Bar Plot ----------------------------- #
df_bar = df_years[df_years['SUBDIVISION'].isin(['Orissa'])]
plt.bar(x = df_bar['YEAR'], height = df_bar['ANNUAL'], color = 'blue')
plt.xlabel('Year')
plt.ylabel('Annual Rainfall (mm)')
plt.title('Annual Rainfall in Odisha (2001 - 2010)')
plt.xticks(np.arange(2001, 2011))
plt.show()
