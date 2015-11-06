#Wikipedia API Call 

## 概要

Wikipediaからアニメの情報を取ってきます．

## 実行
```
 python3 call_wiki_api.py "アニメのタイトル"  
```

第一引数の単語でアニメタイトルを指定し、そのアニメの情報をwikipediaから取ってきます．

## note
 - とりあえずwikipediaのinfoboxをまるごと取り出すだけです．  
 この中から必要な情報を抽出して、整形する予定． キャスト情報の抽出は考え中です．  
 - アニメタイトルと原作のwikipediaの本文が別けられているものは対応できません． 

