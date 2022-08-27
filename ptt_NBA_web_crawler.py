import requests
from bs4 import BeautifulSoup
import time
from datetime import date, timedelta 

today = time.strftime('%m/%d').lstrip('0')

def pttNBA(url):
    resp = requests.get(url)
    if resp.status_code != 200:
        print('URL發生錯誤：' + url)
        return
    
    soup = BeautifulSoup(resp.text, 'html5lib')
    paging = soup.find('div', 'btn-group btn-group-paging').find_all('a')[1]['href']
    print(paging)
    
    articles = []
    rents = soup.find_all('div', 'r-ent')
    for rent in rents:
        title = rent.find('div', 'title').text.strip()
        count = rent.find('div', 'nrec').text.strip()
        dates = rent.find('div', 'meta').find('div', 'date').text.strip()
        article = '%s %s:%s' % (dates, count, title)
        
         
        five_day_ago = date.today() - timedelta(5) 
        five_day_ago =five_day_ago.strftime('%m/%d').lstrip('0')
        
        #抓取至5天前的文章
        if dates > five_day_ago:
            articles.append(article)
        
        '''
        #抓取今天的文章且推文數大於10,或為爆    
        try:
            if today == date and int(count) > 10:
                articles.append(article)
        except:
            if today == date and count == '爆':
                articles.append(article)
       '''

    if len(articles) != 0:
        for article in articles:
            print(article)
        pttNBA('https://www.ptt.cc' + paging)
    else:
        return
    
pttNBA('https://www.ptt.cc/bbs/NBA/index.html')