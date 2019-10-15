import pandas as pd

#загружаем данные
file="result_rca.csv"
path="d:/asic/data/tamog/temp/"
df=pd.read_csv(path+file,encoding="utf-8")

#лидеры по отрасли
#lider=df["01"]>df["01"].mean()
#df_lider=df.loc[lider,["Country"]])

#список с кодами отраслей, всего 99 секторов, 00 - это все индустрии
key_ind=list(range(1,100))
for i in range(9):
    key_ind[i]="0"+str(key_ind[i])
for i in range(9,99):
    key_ind[i]=(str(key_ind[i]))

#print(key_ind)

file_txt="lider_rca.txt"
f=open(path+file_txt,"a",encoding="utf-8")
country_rca=[]
for i in range(len(key_ind)):
    key=key_ind[i]
    lider=df[key]>df[key].mean()
    df2=(df.loc[lider,["Country",key]])
    df2['txt']=df2["Country"].astype(str)+"_"+"("+df2[key].astype(str)+")"
    country=str(list(df2["txt"]))
    #print(country)

    #for k in range(len(country)):
    #   print(country[k])
    f.write("Страны лидеры по RCA в отрасли - "+str(key)+'\n'+ country[:]+'\n')
#print(country_rca)

