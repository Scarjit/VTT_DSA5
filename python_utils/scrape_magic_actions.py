from bs4 import BeautifulSoup
import urllib3
http_pool = urllib3.PoolManager()

url_list = [
	"https://ulisses-regelwiki.de/index.php/AK_Blut_trinken.html",
]

for url in url_list:
    r = http_pool.request('GET', url)
    if r.status != 200:
        print("Couldn't get html file {}".format(url))
        continue  
    else:
        soup = BeautifulSoup(r.data)
        div = soup.findAll("div", {"class": "ce_text"})[0]
        name = div.findAll("h1")[0].text
        print(name)
