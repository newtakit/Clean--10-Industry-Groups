import pandas as pd 

df = pd .read_csv(r'C:/Users/newta/OneDrive/Desktop/new-git-test/Clean--10-Industry-Groups/data10/fac-10scurve.csv')

print(df.dtypes)
df[' คนงานรวม '] = pd.to_numeric(df[' คนงานรวม '], errors='coerce').fillna(0).astype(int)
df[' แรงม้า '] = pd.to_numeric(df[' แรงม้า '], errors='coerce').fillna(0).astype(float)
print(df.dtypes)