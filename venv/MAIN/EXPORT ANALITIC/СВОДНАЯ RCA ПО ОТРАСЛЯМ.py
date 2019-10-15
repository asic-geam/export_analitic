import pandas as pd
import os
#задача получить датасет с самыми перспективынми рынками по всем отраслям исходя из фильтрации по индексу балласа
# 1. собрать индекс балласа колонка страна и колонки RCA
# 2. отфильтровать все страны по RCA и сгруппировть их
# 3. передать группы в датасет с результрующей выборкой (самые перспектиивные страны по отраслям для экспорта)
#функция сбора данных в единуб таблицу по всем отраслям
path="d:/asic/data/tamog/parsing/"
#создаем структуру таблицы с колонками страны
file_0="itc_indust_00.csv"
data=pd.read_csv(path+file_0,encoding="utf-8")
country={"Country":data["Country"],"00":data['Specialisation (Balassa Index / RCA Index )']}
df=pd.DataFrame(country,columns=["Country","00"])
#список с кодами отраслей, всего 99 секторов, 00 - это все индустрии
key_ind=list(range(1,100))
for i in range(9):
    key_ind[i]="0"+str(key_ind[i])
for i in range(9,99):
    key_ind[i]=(str(key_ind[i]))
#пишем цикл прохода по всем таблицам
for i in range(len(key_ind)):
    file="itc_indust_"+str(key_ind[i])+".csv"
    data1=pd.read_csv(path+file,encoding="utf-8")
    data1=data1[["Country",'Specialisation (Balassa Index / RCA Index )']]
    #оздаем датафрейм с новой структурой, где будет колонка (номер индустрии)
    country1={"Country":data1["Country"],str(key_ind[i]):data1['Specialisation (Balassa Index / RCA Index )']}
    df2=pd.DataFrame(country1,columns=["Country",str(key_ind[i])])
    #склеиваем два датасета с наложением по ключам и колонке страна
    df=pd.merge(df, df2, how='outer',on='Country')
#передаем в сводный файл
file_result="result_rca.csv"
path_res="d:/asic/data/tamog/temp/"
df.to_csv(path_res+file_result,encoding="utf-8")

