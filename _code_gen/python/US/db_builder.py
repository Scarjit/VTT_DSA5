from US.Classes.RulePage import RulePage
from US.Classes.Page import Page

entry_points = [
    "https://ulisses-regelwiki.de/index.php/regeln.html",
    "https://ulisses-regelwiki.de/index.php/spezies.html",
    "https://ulisses-regelwiki.de/index.php/kulturen.html",
    "https://ulisses-regelwiki.de/index.php/professionen.html",
    "https://ulisses-regelwiki.de/index.php/sonderfertigkeiten.html",
    "https://ulisses-regelwiki.de/index.php/vor-und-nachteile.html",
    "https://ulisses-regelwiki.de/index.php/magie.html",
    "https://ulisses-regelwiki.de/index.php/goetterwirken.html",
    "https://ulisses-regelwiki.de/index.php/ruestkammer.html",
    "https://ulisses-regelwiki.de/index.php/bestiarium.html",
    "https://ulisses-regelwiki.de/index.php/herbarium.html",
    "https://ulisses-regelwiki.de/index.php/GifteundKrankheiten.html",
    "https://ulisses-regelwiki.de/index.php/WdV18.html",
]


def build_cache(ep: Page):
    for links in ep.links:
        print("Scanning: {}".format(links))
        page = Page(links)
        build_cache(page)


if __name__ == "__main__":
    for entry_point_url in entry_points:
        entry_page = Page(entry_point_url)
        build_cache(entry_page)
