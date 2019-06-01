import requests
from bs4 import BeautifulSoup

def titles(query):
	title = []
	for item in query:
		page = requests.get(item)
		soup = BeautifulSoup(page.content, 'html.parser')

		findList = soup.find("table", class_ = "findList")
		
		result_  = list(list(list(findList.children)[1].children)[3].children)[1]

		href_    = result_.get('href').split('/')
		title.append(href_[2])
	return title