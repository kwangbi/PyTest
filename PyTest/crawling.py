# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import time



while True:
    res = requests.get('http://www.naver.com')
    assert res.status_code is 200
    
    dom = BeautifulSoup(res.content,"html.parser")
    #print(dom)
    
    ranking_elements = dom.select("li.ah_item")
    #print(ranking_elements)
    
    for i, ranking_element in enumerate(ranking_elements):
        i = i+1
        ranking_title_element = ranking_element.select(".ah_k")[0]
        #print(i+1,"위 : ", ranking_title_element.text)
        #print(ranking_title_element.text)
        print "[%d] : %s" %(i,ranking_title_element.text)

    print("-" * 30)
    print("refresh.....1 min")
    print("-" * 30)
    time.sleep(60)
    