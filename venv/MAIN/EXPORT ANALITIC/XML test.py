import xml.etree.ElementTree as ET
import os
#tree = ET.parse('E:/YandexDisk/ASIC/DATA/TAMOG/01 - RESOURCE/EGRUL/test.xml')
#tree = ET.parse('E:/BIGDATA/FNS/EGRUL/SOURCE/VO_RRMSPSV_0000_9965_20190910_00abd725-09fe-4dbf-8c3b-27d33c14958a.xml')
path_in="E:/BIGDATA/FNS/EGRUL/SOURCE/"
dir_file=os.listdir(path_in)
file_in=dir_file[4]
tree = ET.parse(path_in+file_in)

root = tree.getroot()
print(len(root))
for id in range(1,len(root)):
    print(id)
    try:
        #print(root[id][2][0].attrib.get('КодОКВЭД'))
        print(root[id].attrib.get("ДатаВклМСП"))

    except:
        print ("--------")


print(root[900][2][0].attrib.get('КодОКВЭД'))
#for elem in root.findall("*"):
#    print(elem.attrib("КодОКВЭД"))

    #okved_osn = root[i][0].attrib
    #okved_osn = root[id][2][0].attrib['КодОКВЭД']
    #print(okved_osn)

#for elem in root:
#    print(elem[0])
#    print(elem)
#    print("__________")
    #print(elem.attrib)
    #print(elem.items)
    #print(elem.attrib.get("ВидСубМСП"))
    #print(elem[2].find('СвОКВЭДДоп'))
"""
print(root[2][0].attrib.get('ИННФЛ'))
print(root[2][0][0].attrib.get('Фамилия'))
print(root[2][0][0].attrib.get('Имя'))
print(root[2][0][0].attrib.get('Отчество'))
val=root[900]
print(val)
print(root[1][1].attrib.get('КодРегион'))
#print("-------",val.find("Документ").attrib.get("ВидСубМСП"))
"""