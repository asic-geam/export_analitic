import pandas as pd
pd.options.display.max_columns=10
#pd.options.display.max_rows=1000
import os
import numpy as np

# КОНСТАНТЫ
#===========================
# все организации РФ с инн и оквэдами
path_in_1="E:/BIGDATA/FNS/EGRUL/RESULT/"
file_in_1="inn_all(2019).csv"

# база гтд м.о. (урезанная от Мякоты А.).
path_in_2="E:/YandexDisk/ASIC/DATA/TAMOG/PARSING/"
file_in_2="moscow_reg_gtd_result.csv"

# итоговые файлы
path_out_1="E:/YandexDisk/ASIC/DATA/TAMOG/RESULT/1-STEP/"
file_out_1="all_export_moscow_reg.csv" #все отобранные компании экспортеры и потенциальные экспортеры
file_out_2="all_org_moscow_reg.csv" #все компании в регионе
#=============================

# 1. массив с инн всех экспортеров - (DF_4)

df_3=pd.read_csv(path_in_2+file_in_2,encoding="ANSI")
df_4=df_3['ИНН декларанта'].dropna() #удалаем от None
df_4=df_4.apply(lambda x: "{:.{exp}f}".format(float(x), exp=0)) #форматируем инн без вывода в экспоненте
print("Всего зарегестрировано экспортных поставок в регионе за период: " + str(len(df_4)))
df_4=df_4.drop_duplicates() # убираем дубликаты
#print(df_3.loc[df_3['ИНН декларанта']==5001000041])
print("Всего компаний экспортеров в регионе: "+str(len(df_4)))

# 2. массив с окведами экспортеров (DF_5)
df_5=pd.read_csv(path_out_1+file_out_2,encoding="ANSI") #все в регионе
df_5["ИННЮЛ"]=df_5["ИННЮЛ"].astype(str)
inn_all=df_5["ИННЮЛ"]
#print(df_5.loc[0:10,["ИННЮЛ","ОКВЭДОсн"]])

filtr_2=df_5["ИННЮЛ"].isin(df_4) # все экспортеры в общей базе компаний
print("Из них найдено соответствия по инн в регионе: "+ str(len(df_5.loc[filtr_2])))
#print(df_5.loc[filtr_2])
# помечаем в региональной базе компании экспортеры
df_5["Экспорт.статус"]="Nan"
#print(df_5.columns)
df_5.loc[filtr_2,"Экспорт.статус"] = 'ЭКСПОРТЕР' #помечаем экспортный статус

# пометить потенциальных экспортеров
# /если оквэд основной у компаний со статусом Экспортер
filtr_4=df_5["ОКВЭДОсн"].loc[filtr_2] #все оквэды экспортеров
print("Всего окведов экспортеров: "+ str(len(filtr_4)))
df_6=df_5.loc[df_5["Экспорт.статус"]!="ЭКСПОРТЕР"] #не экспортеров
filtr_3=df_5["Экспорт.статус"]=="ЭКСПОРТЕР"
okved_export=df_5["ОКВЭДОсн"].loc[filtr_3].drop_duplicates() # получаем все окведы экспортеров и убираем дубликаты
pot_export=df_6["ОКВЭДОсн"].isin(okved_export)# отфильтровываем в базе не экспортеров всех по фильтру оквэдов экспортеров
print("Всего уникальных ОКЭДОВ у экспортеров: "+ str(len(okved_export)))
df_7=df_6["ИННЮЛ"].loc[pot_export] #все потенциальные экспортеры
print("Всего потенциальных экспортеров отобранных по оквэдам экспортеров: "+ str(len(df_7)))
print(df_7)
filtr_5=df_5["ИННЮЛ"].isin(df_7) # все экспортеры в общей базе компаний
df_5.loc[filtr_5,"Экспорт.статус"] = 'ПОТЕНЦ. ЭКСП.' #помечаем экспортный статус
result=df_5.loc[df_5["Экспорт.статус"]!="Nan"]
result.to_csv(path_out_1+file_out_1,encoding="ANSI")
print("Всего экспортеров и потенциальных экспортеров в регионе:"+ str(len(result)))




"""
for i in range(len(mas_inn)):
    filtr_inn = df_5["ИННЮЛ"] == str(mas_inn[i])
    x=df_5[["ИННЮЛ","ОКВЭДОсн"] ].loc[filtr_inn]

    print(x)
"""

#df_5=df_5 #.astype(float)
#print(df_5)
# найти уникальные значения в таблице и присвоить им код оквед

#filtr_10 = df_5['ИННЮЛ'] == mas_inn[1]
#print(df_5['ИННЮЛ'])



# 3. массив со всеми организациями в регионе

   # ---
# сделали выборку из всех организаций по коду региона 50 и сохранили в отедльный файл
#df_1=pd.read_csv(path_in_1+file_in_1,encoding="ANSI")
#filtr_region=df_1["КодРегион"]==50
#df_2=df_1.loc[filtr_region]
#df_2.to_csv(path_out_1+file_out_2,encoding="ANSI")
    # ---

# 4. очищаем массив всех организаций в регионе от экспортеров
# 5. выборка из очищенного массива от экспортеров тех у кого такие же оквэды как и у экспортеров
# 6. склейка всех экспортеров с потенциальными экспортерами
# 7. формирование итоговой таблицы с полными маркерами (наименование, инн, размер, вид деятельности, статут (экспортер - потенциальный экспортер)



