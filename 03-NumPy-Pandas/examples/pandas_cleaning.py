import pandas as pd
df=pd.DataFrame({'name':['Asha','Ravi','Mina','Mina'],'age':[21,None,24,24]})
df=df.drop_duplicates().copy(); df['age']=df['age'].fillna(df['age'].median()); print(df)
