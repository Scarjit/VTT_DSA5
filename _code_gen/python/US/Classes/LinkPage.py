from US.Classes.Page import Page

"""
TODO: Implement me :)
"""


class LinkPage(Page):
    def __init__(self, page: Page):
        self.url = page.url
        self.contains_rules = page.contains_rules
        self.soup = page.soup
        self.links = page.links
        self.sub_pages = page.sub_pages
        self.path = page.path
        self.data = page.data