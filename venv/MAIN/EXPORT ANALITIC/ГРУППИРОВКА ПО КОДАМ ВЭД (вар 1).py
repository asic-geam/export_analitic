import pandas as pd
#задаем сколько строк и колонок выводится в пандасе
pd.options.display.max_rows = 1000
pd.options.display.max_columns = 1000
#директория
dir="E:/YandexDisk/ASIC/DATA/TAMOG/PARSING/"
#файл исходник
file="moscow_reg_gtd_result.csv"
#итоговый файл
file_res="moscow_reg_gtd_result_group_2.csv"
df=pd.read_csv(dir+file,encoding="cp1251")

#обрезаем до 4ех знаков код вед
df["VED_4"]=df.loc[:,"Код ТН ВЭД"].apply(lambda x: str(x)[0:4])

#переводим все в usd
kurs_usd=65
kurs_eur=72
kurs_gbr=80
for i in range(len(df)):
    if df.loc[i,"Валюта контракта"]=="RUB":
        convert=df.loc[i,"Таможенная стоимость"]/kurs_usd
        df.loc[i,"Тамож.стоим.USD"]=convert
        #print(df.loc[i,["Таможенная стоимость","Тамож.стоим.USD"]])
    elif df.loc[i,"Валюта контракта"]=="EUR":
        convert_2=df.loc[i,"Таможенная стоимость"]/kurs_eur
        df.loc[i,"Тамож.стоим.USD"]=convert_2
        #print(df.loc[i,["Таможенная стоимость","Тамож.стоим.USD"]])
    elif df.loc[i,"Валюта контракта"]=="USD":
        convert_3=df.loc[i,"Таможенная стоимость"]
        df.loc[i,"Тамож.стоим.USD"]=convert_3
    elif df.loc[i,"Валюта контракта"]=="GBP":
        convert_4=df.loc[i,"Таможенная стоимость"]
        df.loc[i,"Тамож.стоим.USD"]=convert_4/kurs_gbr

#print(df.loc[:,["Таможенная стоимость","Тамож.стоим.USD"]])


# пишем счетчик кол-ва всех вед на 4 знака
df_2=df.loc[:,"VED_4"]
ved=list(set(df_2))

#создаем пустой итоговый датасет
data={"Код ВЭД":"NaN","Компаний":"NaN","Объем экспорта в USD":"NaN","Доля в регионе":"NaN"}
df_res=pd.DataFrame(data,index=[0],columns=["Код ВЭД","Компаний","Объем экспорта в USD","Доля в регионе (кол)"])
#заполняем в итерации итоговый датасет
for i in range(len(ved)):
    grouped=df.groupby(["VED_4"])
    res=grouped.get_group(str(ved[i]))
    #!!! написать очистку от повторяющихся компаний по ИНН
    df_res.loc[i,"Код ВЭД"]=ved[i]
    df_res.loc[i,"Компаний"]=len(res)
    df_res.loc[i,"Объем экспорта в USD"]=res["Тамож.стоим.USD"].sum()
    df_res.loc[i,"Доля в регионе (кол)"]=len(res)/len(df_2)
    df_res.loc[i,"Доля в регионе (фин)"]=res["Тамож.стоим.USD"].sum()/df.loc[:,"Тамож.стоим.USD"].sum()
#вывод
#print(df_res)
#сохраняем в файл
df_res.to_csv(dir+file_res,encoding="cp1251",decimal=",")
#print(df["Тамож.стоим.USD"].sum())

#!!! РАЗОБРАТЬСЯ КАК ВЫВОДИТЬ ЧИСЛОВЫЕ ЗНАЧЕНИЕ В НОРМАЛЬНОМ ФОРМАТЕ
# НАПИСАТЬ КОД ВИЗУАЛИЗАЦИИ
