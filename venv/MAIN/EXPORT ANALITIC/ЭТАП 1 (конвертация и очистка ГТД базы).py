import pandas as pd
dir="E:/YandexDisk/ASIC/DATA/TAMOG/PARSING/"
file="moscow_reg_gtd.xlsx"
file_1="moscow_reg_gtd_result.csv"
#df=pd.read_excel(dir+file,nrows=2250)

dir_3="E:/YandexDisk/ASIC/DATA/TAMOG/01 - RESOURCE/OKVED_TNVED/"
file_3="okved_data.csv"
df_2=pd.read_csv(dir_3+file_3,encoding="ANSI")
print(df_2.columns)
filtr_a=df_2['Раздел']=="A"
filtr_b=df_2['Раздел']=="B"
filtr_c=df_2['Раздел']=="C"
df_2=df_2.loc[filtr_a + filtr_b + filtr_c]



#датасет 1 Выборка по инн все компании экспортеры в регионе (есть база Мякоты)
#датасет 2 Сгруппировать по вед всех экспортеров
#отфильтровать всех экспортеров оставив только производителей (разделы А, В, С) и убрав услуги

#df=df.loc[:,["ИНН декларанта","Код ТН ВЭД","Описание и характеристика товара","Наименование декларанта","Страна происхождения товара","Страна назначения","Валюта контракта","Таможенная стоимость"]]

#df.to_csv(dir+file_1, encoding="cp1251")
#print(len(df))

