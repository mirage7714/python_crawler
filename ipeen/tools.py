# coding: utf-8

import requests
import shutil
from bs4 import BeautifulSoup as soup
import random
from predict_phone_nubmer import CheckNumber

main_url = 'http://www.ipeen.com.tw' 

"""
1.	Create page list
2.	Download store list on that page
3.	Download phone photo and rename the photo
4.	

"""

def GetAgent():
	agent_list = []
	with open('useragent_list.txt','r+') as f:
		agents = f.readlines()
		for agent in agents:
			agent_list.append(agent.replace('\n',''))
	index = int(random.random()* len(agent_list))
	headers = {'User-Agent':agent_list[index]}
	return headers
	
def GetLastPage(html):
	pages = soup(html.text, 'lxml')
	last_page = str(pages.find_all('a',{'data-label':'最尾頁'})).split('"')[9].split('=')[1]
	return int(last_page)

def GetPhoneNum(url):
    page_conts = requests.get(url, headers = GetAgent())
    details = soup(page_conts.text, 'lxml')
    phones = details.find_all('a',{'data-action':'up_phone'})
    p = ''
    if(len(phones) > 0):
        phone = phones[0].attrs
        p = phone['href'].split(':')[1].replace('-','').replace('(','').replace(')','').replace(' ','')
    return p

def DownloadImg(url, loc):
	response = requests.get(url, stream = True)
	if (response.status_code == 200):
		with open(loc, 'wb') as f:
			shutil.copyfileobj(response.raw, f)
			del response
	
def GetAddr(article):
	addr = str(article.find_all('span',{'style':'padding-left:3em;'})).split('>')[1].split('\n')[0]
	return addr

def GetNameAndLink(article):
	info = {}
	parts = article.find_all('a',{'data-label':"店名"})[0].attrs
	name = article.find_all('a',{'data-label':"店名"})[0].text
	link = main_url+parts['href']
	info['name'] = name
	info['link'] = link
	return info

def GetImgUrl(article):
	tels = article.find_all('img',{'alt':'電話號碼'})
	info = GetNameAndLink(article)
	if(len(tels) > 0 ) :
		tel = tels[0].attrs
		tel_url = main_url+tel['src']
		#name = GetPhoneNum(info['link'])+'.png'
		if(len(tel_url) >0):
			DownloadImg(tel_url, 'web_content/temp.png')
			phone = CheckNumber()
			info['phone'] = phone
	return info
		
	
def GetCategory(article):
	categories = {}
	category1 = str(article.find_all('a',{'data-label':'大分類'})).split('"')[10].split('>')[1].split('<')[0]
	category2 = str(article.find_all('a',{'data-label':'小分類'})).split('"')[10].split('>')[1].split('<')[0]
	categories['category1'] = category1
	categories['category2'] = category2
	return categories

def CreatePages(pages):
	page_url = 'http://www.ipeen.com.tw/search/taiwan/000/0-100-0-0/?p='
	all_pages = []
	for num in range(1, int(pages)):
		url = page_url+str(num)
		all_pages.append(url)
	return all_pages
