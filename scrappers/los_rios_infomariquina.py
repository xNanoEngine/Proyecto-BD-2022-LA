from random import choice
from utils import USER_AGENT_LIST, format_date
import numpy as np

from requests_html import HTMLSession
import w3lib.html
import html

URL_SEED_LIST = "https://infomariquina.cl/"

session = HTMLSession()
headers = {'user-agent': choice(USER_AGENT_LIST)}

response = session.get(URL_SEED_LIST, headers=headers)

xpath_url_1 = "//h2/a/@href"
xpath_url_2 = "//h4/a/@href"
xpath_url_3 = "//h5/a/@href"

xpath_title = "//h1//text()"
xpath_date = "//div//span[@class='date']//a//text()"
xpath_text="//div[@class='entry-content entry-dropcap']//p//text()"

urls = response.html.xpath(xpath_url_1)
urls_2 = response.html.xpath(xpath_url_2)
urls_3 = response.html.xpath(xpath_url_3)

urls.extend(urls_2)
urls.extend(urls_3)

news = []

def red_de_los_rios():
	for url in urls:
		# se obtienen la pagina de noticia
		article_url = url

		# ingresa en cada noticia
		response = session.get(article_url, headers=headers)
	
		# obtiene los datos de cada noticia
		title = response.html.xpath(xpath_title)
		if(title != []):
			title = title[0]
		else:
			title = ""
		
		date = response.html.xpath(xpath_date)[0]
	
		list_p = response.html.xpath(xpath_text)
	
		text=""
		for p in list_p:
			content = w3lib.html.remove_tags(p)
			content = w3lib.html.replace_escape_chars(content)
			content = html.unescape(content)
			content = content.strip()
			text = text + " " + content

		information = {"url": article_url, "date": format_date(date), "title": title, "text": text}
		news.append(information)
	return news

if  __name__ == "__main__":
	news = red_de_los_rios()
	#for i in news:
	#	print(i['title'])
	print(news[0])
