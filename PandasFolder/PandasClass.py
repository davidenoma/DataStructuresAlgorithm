#Tutorials from Python Data Science Handbook.
from timeit import timeit

import pandas as pd
import numpy as np

data = pd.Series([0.25,0.5,0.75,1.0],index=['a','b','c','d'])
population_dict = {'California':1234,'Texas':93093,
                    'New York':10334,
                   'Florida':493838,
                   'Illinois':29393}
population = pd.Series(population_dict)
print(population)
print(population['New York':'Florida'])

area_dict = {'California':423967,'Texas':93344,'New York':39384,
'Illinois':9283983}
area = pd.Series(area_dict)
print(area)
#creating a new data frame
states = pd.DataFrame({'population':population,'area':area})
print(states,"\n", states.index,"\n",states.columns)

#Consructing DataFrame objects
print(pd.DataFrame(population,columns=['population']))
data = [{'a':i,'b':2*i} for i in range(3)]
print(data)
pd.DataFrame(data)
foo = pd.DataFrame([{'a': 1, 'b': 2}, {'b': 3, 'c': 4}])
print(foo)
#from 2 dimensional numpy array
foo2 = pd.DataFrame(np.random.rand(3,2),
             columns=['foo','bar'],
             index=['a','b','c'])
print(foo2)
#Pandas Indexes
ind = pd.Index([2,3,5,7,9,11])
ind
print(ind[::2],"\n next", ind.size,ind.shape,ind.ndim,ind.dtype)
indA = pd.Index([1,3,5,7,9])
indB = pd.Index([2,3,5,7,11])

print(indA.intersection(indB))
print(indA.union(indB))


##DATA INDEXING AND SELECTION
data = pd.Series([0.25,0.5,0.75,1.0],index=['a','b','c','d'])
print(data)
print(data.keys(),list(data.items()))
print(data[0:2],data[(data>0.3) & (data < 0.8)])

#indexers loc, iloc and ix
data = pd.Series(['a','b','c'],index=[1,3,5])
print(data)
data[1]
data[1:3]
#loc references the explicily stated index
print(data.loc[1])
data.loc[1:3]
#iloc references the implicit python stylle index
print(data.iloc[1])
data.iloc[1:4]
data = pd.DataFrame({'area':area,'pop':population})
print(data['area'][1])
#data['area'][1] = 4342422
data['density'] = data['pop'] / data ['area']
print(data.values)
print(data.values[0])
print(data.T)

#using the iloc for indexing pandas aray
print(data.iloc[:3,:2])
#using the explicit indexes
print(data.loc[:'Illinois',:'pop'])
#ix is a hybrid of these approaches
#not sure if present in 3.9
#print(data.ix[:3,:'pop'])
#masking can be combined with loc indexing
print(data)
print(data.loc[data.density > 0.002 , ['pop','density']])

#assigning values
data.iloc[1,0] = 4859382
print(data)
#additional indexing conventions
print(data['Florida':'Illinois'])

print(data[1:3])
print(data[data.density > 0.002])

#Ufuncs
rng = np.random.RandomState(42)
ser = pd.Series(rng.randint(0,10,4))
print(ser)
df = pd.DataFrame(rng.randint(0,10,(3,4)),
                  columns=['A','B','C','D'])
print(df)
print(np.exp(ser))

print(np.sin(df * np.pi / 4))

area = pd.Series({'Alaska': 1723337, 'Texas': 695662,
'California': 423967}, name='area')
population = pd.Series({'California': 38332521, 'Texas': 26448193,
'New York': 19651127}, name='population')
print(population/area)
print(area.index | population.index)

A = pd.Series([2, 4, 6], index=[0, 1, 2])
B = pd.Series([1, 3, 5], index=[1, 2, 3])
print(A.__add__(B))
print(A.__add__(B))

#Index alignmen in DataFrame
A = pd.DataFrame(rng.randint(0, 20, (2, 2)),
columns=list('AB'))
print(A)
B = pd.DataFrame(rng.randint(0, 10, (3, 3)),
columns=list('BAC'))
print(A+B)
#there are other pandas methods such as sub() and mul()

#HANDLING MISSING DATA
vals1 = np.array([1,None,3,4])
print(vals1)

for dtype in ['object','int']:
    print("dtype = ",dtype)
   # %timeit np.arange(1E6,dtype=dtype).sum()
    print()
data = pd.Series([1,np.nan,2,None])

#operation on null values.

print(data.isnull())
print(data[data.notnull()])
print(data.dropna())

df = pd.DataFrame([[1, np.nan, 2],
[2, 3, 5],
[np.nan, 4, 6]])
print(df.dropna())
print(df.dropna(axis='columns'))
df.dropna(axis='columns', how='all')
df.dropna(axis='rows', thresh=3)

#Fill NA values
data = pd.Series([1, np.nan, 2, None, 3], index=list('abcde'))
print(data)
data.fillna(0)
data.fillna(method='ffill')
data.fillna(method='bfill')

#Hierarchical indexing
index = [('California', 2000), ('California', 2010),
('New York', 2000), ('New York', 2010),
('Texas', 2000), ('Texas', 2010)]
populations = [33871648, 37253956,
18976457, 19378102,
20851820, 25145561]
pop = pd.Series(populations, index=index)
print(pop)

#Pandas multi-index
#pandas multi=index type
index = pd.MultiIndex.from_tuples(index)
print(index)
pop = pop.reindex(index)
print(pop)

print(pop[:,2010])
pop_df = pop.unstack()
print(pop_df)
pop_df = pd.DataFrame({'total': pop,
'under18': [9267089, 9284094,
4687374, 4318033,
5906301, 6879014]})
print(pop_df)
f_u18 = pop_df['under18']/pop_df['total']
print(f_u18)
print(f_u18.unstack())
#multiindex creation
df = pd.DataFrame(np.random.rand(4, 2),
index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
columns=['data1', 'data2'])
print(df)
#Explicit muliindex constructors
pd.MultiIndex.from_arrays([['a', 'a', 'b', 'b'], [1, 2, 1, 2]])
pd.MultiIndex.from_tuples([('a', 1), ('a', 2), ('b', 1), ('b', 2)])
pd.MultiIndex.from_product([['a', 'b'], [1, 2]])

pop.index.names = ['state','year']
print(pop)
#Multi-index for columns
index = pd.MultiIndex.from_product([[2013, 2014], [1, 2]],
names=['year', 'visit'])
columns = pd.MultiIndex.from_product([['Bob', 'Guido', 'Sue'], ['HR', 'Temp']],
names=['subject', 'type'])
# mock some data
data = np.round(np.random.randn(4, 6), 1)
data[:, ::2] *= 10
data += 37
# create the DataFrame
health_data = pd.DataFrame(data, index=index, columns=columns)
#indexing and slicing a multi-index
print(pop['California',2010])
print(pop['California'])
print(pop.unstack())
pop.loc['California':'New York']
pop[:, 2000]
print(pop[pop > 2200000])

#Multiply indexed DataFrames
print(index,columns,"\n",health_data,'\n',health_data.unstack())
print(health_data['Guido','HR'])
print(health_data.iloc[:2, :2])
print(health_data.loc[:,('Bob','HR')])
#Rearranging Multi-Indices
