import pandas as pd
import numpy as np
pd.set_option('display.max_rows',15)
amazon = pd.read_csv('C:/Users/HP/OneDrive/Desktop/AMZN.csv',index_col=0)
#print(amazon.head(10))
#Indexing and writing to file
amazon_subset = amazon.iloc[:,0:3]
#amazon_subset.write_csv('test_sub')
amazon_subset = pd.DataFrame(amazon_subset)
amazon_subset.to_csv('amazon_subset')

print(amazon.columns)
print(amazon_subset.columns)



#creating MISSING VALUES
amazon.iloc[0] = np.nan
print(amazon.head(10))
amazon.iloc[1,3] = np.nan
print(amazon.head(10))
print(amazon.isnull())
#Handling missing values
amazon = amazon.dropna(how= 'all')
print(amazon.head(5))
amazon.iloc[0] = np.nan
print(amazon.fillna(method="ffill"))

df = pd.DataFrame({'x':[0,2,5,57,8],'Y':[5,6,8,9,10]})
print(df)
df = df.apply(lambda v: v+10)
print(df)