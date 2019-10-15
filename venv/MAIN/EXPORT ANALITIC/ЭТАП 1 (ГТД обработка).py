import pandas as pd
#задаем сколько строк и колонок выводится в пандасе
pd.options.display.max_rows = 1000
pd.options.display.max_columns = 1000

dir="E:/YandexDisk/ASIC/DATA/TAMOG/PARSING/"
file="test-3.csv"
data=pd.read_csv(dir+file,encoding="ANSI",sep=";",low_memory=False)
print(len(data))
filtr_1=data["G011 (ИМ/ЭК)"]=="ЭК"
filtr_2=data["G021 (ИНН отправителя)"]!="NaN"
data=data.loc[filtr_1 & filtr_2]
data.to_csv(dir+"test-res.csv",encoding="ANSI")
#print(data.loc[:,["G022 (Отправитель)","G021 (ИНН отправителя)",'G12 (Общая тамож.стоимость)']])
print(len(data))
print(data.loc[:,["G022 (Отправитель)",'G12 (Общая тамож.стоимость)']])
print(data.loc[:,['G12 (Общая тамож.стоимость)']])
