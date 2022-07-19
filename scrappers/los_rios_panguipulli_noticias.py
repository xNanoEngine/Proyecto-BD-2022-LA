from random import choice
from utils import USER_AGENT_LIST

from requests_html import HTMLSession
import w3lib.html
import html
from datetime import datetime
from locale import setlocale
from locale import LC_TIME

URL_SEED_LIST = "https://panguipullinoticias.cl/home/"

session = HTMLSession()
headers = {'user-agent': choice(USER_AGENT_LIST)}

response = session.get(URL_SEED_LIST, headers=headers)

xpath_url = "//div[2]/div/h4/a/@href"
xpath_title = "//div[2]/h3/text()"
xpath_date = "//*[@id='content']/div/div[2]/div[1]/a/text()"
xpath_text = "///*[@id='content']/div/div[2]/p/text()"

urls = response.html.xpath(xpath_url)

news = []

def red_de_los_rios():
	for url in urls:
		# se obtienen la pagina de noticia
		article_url = url

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
			
		# se formatea la fecha
		setlocale(LC_TIME, 'es_CL.UTF-8') # se configura locale
		date = datetime.strptime(date, "\r\n\t\t\t\t\t%d %B %Y\t\t\t\t") # se obtiene el objeto datetime
		date = date.strftime("%Y-%m-%d") # se fomatea a 'YYYY-MM-DD'

		information = {"url": article_url, "date": date, "title": title, "text": text}
		news.append(information)
	return news

if  __name__ == "__main__":
	news = red_de_los_rios()
	#for i in news:
	#	print(i['title'])
	print(len(news))
	print(news[0])
