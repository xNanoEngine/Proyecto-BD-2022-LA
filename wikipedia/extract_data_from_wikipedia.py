from random import choice
from requests_html import HTMLSession
import w3lib.html
import html

from datetime import datetime
from datetime import timedelta

## Simular que estamos utilizando un navegador web
USER_AGENT_LIST = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
]

def data_from_wikipedia(name, lastname):

	URL_SEED = "https://es.wikipedia.org/wiki/" + name + "_" + lastname
	session = HTMLSession()
	headers = {'user-agent': choice(USER_AGENT_LIST)}
	response = session.get(URL_SEED, headers=headers)
	
	today = datetime.now()
	today = today.strftime("%Y%m%d")
	yesterday = today - timedelta(days=1)
	yesterdar = yesterday.strftime("%Y%m%d")

	URL_SEED_PAGEVIEWS = "https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/es.wikipedia/all-access/all-agents/" + name + "_" + "lastname" + "/daily/" + yesterday "/" + today
	response_2 = session.get(URL_SEED_PAGEVIEWS, headers=headers)

	xpath_profession_1 = "//td[@class='role']/a/text()"
	xpath_profession_2 = "//td[@class='role']/text()"
	xpath_date_of_birth_1 = "//td/text()"
	xpath_date_of_birth_2 = "//td/a/text()"
	
	profession_1 = response.html.xpath(xpath_profession_1)
	profession_2 = response.html.xpath(xpath_profession_2)
	#birth_1 = response.html.xpath(xpath_date_of_birth_1)
	#birth_2 = response.html.xpath(xpath_date_of_birth_2)
	
	profession_1.extend(profession_2)
	#birth_1.extend(birth_2)
	
	print(profession_1)
	#print(birth_1)


if  __name__ == "__main__":
	data = data_from_wikipedia("Gabriel", "Boric")
	data = data_from_wikipedia("Sebastián", "Piñera")
	#print(data)


	