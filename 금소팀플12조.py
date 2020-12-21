from bs4 import BeautifulSoup
import requests
import webbrowser


topic = input('단어를 입력하시오:')

#싱어게인 관련단어
title=[]


page = 1
end=11
while page < end:


    url = 'https://search.naver.com/search.naver?where=news&sm=tab_jum&query=싱어게인&start='+str(page)
    req = requests.get(url)
    req

    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    titles = soup.select('ul.list_news > li')



    for i in titles:
        news = i.select_one('a.news_tit')
        articles = news. text
        title.append(articles)
    page+=1


titles = ' '.join(title)

singagain = titles.split()



count1 = 0


for i in range(len(singagain)):
    if singagain[i] == topic:
        count1+= 1
    i+= 1

print('검색중...')

#아는형님 관련단어
title=[]
page = 1
end=11

while page < end:


    url = 'https://search.naver.com/search.naver?where=news&sm=tab_jum&query=아는형님&start='+str(page)
    req = requests.get(url)
    req

    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    titles = soup.select('ul.list_news > li')



    for i in titles:
        news = i.select_one('a.news_tit')
        articles = news. text
        title.append(articles)
    page+=1


titles = ' '.join(title)

anenheagnim = titles.split()


count2 = 0


for i in range(len(anenheagnim)):
    if anenheagnim[i] == topic:
        count2+= 1
    i+= 1

print('검색중...')

#뭉쳐야찬다 관련단어
title=[]
page = 1
end=11

while page < end:


    url = 'https://search.naver.com/search.naver?where=news&sm=tab_jum&query=뭉쳐야찬다&start='+str(page)
    req = requests.get(url)
    req

    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    titles = soup.select('ul.list_news > li')



    for i in titles:
        news = i.select_one('a.news_tit')
        articles = news. text
        title.append(articles)
    page+=1


titles = ' '.join(title)

mong = titles.split()

count3 = 0


for i in range(len(mong)):
    if mong[i] == topic:
        count3+= 1
    i+= 1

print('검색중...')

#1호가될순없어 관련단어
title=[]
page = 1
end=11

while page < end:


    url = 'https://search.naver.com/search.naver?where=news&sm=tab_jum&query=1호가될순없어&start='+str(page)
    req = requests.get(url)
    req

    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    titles = soup.select('ul.list_news > li')



    for i in titles:
        news = i.select_one('a.news_tit')
        articles = news. text
        title.append(articles)
    page+=1


titles = ' '.join(title)

firstcant = titles.split()

count4 = 0


for i in range(len(firstcant)):
    if firstcant[i] == topic:
        count4+= 1
    i+= 1

print('검색중...')

#갬성주점 관련단어
title=[]
page = 1
end=11

while page < end:


    url = 'https://search.naver.com/search.naver?where=news&sm=tab_jum&query=갬성캠핑&start='+str(page)
    req = requests.get(url)
    req

    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    titles = soup.select('ul.list_news > li')



    for i in titles:
        news = i.select_one('a.news_tit')
        articles = news. text
        title.append(articles)
    page+=1


titles = ' '.join(title)

gamsang = titles.split()

count5 = 0


for i in range(len(gamsang)):
    if gamsang[i] == topic:
        count5+= 1
    i+= 1

print('검색중...')

#서울엔우리집이없다 관련단어
title=[]
page = 1
end=11

while page < end:


    url = 'https://search.naver.com/search.naver?where=news&sm=tab_jum&query=서울엔우리집이없다&start='+str(page)
    req = requests.get(url)
    req

    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    titles = soup.select('ul.list_news > li')



    for i in titles:
        news = i.select_one('a.news_tit')
        articles = news. text
        title.append(articles)
    page+=1


titles = ' '.join(title)

seaul = titles.split()

count6 = 0


for i in range(len(seaul)):
    if seaul[i] == topic:
        count6+= 1
    i+= 1

print('검색중...')

#방구석1열 관련단어
title=[]
page = 1
end=11

while page < end:


    url = 'https://search.naver.com/search.naver?where=news&sm=tab_jum&query=방구석1열&start='+str(page)
    req = requests.get(url)
    req

    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    titles = soup.select('ul.list_news > li')



    for i in titles:
        news = i.select_one('a.news_tit')
        articles = news. text
        title.append(articles)
    page+=1


titles = ' '.join(title)

banggu = titles.split()

count7 = 0


for i in range(len(banggu)):
    if banggu[i] == topic:
        count7+= 1
    i+= 1

print('검색중...')

#최고 빈도 찾기
count= [count1, count2, count3, count4, count5, count6, count7]

URLlist= ['https://search.naver.com/search.naver?where=nexearch&sm=top_sug.pre&fbm=1&acr=1&acq=%EC%8B%B1%EC%96%B4%EA%B2%8C%EC%9D%B8%ED%8E%B8&qdt=0&ie=utf8&query=%EC%8B%B1%EC%96%B4%EA%B2%8C%EC%9D%B8+%ED%8E%B8%EC%84%B1%ED%91%9C','https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%95%84%EB%8A%94%ED%98%95%EB%8B%98+%ED%8E%B8%EC%84%B1%ED%91%9C','https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EB%AD%89%EC%B3%90%EC%95%BC%EC%B0%AC%EB%8B%A4+%ED%8E%B8%EC%84%B1%ED%91%9C','https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=1%ED%98%B8%EA%B0%80%EB%90%A0%EC%88%9C%EC%97%86%EC%96%B4+%ED%8E%B8%EC%84%B1%ED%91%9C','https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EA%B0%AC%EC%84%B1%EC%BA%A0%ED%95%91+%ED%8E%B8%EC%84%B1%ED%91%9C','https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%84%9C%EC%9A%B8%EC%97%94%EC%9A%B0%EB%A6%AC%EC%A7%91%EC%9D%B4%EC%97%86%EB%8B%A4+%ED%8E%B8%EC%84%B1%ED%91%9C','https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EB%B0%A9%EA%B5%AC%EC%84%9D1%EC%97%B4+%ED%8E%B8%EC%84%B1%ED%91%9C']

if max(count) == 0:
    print('일치하는 예능을 찾지 못해 죄송합니다. 더 좋은 서비스를 위해 항상 노력하겠습니다.')
    
    
else:
    for i in range(len(count)):
        if max(count) == count[i]:
            URL = URLlist[i]
        i+=1

#해당 예능 편성표 열기
    webbrowser.open_new(URL)

