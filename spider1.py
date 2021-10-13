import requests
import os
n=1
history=open('history.txt','r+')
m=history.read()
history.close
m=int(m)
print("确保同一目录下有history.txt文件且其中有数字用以读取")
print("图片存储路径为D:/jpg/")
while True:
    if n<10:
        num="0"+str(n)
    else:
        num=str(n)
    url="https://img.i1m2g3e.com/passimg/kt/"+str(m)+"/"+num+".jpg"
    response = requests.get(url=url)
    text=response.text
    if text.count("404 Not Found")==0:
        page_text=response.content
        if num=='01':
            os.mkdir("D:/jpg/"+str(m))
        filename=str(m)+'/'+num+".jpg"
        with open(filename,'wb') as fp:
            fp.write(page_text)
        print(str(m)+" "+num+"爬取成功")
        n=n+1
    else:
        print(str(m)+" "+num+"爬取结束")
        m=m+1
    if n>20:
        m=m+1
        n=1
    history=open("history.txt",'w')
    history.write(str(m+1))

