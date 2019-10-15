

import numpy as np
import pandas as pd
import numpy as np
#получаем данные из csv
dir="d:/asic/data/tamog/parsing/"
file="comtrade_75_nikel.csv"
#промежуточный файл
file_end="import_dinamics_75_nikel_imp.csv"
#результирующий файл
file_result="result_dinamics_75_nikel_imp.csv"
#задаем импорт или экспорт
TradeFlow="Import"
#TradeFlow="Export"

df=pd.read_csv(dir+file,encoding="utf-8")

#фильтруем от лишних cтолбоцов
df=df[['Year',"Reporter","Trade Flow","Trade Value (US$)"]]
df=df.loc[ df['Year'].isin(['2015','2016','2017','2018'])
          & df["Trade Flow"].isin([TradeFlow])
          & (df['Trade Value (US$)']>0)]
#получаем список стран
reporter=list(set(df["Reporter"]))
#создаем пустой итоговый csv файл с заголовками
non=None
data1={"Country":non,"2015":non,"2016":non,"2017":non,"2018":non}
df_2=pd.DataFrame(data1, columns=["Country","2015","2016","2017","2018"])
df_2.to_csv(dir+file_end,encoding="utf-8")

#делаем итерацию по группировке
for i in range(len(reporter)):
    #группируем по странам
    grouped=df.groupby(["Reporter"])
    result=grouped.get_group(reporter[i])
    result=(result[['Year',"Reporter","Trade Value (US$)"]])
    #передать значения в таблицу Страна, годовой импорт
    def year(god):
        result_2=result.loc[result["Year"]==god]
        year=result_2.loc[:,["Trade Value (US$)"]]
        year=(list(year['Trade Value (US$)']))
        return (year)
    #записываем в словарь
    data={"Country":reporter[i],"2015":year(2015),"2016":year(2016),"2017":year(2017),"2018":year(2018)}
    #заменяем пустые ячейки Nan
    data = {k: None if not v else v for k, v in data.items() }
    #показываем процесс обработки
    print(data)
    #передаем данные обработки, дозаписывая в созданный ранее csv файл
    df_new=pd.DataFrame(data, columns=["Country","2015","2016","2017","2018"])
    df_new.to_csv(dir+file_end,encoding="utf-8", mode = 'a', index = True, header = False)

#ЭТАП 2
# обрабатываем полученную ранее таблицу
df=pd.read_csv(dir+file_end,encoding="utf-8")
#очищаем строки в которых есть хотябы один Nan
df=df.dropna(axis=0)
#высчитываем показатель
change=((df["2018"]-df["2015"])/df["2015"])*100
#округляем после запятой
df["Change (%)"]=round(change,1)
#пишем в итоговый csv
df.to_csv(dir+file_result, encoding="utf-8",decimal=",")

#ЭТАП 3
# в ручную оформляем и причесываем файл в виде итгового xls
# ВСЕ
