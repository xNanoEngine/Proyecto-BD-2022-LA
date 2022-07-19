from random import choice
from utils import USER_AGENT_LIST

from requests_html import HTMLSession
import w3lib.html
import html
from datetime import datetime
from locale import setlocale
from locale import LC_TIME

URL_SEED_LIST = "https://redlosrios.com/"

session = HTMLSession()
headers = {'user-agent': choice(USER_AGENT_LIST)}

response = session.get(URL_SEED_LIST, headers=headers)

xpath_url_1 = "//article//h1/a/@href"
xpath_url_2 = "//article//h2/a/@href"
xpath_url_3 = "//article//h3/a/@href"

xpath_title = "//div//h1/text()"
xpath_date = "//ul//li[@class='main_fecha']//text()"
#xpath_hour = "//ul//li[@class='main_hora']//text()"
xpath_text="//div[@class='CUERPO']//p//text()"

urls = response.html.xpath(xpath_url_1)
urls_2 = response.html.xpath(xpath_url_2)
urls_3 = response.html.xpath(xpath_url_3)

urls.extend(urls_2)
urls.extend(urls_3)

news = []

def red_de_los_rios():
	for url in urls:
		# se obtienen la pagina de noticia
		article_url = URL_SEED_LIST + url[1:]
	
		# ingresa en cada noticia
		response = session.get(article_url, headers=headers)
	
		# obtiene los datos de cada noticia
		title = response.html.xpath(xpath_title)[0]
		date = response.html.xpath(xpath_date)[0]
		#hour = response.html.xpath(xpath_hour)[0]
	
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
		date = datetime.strptime(date, "%A %d de %B de %Y") # se obtiene el objeto datetime
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
