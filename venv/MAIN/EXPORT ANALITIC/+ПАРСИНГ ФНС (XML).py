import xml.etree.ElementTree as ET
import pandas as pd
import os

path_in="E:/BIGDATA/FNS/EGRUL/SOURCE/"
path_out="E:/BIGDATA/FNS/EGRUL/RESULT/"
dir_file=os.listdir(path_in)
file_out="inn_all(2019)"


#функция парсинга xml базы фнс
def pars_fns_all(id,path_in,file_in):
    if root[id].get('ВидСубМСП')=="2": #ип
        inn = root[id][0].attrib.get('ИННФЛ')
        nm1 = root[id][0][0].attrib.get('Фамилия')
        nm2 = root[id][0][0].attrib.get('Имя')
        nm3 = root[id][0][0].attrib.get('Отчество')
        full_name = "ИП " + str(nm1) +" " + str(nm2) +" "+ str(nm3)
    else: #организация
        full_name=root[id][0].attrib.get('НаимОргСокр')
        inn=root[id][0].attrib.get('ИННЮЛ')
    mas = []
    for okved_dop in root[id][2].findall('СвОКВЭДДоп'):
        kod = okved_dop.get('КодОКВЭД')
        mas.append(kod)
    #Обходим ошибки
    try:
        okved_osn = root[id][2][0].attrib.get('КодОКВЭД')
    except:
        okved_osn="Nan"
    region=root[id][1].attrib.get('КодРегион')
    return (full_name, inn, region, okved_osn,mas)

#создаем пустую таблицу
df=pd.DataFrame(columns=["НаимОргСокр", 'ИННЮЛ', 'КодРегион',"ОКВЭДОсн","ОКВЭДДоп"])
# создаем пустой файл контейнер
df.to_csv(path_out + file_out+".csv",  encoding="ANSI")

# функция записи в csv
def obrabotka (path_in,file_in):
    #tree = ET.parse(path_in + file_in)
    #root = tree.getroot()
    # создаем пустую таблицу
    df = pd.DataFrame(columns=["НаимОргСокр", 'ИННЮЛ', 'КодРегион', "ОКВЭДОсн", "ОКВЭДДоп"])
    # проходимся в цикле
    for i in range(3,len(root)-1):
        res = pars_fns_all(i, path_in, file_in)
        df = df.append({'НаимОргСокр': res[0], 'ИННЮЛ': res[1], 'КодРегион': res[2], 'ОКВЭДОсн': res[3], 'ОКВЭДДоп': res[4]}, ignore_index=True)
    return(df)

#проходимся по папке с файлами и записываем в csv единый
for fl in range(len(dir_file)):
    file_in=dir_file[fl]
    tree = ET.parse(path_in + file_in)
    root = tree.getroot()
    print(fl, path_in+file_in)
    df=obrabotka(path_in,file_in)
    # пишем в итоговый файл csv
    df.to_csv(path_out+file_out +".csv",  mode='a', header=False, encoding="ANSI") #index = False
