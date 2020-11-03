import threading
try:
    from US.Classes.Page import Page
except ImportError:
    from Classes.Page import Page

_ENTRY_POINTS = [
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


def build_cache(ep: Page, use_threadding: bool):
    if use_threadding:
        thrds = []
        for links in ep.links:
            page = Page(links)
            tx = threading.Thread(target=build_cache, args=(page, use_threadding,), daemon=True)
            thrds.append(tx)
            tx.start()
        for tx in thrds:
            tx.join()
    else:
        for links in ep.links:
            page = Page(links)
            build_cache(page, use_threadding)


def build_cache_from_eps():
    threads = []
    for entry_point_url in _ENTRY_POINTS:
        entry_page = Page(entry_point_url)
        t = threading.Thread(target=build_cache, args=(entry_page, False,), daemon=True)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

def parse_eps():

    for entry_point_url in _ENTRY_POINTS:
        entry_page = Page(entry_point_url)

if __name__ == "__main__":
    parse_eps()
