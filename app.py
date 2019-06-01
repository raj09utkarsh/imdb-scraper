import requests
from bs4 import BeautifulSoup
import unicodedata
import titleFinder
import linkFinder


series_name   = input("TV Series: ").split(', ')
query = []
display_message = ''


for item in series_name:
	query_string = "https://www.imdb.com/find?ref_=nv_sr_fn&q=" + item.replace(' ', '+') + "&s=all"
	query.append(query_string)


title = titleFinder.titles(query)


query_page = []
for item in title:
	query_page.append("https://www.imdb.com/title/" + item + "/?ref_=fn_al_tt_1")



for url in query_page:
	i = query_page.index(url)
	series_name_to_be_displayed = series_name[i]

	link_               = linkFinder.findLink(url)

	page                = requests.get(link_)
	soup                = BeautifulSoup(page.content, 'html.parser')

	subpage_title_block = soup.find("div", class_ = "subpage_title_block")

	parent              = subpage_title_block.find("div", class_ = "parent")

	h3_                 = list(parent.find("h3").children)[3].get_text().strip()

	duration_           = h3_.split('(')[1].split(')')[0].strip()


	aa = duration_[len(duration_) - 1]


	if unicodedata.name(aa) == "EN DASH":
		all_episode_list = soup.find("div", class_ = "list detail eplist")

		flag = 0
		for episode in list(all_episode_list.children):
			title_ = episode.find("strong")
			
			if title_ != -1:
				title_name = list(title_.children)[0].get_text()
				if title_name.startswith("Episode"):
					airdate_ = episode.find("div", class_="airdate").get_text().strip()
					display_message += f'{series_name_to_be_displayed.upper()}: This TV series is currently running and next episode will be aired: {airdate_} \n'
					flag = 1
			if flag == 1:
				break
	else:
		all_episode_list = soup.find("div", class_ = "list detail eplist")
		episodes_        = list(all_episode_list.children)
		last_aired_date  =  episodes_[len(episodes_)-2].find("div", class_="airdate").get_text().strip()
		display_message += f"{series_name_to_be_displayed.upper()}: This TV series has ended airing and it was last aired on {last_aired_date} \n"


print(display_message)
