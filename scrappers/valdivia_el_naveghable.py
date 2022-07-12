from random import choice
from utils import USER_AGENT_LIST, format_date
import numpy as np

from requests_html import HTMLSession
import w3lib.html
import html

URL_SEED_LIST = "https://www.elnaveghable.cl/"

session = HTMLSession()
headers = {'user-agent': choice(USER_AGENT_LIST)}

response = session.get(URL_SEED_LIST, headers=headers)

xpath_url_1 = "//h4/a/@href"
xpath_url_2 = "//h3/a/@href"
xpath_title = "//div//h1/text()"
xpath_date = "//div[@class='date-created-node']//span//text()"
xpath_text="//div[@class='content content-node']//p//text()"

urls = response.html.xpath(xpath_url_1)
urls_2 = response.html.xpath(xpath_url_2)

urls.extend(urls_2)

news = []

def el_navegable():
	for url in urls:
		# se obtienen la pagina de noticia
		article_url = URL_SEED_LIST + url

		# ingresa en cada noticia
		response = session.get(article_url, headers=headers)
	
		# obtiene los datos de cada noticia
		title = response.html.xpath(xpath_title)[0]
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
	news = el_navegable()
	#for i in news:
	#	print(i['title'])
	print(news[0])