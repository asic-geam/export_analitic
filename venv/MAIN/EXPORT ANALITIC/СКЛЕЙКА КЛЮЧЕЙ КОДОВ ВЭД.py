import pandas as pd
import os
path_in="E:/YandexDisk/ASIC/DATA/TAMOG/01 - RESOURCE/OKVED_TNVED/"
path_out=path_in
dir_file=os.listdir(path_in)
file_in=dir_file[3]
print(file_in)
df=pd.read_excel(path_in+file_in) #,na_values=['Код ОКПД2 (6 зн.)', 'Код ТН ВЭД (6 зн.)']
print(df.columns)
print(df[['Код ОКПД2 (6 зн.)','Код ТН ВЭД (6 зн.)']])

df.to_csv(path_out+"baze_tnved_okpd_okved.csv", encoding="ANSI")
#разобраться почему нектороые коды тн вед пустые при экспорте в csv ???