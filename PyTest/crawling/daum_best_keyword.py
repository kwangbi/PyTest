# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import time


while True:

    res = requests.get('http://www.daum.net')
    assert res.status_code is 200
    
    dom = BeautifulSoup(res.content,"html.parser")
    #print(dom)
        
    ranking_elements = dom.select("div.roll_txt")
    #print(ranking_elements)
    
    for i, ranking_element in enumerate(ranking_elements):
        i = i+1
        ranking_title_element = ranking_element.select(".link_issue")[0]
        #print(ranking_title_element.text)
        print "[%d] : %s" %(i,ranking_title_element.text)
        
        if i==10:
            break
        
    print("-" * 30)
    print("refresh.....1 min")
    print("-" * 30)
    time.sleep(60)
    