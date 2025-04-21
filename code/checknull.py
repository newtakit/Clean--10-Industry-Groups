import pandas as pd 

df = pd .read_csv(r'C:/Users/newta/OneDrive/Desktop/new-git-test/Clean--10-Industry-Groups/data10/fac-10scurve.csv')

  # แสดงจำนวนค่า NaN ในแต่ละคอลัมน์
#print(df.isnull().sum())

#ลบโรงานที่ไม่มีชื่อออก
df = df.dropna(subset=['ชื่อโรงงาน'])
print(df.isnull().sum())