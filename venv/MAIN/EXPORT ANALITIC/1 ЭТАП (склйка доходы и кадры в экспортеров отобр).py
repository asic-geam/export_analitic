import pandas as pd
import os

#задаем пути к рабочим файлам
file_dohodi="E:/BIGDATA/FNS/DOHODI/RESULT/dohodi_all(2019).csv"
file_kadri="E:/BIGDATA/FNS/KADRI/RESULT/kadri_all(2019).csv"
file_okved="E:/YandexDisk/ASIC/DATA/TAMOG/01 - RESOURCE/OKVED_TNVED/okved_data.csv"
file_export_comp_reg="E:/YandexDisk/ASIC/DATA/TAMOG/RESULT/1-STEP/all_export_moscow_reg.csv"
gtd_comp="E:/YandexDisk/ASIC/DATA/TAMOG/RESULT/1-STEP/moscow_reg_gtd_result.csv"
#функция добавления столбцов в итоговый файл

df_main=pd.read_csv(file_export_comp_reg,encoding="ANSI")
#df_main=df_main.loc[df_main['Экспорт.статус']=="ЭКСПОРТЕР",["ИННЮЛ","НаимОргСокр"]]
#print(len(df_main))
#df_gtd=pd.read_csv(gtd_comp,encoding="ANSI")
#print(len(df_gtd.drop_duplicates("ИНН декларанта")))#ИНН декларанта

df_kadri=pd.read_csv(file_kadri,encoding="UTF-8")
df_kadri=df_kadri.drop('НаимОрг', axis=1)
df_okved=pd.read_csv(file_okved,encoding="ANSI")
df_dohodi=pd.read_csv(file_dohodi,encoding="UTF-8")
df_dohodi=df_dohodi.drop('НаимОрг', axis=1)

#print(len(df_main['Экспорт.статус']=="ЭКСПОРТЕР"))

df_new=df_main.merge(df_dohodi,how='left', left_on='ИННЮЛ', right_on='ИННЮЛ')
df_new=df_new.merge(df_kadri,how='left', left_on='ИННЮЛ', right_on='ИННЮЛ')
df_new=df_new.merge(df_okved,how='left', left_on='ОКВЭДОсн', right_on='Официальный код')

df_new.to_csv("E:/YandexDisk/ASIC/DATA/TAMOG/RESULT/1-STEP/merge_all_export.csv",encoding="UTF-8")

