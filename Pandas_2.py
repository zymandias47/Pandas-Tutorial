import pandas as pd
from numpy.random import randn

df = pd.DataFrame(randn(3,3),index = ["A","B","C"],columns =["Sütun 1","Sütun 2","Sütun 3"] )
"""
#Sadece kolonu yada tipini yazdırmak için
result = df["Sütun 1"]
print(result)
results =type(df["Sütun 1"])
print(results)

#Aynı anda birden fazla sütunu yazddırmak için ama bi liste içine alınnı dikkat et
resul = df[["Sütun 1","Sütun 2"]]
print(resul)

"""
# Her bir satırı yazdırmak için
#result = df.loc["A"]

# Loc metedo ile oluşan Dateframein her bir öğesine olaşabiliriz  df.loc["row","columns"]
#results = df.loc["A","Sütun 1"]

#Saadece ilk sütünu yazdırmak içinn loc
#resolt = df.loc[:,"Sütun 1"]
deb = df.loc[:,["Sütun 1","Sütun 2"]]

result = df.loc[:,"Sütun 1":"Sütun 3"] #Bunda ise aralık belirtiriz
results = df.loc[:,:"Sütun 3"] # böylede kullanılabilir
#aynı işlemler satır işlemleri içinde geçerlidir
#İndex numarası ile satır çağırmak için iloc metodu vardır
result = df.iloc[2]

#Yeni bi sütüun eklemek için bunun için bi seri oluştururuz
df["Sütün 4"] = pd.Series(randn(3),["A","B","C"])
#Diğer bi yötem ise
df["Sütun 5"] = df["Sütun 1"] + df["Sütun 3"]

#Sütun silmek için
#print(df.drop("Sütun 5",axis = 1))

#print(df)