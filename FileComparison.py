import requests
import urllib.request 
from bs4 import BeautifulSoup 
import zipfile, io
import os


url= 'http://staging.imgtranslate.com:9999/'
extension = ".zip"
r = requests.get(url)

html_content=r.text

soup= BeautifulSoup(html_content, "html.parser")

for anchor in soup.findAll('a', href=True):
    links = url + anchor['href']
    if links.endswith(extension):
        r2 = requests.get(links)
        z = zipfile.ZipFile(io.BytesIO(r2.content))
        z.extractall()
        
TextFiles = []
cwd = os.getcwd()



for i in os.listdir(cwd+'/a'):

    if i.endswith('.txt'):
        TextFiles.append(cwd+'/a'+'/'+i) 
       
for j in os.listdir(cwd+'/b'):
    if j.endswith('.txt'):
        TextFiles.append(cwd+'/b'+'/'+j)
        
for k in os.listdir(cwd+'/c'):
    if k.endswith('.txt'):
        TextFiles.append(cwd+'/c'+'/'+k)


for a in TextFiles:
    
    for b in TextFiles:

        with open(a) as file1:
            with open(b) as file2:
                commonLine = set(file1).intersection(file2)

        commonLine.discard('\n')

        if len(commonLine)!=0 and a!=b:
            print(str(os.path.basename(a))+ ' ' +str(os.path.basename(b)))
        

