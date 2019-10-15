import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
dir="d:/asic/data/tamog/"
file="comtrade_indicator_2.csv"
df=pd.read_csv(dir+file,encoding="utf-8")

print(df)
global year,val_sum
year=[]
val_sum=[]
x=np.linspace(2015,2018,4)
for i in range(2015,2019):
    par_1=df.loc[(df['Trade Flow']=="Import") & (df['Year']==i) & (df['Trade Value (US$)']>0)]
    sum_val=par_1['Trade Value (US$)'].sum()
    year.append(i)
    val_sum.append(sum_val)
new_data=par_1.loc[:,["Reporter",'Trade Value (US$)','Year']]
#print(new_data["Year"]=="2018")
#grouped=par_1.groupby(["Year"]).groups
grouped=par_1.groupby(["Reporter"])
print(grouped)
print(grouped.get_group("Barbados"))

#for name,group in grouped:
#    print (name)
#    print (group)

data=dict(zip(year,val_sum))
df_1=pd.DataFrame(data,index=[0],columns=year)

df_1["Изменение (%)"]=(df_1.iloc[0,3]-df_1.iloc[0,0])/df_1.iloc[0,0]*100

print(df_1)
#print(df_1.iloc[0,2])

fig, ax=plt.subplots()
ax.bar(x,val_sum)
ax.set_title('Динамика товарооборота')
ax.set_xlabel('Год')
ax.set_ylabel('USD')

#plt.show()

