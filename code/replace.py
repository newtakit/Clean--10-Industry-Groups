import pandas as pd 

df = pd .read_csv(r'C:/Users/newta/OneDrive/Desktop/new-git-test/Clean--10-Industry-Groups/data10/fac-10scurve.csv')

#ลบช่องว่างในชื่อคอลัมน์
df.columns = df.columns.str.replace(' ', '')
