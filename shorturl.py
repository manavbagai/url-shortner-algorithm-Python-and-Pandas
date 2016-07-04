import numpy as np
import pandas as pd
class convert1:
    __map=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9"]
    def __init__(self,id1):
        self.id1=id1
    def convert22(self):
        shorturl=""
        while (self.id1)>0:
            shorturl=shorturl+ convert1.__map[int(self.id1%62)]
            self.id1=int(self.id1/62)
        
        return shorturl[::-1]
class input1:
    def __init__(self,url):
        self.url=url
    def database_entry(self):
        file=pd.read_csv("data.csv",names=["id","url","surl"],header=0)
        x=int(file.shape[0])
        x=x+1
        if (self.url) in file.url.values:
            x=file[file.url==self.url].id
            w=file[file.url==self.url].surl
            print(w.values[0])
            return(w.values[0])
            
        else:
            c1=convert1(x)
            w=c1.convert22()
            x=x-1
            data2={"id":[x],"url":[self.url],"surl":[w]}
            file.loc[x]=[int(x),self.url,"www.mb.com/"+w]
            file.to_csv("data.csv")
            print("www.mb.com/"+w)
            return("www.mb.com/"+w)   
      
class output1:
    def __init__(self,surl):
        self.surl=surl
    def full_url(self):
        file1=pd.read_csv("data.csv",names=["id","url","surl"],header=0)
        w=file1[(file1.surl)==(self.surl)].url
        return(w.values[0])
url=input("Enter url")
x=input1(url)
y=x.database_entry()
q=output1(y)
z=q.full_url()
print("Short URL: "+y+" Long URL "+z)
