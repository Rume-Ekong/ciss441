from bs4 import BeautifulSoup
import requests

myzips = list()
myzips.append(['cd_28146','http://www.city-data.com/zips/28146.html'])
myzips.append(['zi_28146','https://www.zillow.com/homes/28146_rb'])
myzips.append(['wi_sal_nc','https;//en.wikipedia.org/wiki/Salisbury,_North_Carolina'])
myzips.append(['wi_leeu','https://en.wikipedia.org/wiki/Lee_University'])
for myzipdata in myzips:
    
    mytype, mypageurl = myzipdata
    res = requests.get(mypageurl)
    webcontent = res.text
    #with open(mytype + '.txt', mode='w') as fo:
        #fo.write(webcontent)
        
    soup = BeautifulSoup(webcontent, "html.parser")
    print('n\n', mypageurl, res.status_code)
    ptitle = soup.title
    if ptitle:
        print(ptitle.string)
        
    for lnkct, link in enumerate(soup.find_all('a')):
        lnk = link.get('href')
        if lnk and lnkct < 3:
            print('  ' + lnk)
    #with open(mytype + '_justtext.txt', mode='w') as fo:
        #fo.write(soup.get_text())