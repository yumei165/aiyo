from pandas import DataFrame, Series
import pandas as pd

#1, Data Structure

#Series: 1D array-like object, can be used as array in numpy, and as dict
obj2 = Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
obj.values #array([4,7,-5,3])
obj.index  #array(['d','b','a','c']), can be altered by assignment
obj[['c', 'a', 'd']] # Series with subset index
'b' in obj  #True
sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
obj3 = Series(sdata)  #obj3 will be in sorted order of sdata keys
states = ['California', 'Ohio', 'Oregon', 'Texas']
obj3 = Series(sdata,index = states)

In [25]: obj3
Out[25]:
California NaN
Ohio 35000
Oregon 16000
Texas 71000

pd.isnull(obj3)  #T, F,F,F
obj3.notnull()

  #critical feature: automatically aligns differently indexed data in arithmetic operation
obj3 + obj4  #will do plus for common indices
obj4.index.name = 'state'  #can assign names to object,index

#DataFrame:the data is stored as one or more two-dimensional blocks
  #create dataframe
data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
  'year': [2000, 2001, 2002, 2001, 2002],
  'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
frame = DataFrame(data)  #5 rows, 3 columns
DataFrame(data, columns=['year', 'state', 'pop'])  #change the order of columns
  #nonpresent columns will have NaN values
frame2 = DataFrame(data, columns=['year', 'state', 'pop', 'debt'], index=['one', 'two', 'three', 'four', 'five']) 
frame2[['state','year']]  frame2.year   #column retrival, get view of data, use Series.copy() to get a copy
frame2.ix[[0,1]]  #get first and second row
  #modify frame values
val = Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])
frame2['debt'] = val
frame2['eastern'] = frame2.state == 'Ohio'
del frame2['eastern']  #delete one column
  #another source: nested dict
pop = {'Nevada': {2001: 2.4, 2002: 2.9},'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}
frame3 = DataFrame(pop)  #in sorted order of key of inner dict
DataFrame(pop, index=[2001, 2002, 2003])  #will match given index from pop
frame3.index.name = 'year'; frame3.columns.name = 'state'; frame3.values; frame3.index(immutable)



