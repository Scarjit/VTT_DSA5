try:
    from US.Classes.Page import Page
except ImportError:
    from .Page import Page
"""
TODO: Implement me :)
"""


class LinkPage(Page):
    def __init__(self, page: Page):
        self.url = page.url
        self.soup = page.soup
        self.links = page.links
        self.sub_pages = page.sub_pages
        self.path = page.path
        self.data = page.data
        print("New LinkPage: {}".format(self.url))