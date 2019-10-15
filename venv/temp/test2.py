import xml.etree.ElementTree as ET
import pandas as pd
import os

path_in="E:/BIGDATA/FNS/EGRUL/SOURCE/"
path_out="E:/BIGDATA/FNS/EGRUL/RESULT/"


#функция парсинга xml базы фнс
def pars_fns_all(id,path_in,file_in):
    if root[id][0].attrib.get('ИННЮЛ')==None:
        inn = root[id][0].attrib.get('ИННФЛ')
        nm1 = root[id][0][0].attrib.get('Фамилия')
        nm2 = root[id][0][0].attrib.get('Имя')
        nm3 = root[id][0][0].attrib.get('Отчество')
        full_name = "ИП " + str(nm1) +" " + str(nm2) +" "+ str(nm3)
    else:
        full_name=root[id][0].attrib.get('НаимОргСокр')
        inn=root[id][0].attrib.get('ИННЮЛ')
    okved_osn = root[id][2][0].attrib['КодОКВЭД']
    mas = []
    for okved_dop in root[id][2].findall('СвОКВЭДДоп'):
        kod = okved_dop.get('КодОКВЭД')
        mas.append(kod)
    region=root[id][1].attrib.get('КодРегион')
    #dict={"НаимОргСокр": full_name, 'ИННЮЛ':inn, 'КодРегион':region, "ОКВЭДОсн":okved_osn,"ОКВЭДДоп":(mas)}
    #return (dict)
    return (full_name, inn, region, okved_osn,mas)
#создаем пустую таблицу
df=pd.DataFrame(columns=["НаимОргСокр", 'ИННЮЛ', 'КодРегион',"ОКВЭДОсн","ОКВЭДДоп"])


dir_file=os.listdir(path_in)
#len(dir_file)
for g in range(10):
    print(dir_file[g])
    file_in=dir_file[g]
    tree = ET.parse(path_in+file_in)
    root = tree.getroot()
    #проходимся в цикле и пишем в итоговый файл csv
    file_out="res.csv"
    for i in range(1,len(root)):
        res = pars_fns_all(i, path_in, file_in)
        df = df.append({'НаимОргСокр': res[0], 'ИННЮЛ': res[1], 'КодРегион': res[2], 'ОКВЭДОсн': res[3], 'ОКВЭДДоп': res[4]}, ignore_index=True)
    df.to_csv(path_out+file_out,encoding="ANSI")





