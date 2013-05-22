#data source: http://www.ssa.gov/oact/babynames/limits.html, txt files

import pandas as pd
import numpy as np

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
    






