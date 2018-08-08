# coding: utf-8

import os
import subprocess
import sqlite3
import sys
from collections import Counter


def getgoohistoryword():
    """
    グーグルのフォルダーにアクセスして、
    自身の履歴を取得し、そこから言葉を取り出す
    """
    cmd = 'cp -R /Users/fenganling/Library/Application\ Support/Google/Chrome/Default/History tmpsql.text'
    subprocess.run(cmd, shell=True)
    conn = sqlite3.connect('tmpsql.text')
    cur = conn.cursor()
    sql = "select urls.title from visits left join urls on visits.url = urls.id;"
    cur.execute(sql)

    alldata=[]
    #全てのデータ
    replacewords =["YouTube" , '|' , '-']
    for row in cur:
        rowstring = str(row[0])
        for replaceword in replacewords:
            rowstring.replace(replaceword,"")
        oneulrdata = rowstring.split(' ')
        alldata.extend(oneulrdata)

    c = Counter(alldata)
    #カウンターオブジェクトを丸ごと渡すのは動作が重くなるが、わかりやすさを重視
    return c


class GoogleHistory:
    def __init__(self):
        cmd = 'cp -R /Users/fenganling/Library/Application\ Support/Google/Chrome/Default/History jojo.text'
        subprocess.run(cmd, shell=True)
        self.__conn = sqlite3.connect('jojo.text')
        self.cur = self.__conn.cursor()

    def sqlcommand(self,sql="select urls.title from visits left join urls on visits.url = urls.id;"):
        self.cur.execute(sql)
    
    def returnword(self):
        """
        return word by "from collections import Counter"
        """
        alldata=[]
        replacewords =["YouTube" , '|' , '-']
        for row in self.cur:
            rowstring = str(row[0])
            for replaceword in replacewords:
                rowstring.replace(replaceword,"")
            oneulrdata = rowstring.split(' ')
            alldata.extend(oneulrdata)

        c = Counter(alldata)

        return c
    
    def __del__(self):
        self.cur.close()
        self.__conn.close()
        

if __name__=='__main__':
    gohisObj=GoogleHistory()
    gohisObj.sqlcommand()
    c=gohisObj.returnword()
    print(c)
    del gohisObj