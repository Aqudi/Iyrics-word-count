# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import urllib, traceback, os, sys
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "word_counter.settings")
django.setup()
from word_app.models import lyrics

def getData(keyword):
    chrome_options = Options()
    chrome_options.add_argument('headless')
    chrome_options.add_argument('window-size=1920x1080')
    chrome_options.add_argument("disable-gpu")
    ua = UserAgent()
    chrome_options.add_argument('User-Agent='+ua.chrome)
    try:
        drive_path = os.path.abspath("chromedriver.exe")
        # print(drive_path)
        web = webdriver.Chrome(executable_path=drive_path, options=chrome_options)
    except:
        drive_path = os.path.abspath("chromedriver")
        # print(drive_path)
        web = webdriver.Chrome(executable_path=drive_path, options=chrome_options)

    web.implicitly_wait(3)

    lyrics_search_link = ""

    # 검색방식 : 구글 검색 -> 가사 검색결과
    baseURL = "https://www.google.com/search"
    siteOption = "site:http://boom4u.net/lyrics/"

    # 검색조건 설정
    values = {
         'q': keyword + " " + siteOption,
        'oq': keyword,
         'aqs': 'chrome..69i57.35694j0j7',
            'sourceid': 'chrome',
            'ie': 'UTF-8',
         }
    
    # URL형식으로 변환
    query_string = urllib.parse.urlencode(values)

    try:
        req = web.get(baseURL + '?' + query_string)
        print("구글 검색 URL \t:\n", baseURL + '?' + query_string)
        print()
        soup = BeautifulSoup(web.page_source, 'html.parser')
        search_result = soup.select_one(".r > a")
    except:
        print("songParser Error!! ================================")
        traceback.print_exc()

    # for g in soup.find_all(class_='g'):
    #     print(g.text)
    #     print('-----')
    try:
        lyrics_search_link = search_result.get('href')
        song_name = search_result.getText().split()[0]
        print("노래 제목 \t: " + song_name)
        print("추출한 주소 \t:\n" + lyrics_search_link)
        print()
        if song_name not in keyword:
            print("검색결과가 일치하지 않습니다.")
            return "검색결과가 일치하지 않습니다."
    except:
        print("페이지를 찾지 못했습니다.")
        return "페이지를 찾지 못했습니다."
    web.get(lyrics_search_link)
    soup = BeautifulSoup(web.page_source, 'html.parser')

    # for s in soup.select('table.tabletext > tbody > tr'):
    #     print(s.getText())
    tag_string = []
    for s in soup.select('table.tabletext > tbody > tr'):
        tag_string.append(s.getText())
    return {song_name:'\n'.join(tag_string)}

def save_data(keyword):
    for t, l in getData(keyword).items():
        lyrics(name=t, lyrics=l).save()


if __name__ == '__main__':
    for t, l in getData("엔플라잉 옥탑방").items():
        print(t)
        print(l)
        lyrics(name=t, lyrics=l).save()

