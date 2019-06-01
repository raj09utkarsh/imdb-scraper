import requests
from bs4 import BeautifulSoup


def findLink(url):
	page = requests.get(url)
	soup = BeautifulSoup(page.content, 'html.parser')

	season_and_years   = soup.find("div", class_ = "seasons-and-year-nav")
	last_year_shown    = list(list(season_and_years.children)[9])[1]
	link_              = last_year_shown.get('href')
	current_year_shown = last_year_shown.get_text()
	link_              = "https://www.imdb.com" + link_
	return link_