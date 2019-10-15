import pandas as pd
import matplotlib.pyplot as plt
#задаем сколько строк и колонок выводится в пандасе
pd.options.display.max_rows = 1000
pd.options.display.max_columns = 1000
#директория
dir="E:/YandexDisk/ASIC/DATA/TAMOG/PARSING/"
#файл исходник
file_in="moscow_reg_gtd_result_group_2.csv"
#итоговый файл
file_out="moscow_reg_gtd_result_group.csv"
df=pd.read_csv(dir+file_in,encoding="cp1251")
print(df.columns)
df["Компаний"]=df["Компаний"].astype(str).str[:-2].astype(int) # компаний по каждому тн вэд
filtr_1=df["Компаний"] >= df["Компаний"].mean()
filtr_2=df['Объем экспорта в USD']>= df['Объем экспорта в USD'].mean()
x=df["Компаний"].loc[filtr_1 & filtr_2]
#print(x)
df['Код ВЭД']=df['Код ВЭД'].astype(str) #тн вэды
y=df['Код ВЭД'].loc[filtr_1 & filtr_2]
print(len(x))

x=x.sort_values()
print(x)

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = y
sizes = x
explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes,  labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()
