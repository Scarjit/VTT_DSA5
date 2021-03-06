from bs4 import BeautifulSoup
import urllib3
import json
import hashlib
import os

http_pool = urllib3.PoolManager()


class Page:
    def __init__(self, url):
        self.url = url
        self.path = []
        self.links = []
        self.data = None
        self.do_cached_get_request()
        self.soup = BeautifulSoup(self.data, features="html.parser")
        self.scan_path()
        self.scan_links()
        self.sub_pages = []
        self.parse_sub_pages()

    def scan_path(self):
        head_div = self.soup.findAll("div", {"class": "col-md-12"})[1].findAll("li")
        self.path = []
        for div in head_div[1:]:
            div_dict = div.attrs
            if (("class" in div_dict and "sep" not in div_dict['class'])
                    or "class" not in div_dict):
                self.path.append(div.text)

    def scan_links(self):
        a = self.soup.findAll("a", {"class": "ulSubMenu"}, recursive=True)
        self.links = []
        for ah in a:
            self.links.append("https://ulisses-regelwiki.de/{}".format(ah.attrs["href"]))

    def parse_sub_pages(self):
        try:
            from US.Classes import LinkPage
            from US.Classes import CombinedPage
            from US.Classes import RulePage
        except ImportError:
            from . import LinkPage
            from . import CombinedPage
            from . import RulePage
        for sub_page in self.links:
            sub = Page(sub_page)
            switcher = {
                "LinkPage": LinkPage.LinkPage,
                "CombinedPage": CombinedPage.CombinedPage,
                "RulePage": RulePage.RulePage,
            }
            sub_class = switcher.get(
                sub.get_page_type(),
                Exception(f"type not in dictionary", f"{sub.get_page_type()}")
            )
            if type(sub_class) == "str":
                raise Exception(sub_class)
            self.sub_pages.append(
                sub_class(sub)
            )

    def get_page_type(self) -> str:
        if len(self.soup.findAll("div", {"class": "mod_article"})) > 0:
            if len(self.soup.findAll("h1", {"class": "ulStrikeOutH1"})):
                return "CombinedPage"
            else:
                return "RulePage"
        else:
            return "LinkPage"

    def do_cached_get_request(self):
        s = hashlib.sha3_512()
        if type(self.url) != str:
            print("{} is not a str ({})".format(self.url, type(self.url)))
            exit()
        s.update(self.url.encode('utf-8'))
        filename = "cache\\{}.html".format(s.hexdigest())
        if os.path.isfile(filename):
            # print("{} from cache".format(self.url))
            with open(filename, 'r', encoding='utf-8') as f:
                data = f.read()
                self.data = data
        else:
            print("{} from web".format(self.url))
            r = http_pool.request('GET', self.url)
            if r.status != 200:
                print("Couldn't get url: {}".format(self.url))
                exit()
            cleaned = r.data.decode('utf-8', 'ignore')
            with open(filename, 'w', encoding='utf-8') as f:
                print("\t->{}".format(filename))
                f.write(cleaned)
            self.data = cleaned

    def __str__(self):
        xstr = [
            "================",
            "URL:\t{}".format(self.url),
            "Path:\t{}".format(self.path),
            "Links:\t{}".format(self.links),
        ]
        return '\n'.join(xstr)

    def to_json(self) -> str:
        return json.dumps({
            "url": self.url,
            "path": self.path,
            "links": self.links,
        })
