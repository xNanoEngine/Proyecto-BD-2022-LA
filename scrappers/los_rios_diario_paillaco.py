from random import choice
from utils import USER_AGENT_LIST

from requests_html import HTMLSession
import w3lib.html
import html
from datetime import datetime
from locale import setlocale
from locale import LC_TIME

URL_SEED_LIST = "https://www.diariopaillaco.cl/"

session = HTMLSession()
headers = {'user-agent': choice(USER_AGENT_LIST)}

response = session.get(URL_SEED_LIST, headers=headers)

xpath_url_1 = "/html/body/main/div[4]/div[1]/h2/a/@href"
xpath_url_2 = "/html/body/main/div[4]/div/div/div/div/a/@href"
xpath_url_3 = "//*[@id='body_center']/div/div/div/div/h4/a/@href"
xpath_url_4 = "//*[@id='body_center']/div/div/div/div/h5/a/@href"
xpath_url_5 = "//*[@id='body_center']/div/div/div/div/h6/a/@href"
xpath_url_6 = "//*[@id='body_right']/div/div/div/div/h6/a/@href"
xpath_url_7 = "//*[@id='body_right']/div/div[1]/div[3]/h5/a/@href"

xpath_title = "//h1/text()"
xpath_date = "//small/text()"
xpath_text = "//div[2]/p/text()"

urls = response.html.xpath(xpath_url_1)
urls_2 = response.html.xpath(xpath_url_2)
urls_3 = response.html.xpath(xpath_url_3)
urls_4 = response.html.xpath(xpath_url_4)
urls_5 = response.html.xpath(xpath_url_5)
urls_6 = response.html.xpath(xpath_url_6)
urls_7 = response.html.xpath(xpath_url_7)

urls.extend(urls_2)
urls.extend(urls_3)
urls.extend(urls_4)
urls.extend(urls_5)
urls.extend(urls_6)
urls.extend(urls_7)

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
		date = date.split(',')[1].split('|')[0]
		
		if(date[-1] == " "): # se obtiene el objeto datetime
			date = datetime.strptime(date, " %d de %B de %Y ")
		else:
			date = datetime.strptime(date, " %d de %B de %Y")
			
		date = date.strftime("%Y-%m-%d") # se fomatea a 'YYYY-MM-DD'

		information = {"url": article_url, "date": date, "title": title, "text": text[0:-11]}
		news.append(information)
	return news

if  __name__ == "__main__":
	news = red_de_los_rios()
	#for i in news:
	#	print(i['title'])
	print(len(news))
	print(news[0])
