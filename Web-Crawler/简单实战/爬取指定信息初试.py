import requests
import bs4
from bs4 import BeautifulSoup

def getHTMLText(url):
    try:
        r = requests.get(url,timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("爬取失败")
        return ""
def fillUnivlist(ulist,html):
    soup = BeautifulSoup(html,"html.parser")
    for tr in soup.find('tbody').children:
        '''

        print(tr)
        type(tr)
        dir(tr)
        break           #######
        '''
        if isinstance(tr,bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string,tds[1].string,tds[2].string,])


def printUnivList(ulist, num):
    tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}"
    print(tplt.format("排名","学校名称","总分",chr(12288)))
    for i in range(num):
        u=ulist[i]
        print(tplt.format(i+1,u[1],u[2],chr(12288)))

        
def main():
    num = 20
    uinfo = []
    url = "http://www.zuihaodaxue.com/zuihaodaxuepaiming2017.html"
    html = getHTMLText(url)
    fillUnivlist(uinfo,html)
    printUnivList(uinfo,num)

main()
