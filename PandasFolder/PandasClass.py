#Tutorials from Python Data Science Handbook.
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

#using