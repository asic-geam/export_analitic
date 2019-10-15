import xml.etree.ElementTree as ET
import pandas as pd
import os

path_in="E:/BIGDATA/FNS/DOHODI/SOURCE/"
path_out="E:/BIGDATA/FNS/DOHODI/RESULT/"
dir_file=os.listdir(path_in)
file_out="dohodi_all(2019)"

#функция парсинга xml базы фнс (исленность сотрудников)
def pars_fns_all(id,path_in,file_in):
    try:
        name=(root[id][0].attrib.get("НаимОрг"))
        inn=(root[id][0].attrib.get("ИННЮЛ"))
        dohodi=(root[id][1].attrib.get("СумДоход"))
        rashodi=(root[id][1].attrib.get("СумРасход"))

    except:
        okved_osn="Nan"
    return (name, inn,dohodi,rashodi)

#создаем пустую таблицу
df=pd.DataFrame(columns=["НаимОрг", 'ИННЮЛ', "СумДоход-2018","СумРасход-2018"])
# создаем пустой файл контейнер
df.to_csv(path_out + file_out+".csv",  encoding="UTF-8")

# функция записи в csv
def obrabotka (path_in,file_in):
    # создаем пустую таблицу
    df = pd.DataFrame(columns=["НаимОрг", 'ИННЮЛ', 'СумДоход-2018',"СумРасход-2018"])
    # проходимся в цикле
    for i in range(1,len(root)-1):
        res = pars_fns_all(i, path_in, file_in)
        df = df.append({'НаимОрг': res[0], 'ИННЮЛ': res[1], 'СумДоход-2018': res[2], 'СумРасход-2018': res[3]}, ignore_index=True)
    return(df)

#проходимся по папке с файлами и записываем в csv единый
for fl in range(len(dir_file)):
    file_in=dir_file[fl]
    tree = ET.parse(path_in + file_in)
    root = tree.getroot()
    print(fl, path_in+file_in)
    df=obrabotka(path_in,file_in)
    # пишем в итоговый файл csv
    df.to_csv(path_out + file_out + ".csv", mode='a', header=False, encoding="UTF-8")  # index = False