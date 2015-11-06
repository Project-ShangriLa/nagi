# -*- coding: utf-8 -*-
import sys
import requests
import urllib

if len(sys.argv) != 2 :
    print("arguments error")
    exit(0)

title = urllib.parse.quote_plus(sys.argv[1])

#test-url
# url='http://ja.wikipedia.org/w/api.php?format=xml&action=query&prop=revisions&titles=%E3%81%AE%E3%82%93%E3%81%AE%E3%82%93%E3%81%B3%E3%82%88%E3%82%8A&rvprop=content'

url='http://ja.wikipedia.org/w/api.php?format=xml&action=query&prop=revisions&titles='+title+'&rvprop=content'

r = requests.get(url)
get=r.text

lines=[]
tmp=""
st=""

for tmp in get:
    st=st+tmp
    if tmp == "\n" :
        lines.append(st)
        st=""

flag=0
getline=""
for line in lines:
    if line.startswith("{{Infobox") == True :
        getline = getline + line
        flag=1
    if flag == 1:
        getline = getline + line
    if line.startswith("}}") ==  True :
        flag=0
print (getline)










