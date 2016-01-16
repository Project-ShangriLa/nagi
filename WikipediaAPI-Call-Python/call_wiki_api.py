# -*- coding: utf-8 -*-
import sys
import requests
import urllib

# 本文取得
def gethtml(argv):
    title = urllib.parse.quote_plus(sys.argv[1])
    url='http://ja.wikipedia.org/w/api.php?format=xml&action=query&prop=revisions&titles='+title+'&rvprop=content'
    r = requests.get(url)
    return r.text

# linesに本文htmlを1行毎にリストに格納
def linesget(get):
    lines=[]
    tmp=""
    st=""
    for tmp in get:
        st=st+tmp
        if tmp == "\n" :
            lines.append(st)
            st=""
    return lines

#-------main--------------------
if __name__ == '__main__' :
    lines=[]
    infolines=[]
    #引数処理
    if len(sys.argv) != 2 :
        print("arguments error")
        exit(0)

    #本文html取得
    get=gethtml(sys.argv[1])

    #1行毎にリストに格納
    lines=linesget(get)

    #声優一覧取得
    line=""
    for line in lines :
        if '声優|声' in line :
            print(line)
        if '声 - ' in line :
            print(line)

    # infoboxを抜き出す
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
    #1行毎にリストに格納
    infolines=linesget(getline)

    #infobox内の指定情報取得
    line=""
    for line in infolines :
        if '監督' in line :
            print(line)
        if 'キャラクターデザイン' in line :
            print(line)
        if 'アニメーション制作' in line :
            print(line)
        # if '出版社' in line :
        #     print(line)
        # if '原作' in line :
        #     print(line)
        # if 'レーベル' in line :
        #     print(line)




