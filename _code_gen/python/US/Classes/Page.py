from US.Helpers import *


class Page:
    def __init__(self, url):
        self.url = url
        self.data = CachedGetRequest(url)
        self.soup = BeautifulSoup(self.data, features="html.parser")
        self.path = GetPathFromSoup(self.soup)
        self.links = GetDeepLinks(self.soup)
        self.is_rule_page = IsRulePage(self.soup)

    def __str__(self):
        xstr = [
            "================",
            "URL:\t{}".format(self.url),
            "Path:\t{}".format(self.path),
            "Links:\t{}".format(self.links),
            "Is Rulepage:\t{}".format(self.is_rule_page)
        ]
        return '\n'.join(xstr)