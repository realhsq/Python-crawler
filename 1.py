from urllib.request import urlopen
from urllib.request import Request
from urllib import parse
from bs4 import BeautifulSoup
import os
import re
import ssl
url = 'https://muse.jhu.edu/issue/938'
req = Request(url)
req.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36")
res = urlopen(req)
data =res.read().decode("utf-8")
soup = BeautifulSoup(data,"lxml")
infoList = soup.find_all('a')
#print(infoList)

folder = 'haha1'
if(os.path.exists(folder) == False):
    os.mkdir(folder)
os.chdir(folder)

for info in infoList:
    if(len(re.compile(r'Download').findall(info.text.strip()))):
        response = urlopen('https://muse.jhu.edu' + info['href'])
        filename = info['href'] + '.pdf'
        filename = filename.replace('/','')
        file =response.read()
        # 文件存储
        with open(filename,'wb') as f:
            print("save -> %s " % filename)
            f.write(file)