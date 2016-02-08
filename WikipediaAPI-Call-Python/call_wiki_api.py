# -*- coding: utf-8 -*-
import sys
import requests
import urllib
import re

# 本文取得
def gethtml(argv):
    title = urllib.parse.quote_plus(argv)
    url='http://ja.wikipedia.org/w/api.php?format=xml&action=query&prop=revisions&titles='+title+'&rvprop=content'
    r = requests.get(url)
    #wikipediaのページが取ってこれなければエラーを返す
    if "missing" in r.text :
        print("wiki page not find")
        sys.exit(0)
    else:
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


#アニメ制作の情報を抽出
def get_infobox(lines):
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
    infolines=[]
    infolines=linesget(getline)

    #infobox内の指定情報取得
    info=[]
    for line in infolines :
        if '監督' in line :
            info.append("監督")
            info+=re.findall('\[+(.*?.)\]+',line)
        if 'キャラクターデザイン' in line :
            info.append("キャラデザ")
            info+=re.findall('=(.*)',line)
        if 'アニメーション制作' in line :
            info.append("制作")
            info+=re.findall('=(.*)',line)
        # if '出版社' in line :
        #     info.append("出版社")
        #     info+=re.findall('=(.*)',line)
        # if '原作' in line :
        #     info.append("原作")
        #     info+=re.findall('=(.*)',line)
        # if 'レーベル' in line :
        #     info.append("レーベル")
        #     info+=re.findall('=(.*)',line)
    return info
##アニメ制作の情報を抽出-----ここまで---------


#声優一覧取得
def get_cv_list(lines):
    cv_list=[]
    for line in lines :
        if '声優|声' in line :
            cv_list+=re.findall('\[+(.*?.)\]+',line)
        if '声 - ' in line :
            cv_list+=re.findall('\[+(.*?.)\]+',line)
    return cv_list


#エラー表示
def print_error():
    print("argument error")
    print("python3 call_wiki_api.py [param] [anime_title] ")
    print("argument : [-c] or [-i] ")
    print(" [-c] : print charactor voice ")
    print(" [-i] : print info ")
    sys.exit(1)
#-------main--------------------
if __name__ == '__main__' :

    #引数処理
    param = sys.argv
    argc = len(param)

    if argc != 2 and argc != 3 and argc != 4 :
        print_error()

    pflag=-1
    if argc == 2 :  pflag=0
    if "-c" in param : pflag+=2
    if "-i" in param : pflag+=3
    print(argc)
    print(pflag)

    if( argc == 3 or argc ==4 ) and pflag < 0 :
        print_error()

   #本文html取得
    get=gethtml(str(param[-1]))
    #1行毎にリストに格納
    lines=[]
    lines=linesget(get)

    #声優一覧取得
    if pflag != 2 :
        cv_list=[]
        cv_list=get_cv_list(lines)
        print(cv_list)

    # infoboxを抜き出す
    if pflag == 1 :  sys.exit(0)
    infolines=[]
    infolines=get_infobox(lines)
    print(infolines)


