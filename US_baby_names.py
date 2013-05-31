#data source: http://www.ssa.gov/oact/babynames/limits.html, txt files

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#load data
names1880 = pd.read_csv('names/yob1880.txt', names=['name', 'sex', 'births'])

#get births by sex
birth_sum = names1880.groupby('sex').births.sum()

#make a list of frames
years = range(1880,2011)
pieces = []
columns = ['name', 'sex', 'births']
for year in years:
   path = 'names/yob%d.txt' % year
   frame = pd.read_csv(path, names=columns)
   frame['year'] = year
   pieces.append(frame)
# Concatenate the list into a single DataFrame
names = pd.concat(pieces, ignore_index=True)

#get total births by year/sex
total_births = names.pivot_table('births', rows='year', cols='sex', aggfunc=sum)
total_births.tail()
total_births.plot(title='Total births by sex and year')

#calculate proportion to total births per sex/year
def add_prop(group):
    #Integer division floors, can skip it with python 3+
    births = group.births.astype(float)
    group['prop'] = births / births.sum()
    return group
names = names.groupby(['year', 'sex']).apply(add_prop)

#boolean to check if prop adds to 1(nice to have)
np.allclose(names.groupby(['year', 'sex']).prop.sum(), 1)

#get top 1000 names by sex/year
def get_top1000(group):
    return group.sort_index(by='births', ascending=False)[:1000]
top1000 = names.groupby(['year', 'sex']).apply(get_top1000)

  #a more intuitive way
pieces = []
for year, group in names.groupby(['year', 'sex']):
    pieces.append(group.sort_index(by='births', ascending=False)[:1000])
    top1000 = pd.concat(pieces, ignore_index=True)
   
#analyze name trend
boys = top1000[top1000.sex == 'M']
girls = top1000[top1000.sex == 'F']
total_births = top1000.pivot_table('births', rows='year', cols='name', aggfunc=sum)
subset = total_births[['John', 'Harry', 'Mary', 'Marilyn']]
subset.plot(subplots=True, figsize=(12, 10), grid=False, title="Number of births per year")
table = top1000.pivot_table('prop', rows='year', cols='sex', aggfunc=sum)
table.plot(title='Sum of table1000.prop by year and sex', yticks=np.linspace(0, 1.2, 13), xticks=range(1880, 2020, 10))
df = boys[boys.year == 2010]
  #how many of the most popularnames it takes to reach 50%
prop_cumsum = df.sort_index(by='prop', ascending=False).prop.cumsum()
prop_cumsum.searchsorted(0.5)
  #apply to all data
def get_quantile_count(group, q=0.5):
    group = group.sort_index(by='prop', ascending=False)
    return group.prop.cumsum().searchsorted(q) + 1
diversity = top1000.groupby(['year', 'sex']).apply(get_quantile_count)
diversity = diversity.unstack('sex')

# extract last letter from name column
get_last_letter = lambda x: x[-1]
last_letters = names.name.map(get_last_letter)
last_letters.name = 'last_letter'
table = names.pivot_table('births', rows=last_letters, cols=['sex', 'year'], aggfunc=sum)
 #select 3 representative years
subtable = table.reindex(columns=[1910, 1960, 2010], level='year')
subtable.head()
subtable.sum()
letter_prop = subtable / subtable.sum().astype(float)
fig, axes = plt.subplots(2, 1, figsize=(10, 8))
letter_prop['M'].plot(kind='bar', rot=0, ax=axes[0], title='Male')
letter_prop['F'].plot(kind='bar', rot=0, ax=axes[1], title='Female', legend=False)
  #all years with last letter 'd'/'n'/'y'
letter_prop = table / table.sum().astype(float)
dny_ts = letter_prop.ix[['d', 'n', 'y'], 'M'].T
dny_ts.plot()

#boy names that become girl names(and vice versa)
all_names = top1000.name.unique()
mask = np.array(['lesl' in x.lower() for x in all_names])
lesley_like = all_names[mask]
 #analyze the name 'lesley'-like
filtered = top1000[top1000.name.isin(lesley_like)]
filtered.groupby('name').births.sum()
table = filtered.pivot_table('births', rows='year', cols='sex', aggfunc='sum')
table = table.div(table.sum(1), axis=0)
table.plot(style={'M': 'k-', 'F': 'k--'})





