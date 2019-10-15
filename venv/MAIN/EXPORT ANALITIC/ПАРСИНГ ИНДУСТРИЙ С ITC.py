import pandas as pd
#url="https://tradecompetitivenessmap.intracen.org/TP_EP_IC.aspx?IN=01&YR=2014"
#data=pd.read_html(url)
#path="d:/asic/data/tamog/parsing/"
#file="itc_all.csv"
#data[2].to_csv(path+file,encoding="utf-8")
#print(data[2])

#генерация ссылок ITC
aspx="TP_EP_IC" #вместо EP - IP если по импорту
year="2016"
def ITC_URL(aspx,industry,year):
    url="https://tradecompetitivenessmap.intracen.org/"+aspx+".aspx?"+"IN="+industry+"&YR="+year
    return (url)

#список с кодами отраслей, всего 99 секторов, 00 - это все индустрии
key_ind=list(range(0,100))
for i in range(len(key_ind)):
    if key_ind[i]<10:
        key_ind[i]=("0"+str(i))

#парсим по всем индустриям 100 файлов в итоге в папке должно лежать
path="d:/asic/data/tamog/parsing/"
for i in range(len(key_ind)):
    industry=str(key_ind[i])
    url=ITC_URL(aspx,industry,"2016")
    data=pd.read_html(url)
    file="itc_indust_"+str(key_ind[i])+".csv"
    data[2].to_csv(path+file,encoding="utf-8")
    print("датасет по индустрии №"+str(key_ind[i])+"готов" )
