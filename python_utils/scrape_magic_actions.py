from bs4 import BeautifulSoup
import urllib3
import json
http_pool = urllib3.PoolManager()

magic_actions = {
    "animist_forces" : [
        "https://ulisses-regelwiki.de/index.php/AK_Blut_trinken.html",
        "https://ulisses-regelwiki.de/index.php/AK_Durch_feste_Materie.html",
        "https://ulisses-regelwiki.de/index.php/AK_Gro%C3%9Fer_Sprung.html",
        "https://ulisses-regelwiki.de/index.php/AK_Harte_Haut.html",
        "https://ulisses-regelwiki.de/index.php/AK_Immunitaet_gegen_Hitze.html",
        "https://ulisses-regelwiki.de/index.php/AK_Immunitaet_gegen_Kaelte.html",
        "https://ulisses-regelwiki.de/index.php/AK_Kampffaehigkeiten_verbessern.html",
        "https://ulisses-regelwiki.de/index.php/AK_Patronruf.html",
    ],
    "distorted_fairy_songs": [
        "https://ulisses-regelwiki.de/index.php/kako.html",
        "https://ulisses-regelwiki.de/index.php/lieddesschmerz.html",
        "https://ulisses-regelwiki.de/index.php/sturmlied.html",
        "https://ulisses-regelwiki.de/index.php/Sklavenlied.html",
        "https://ulisses-regelwiki.de/index.php/Schlachtlied.html",
    ],
    "fairy_songs": [
        "https://ulisses-regelwiki.de/index.php/ESF_Erinnerungsmelodie.html",
        "https://ulisses-regelwiki.de/index.php/ESF_Freundschaftslied.html",
        "https://ulisses-regelwiki.de/index.php/ESF_Friedenslied.html",
        "https://ulisses-regelwiki.de/index.php/ESF_AbwehrDaemonisch.html",
        "https://ulisses-regelwiki.de/index.php/ESF_Erholung.html",
        "https://ulisses-regelwiki.de/index.php/ESF_Klarheit.html",
        "https://ulisses-regelwiki.de/index.php/ESF_Lieder.html",
        "https://ulisses-regelwiki.de/index.php/ESF_Lied_der_Pflanzen.html",
        "https://ulisses-regelwiki.de/index.php/ESF_Reinheit.html",
        "https://ulisses-regelwiki.de/index.php/ESF_Tierwahrnehmung.html",
        "https://ulisses-regelwiki.de/index.php/ESF_Heilschlafs.html",
        "https://ulisses-regelwiki.de/index.php/ESF_Trostes.html",
        "https://ulisses-regelwiki.de/index.php/ESF_Windgefluesters.html",
        "https://ulisses-regelwiki.de/index.php/ESF_Zauberschutzes.html",
        "https://ulisses-regelwiki.de/index.php/ESF_MelodiederKunstfertigkeit.html",
        "https://ulisses-regelwiki.de/index.php/ESF_Sorgenlied.html",
        "https://ulisses-regelwiki.de/index.php/ESF_Zaubermelodie.html",
    ],
    "geod_rituals": [
        "https://ulisses-regelwiki.de/index.php/grit_Gestalt_aus_Rauch.html",
        "https://ulisses-regelwiki.de/index.php/grit_Trank_des_ungehinderten_Weges.html",
    ],
    "magic_dance": [
        "https://ulisses-regelwiki.de/index.php/ZT_TanzderAngriffslust.html",
        "https://ulisses-regelwiki.de/index.php/ZT_TanzderBeweglichkeit.html",
        "https://ulisses-regelwiki.de/index.php/ZT_tanzderBilder.html",
        "https://ulisses-regelwiki.de/index.php/ZT_TanzderErloesung.html",
        "https://ulisses-regelwiki.de/index.php/ZT_TanzderErmutigung.html",
        "https://ulisses-regelwiki.de/index.php/ZT_TanzderHeilung.html",
        "https://ulisses-regelwiki.de/index.php/ZT_TanzderLibe.html",
        "https://ulisses-regelwiki.de/index.php/ZT_TanzderLinderung.html",
        "https://ulisses-regelwiki.de/index.php/ZT_TanzderTraeume.html",
        "https://ulisses-regelwiki.de/index.php/ZT_TanzderTäuschung.html",
        "https://ulisses-regelwiki.de/index.php/ZT_TanzderUnantastbarkeit.html",
        "https://ulisses-regelwiki.de/index.php/ZT_TanzderUnver.html",
        "https://ulisses-regelwiki.de/index.php/ZT_TanzderVert.html",
        "https://ulisses-regelwiki.de/index.php/ZT_TanzderVerwirrung.html",
        "https://ulisses-regelwiki.de/index.php/ZT_TanzderWacht.html",
        "https://ulisses-regelwiki.de/index.php/ZT_TanzderWahrheit.html",
        "https://ulisses-regelwiki.de/index.php/ZT_TanzderWeisheit.html",
        "https://ulisses-regelwiki.de/index.php/ZT_TanzdermagischenGemeinschaft.html",
        "https://ulisses-regelwiki.de/index.php/ZT_TanzdesBeg.html",
        "https://ulisses-regelwiki.de/index.php/ZT_Blut.html",
        "https://ulisses-regelwiki.de/index.php/ZT_Feuer.html",
        "https://ulisses-regelwiki.de/index.php/ZT_Handels.html",
        "https://ulisses-regelwiki.de/index.php/ZTGlueck.html",
        "https://ulisses-regelwiki.de/index.php/ZT_Pech.html",
        "https://ulisses-regelwiki.de/index.php/ZT_Ungeh.html",
        "https://ulisses-regelwiki.de/index.php/ZTohenEnde.html"
    ],
    "magic_melodies": [
        "https://ulisses-regelwiki.de/index.php/ZM_Melodie_der_Angriffslust.html",
        "https://ulisses-regelwiki.de/index.php/ZM_Melodie_der_Erloesung.html",
        "https://ulisses-regelwiki.de/index.php/ZM_Melodie_der_Ermutigung.html",
        "https://ulisses-regelwiki.de/index.php/ZM_Melodie_der_Feen.html",
        "https://ulisses-regelwiki.de/index.php/ZM_Melodie_der_Flammen.html",
        "https://ulisses-regelwiki.de/index.php/ZM_Melodie_der_Freundschaft.html",
        "https://ulisses-regelwiki.de/index.php/ZM_Melodie_der_Geschwindigkeit.html",
        "https://ulisses-regelwiki.de/index.php/ZM_Melodie_der_Heilung.html",
        "https://ulisses-regelwiki.de/index.php/ZM_Melodie_der_Taeuschung.html",
        "https://ulisses-regelwiki.de/index.php/ZM_Melodie_der_Versoehnung.html",
        "https://ulisses-regelwiki.de/index.php/ZM_Melodie_der_Verwirrung.html",
        "https://ulisses-regelwiki.de/index.php/ZM_Melodie_der_Weisheit.html",
        "https://ulisses-regelwiki.de/index.php/ZM_Melodie_der_Wueste.html",
        "https://ulisses-regelwiki.de/index.php/ZM_Melodie_der_Zaehigkeit.html",
        "https://ulisses-regelwiki.de/index.php/ZM_Melodie_des_Bebens.html",
        "https://ulisses-regelwiki.de/index.php/ZM_Melodie_des_Einlullens.html",
        "https://ulisses-regelwiki.de/index.php/ZM_Melodie_des_Handels.html",
        "https://ulisses-regelwiki.de/index.php/ZM_Melodie_des_Kampfes.html",
        "https://ulisses-regelwiki.de/index.php/ZM_Melodie_des_Magieschadens.html",
        "https://ulisses-regelwiki.de/index.php/ZM_Melodie_des_Meeres.html",
        "https://ulisses-regelwiki.de/index.php/ZM_Melodie_des_Rausches.html",
        "https://ulisses-regelwiki.de/index.php/ZM_Melodie_des_Windes.html",
        "https://ulisses-regelwiki.de/index.php/ZM_Melodie_des_Zauberschutzes.html",
        "https://ulisses-regelwiki.de/index.php/ZM_Melodie_des_Zoegerns.html"
    ],
    "prankster_pranks": [
        "https://ulisses-regelwiki.de/index.php/SST_Aufgeblasen.html",
        "https://ulisses-regelwiki.de/index.php/SST_DichterDenker.html",
        "https://ulisses-regelwiki.de/index.php/SST_Holterdipolter.html",
        "https://ulisses-regelwiki.de/index.php/SST_Juckpulver.html",
        "https://ulisses-regelwiki.de/index.php/SST_Koboldgeschenk.html",
        "https://ulisses-regelwiki.de/index.php/SST_Lachgesund.html",
        "https://ulisses-regelwiki.de/index.php/SST_Lachkrampf.html",
        "https://ulisses-regelwiki.de/index.php/SST_Lulatsch.html",
        "https://ulisses-regelwiki.de/index.php/SST_Meister.html",
        "https://ulisses-regelwiki.de/index.php/SST_MurksPatz.html",
        "https://ulisses-regelwiki.de/index.php/SST_Nackedei.html",
        "https://ulisses-regelwiki.de/index.php/SST_Papperlapapp.html",
        "https://ulisses-regelwiki.de/index.php/SST_Schelmenkleister.html",
        "https://ulisses-regelwiki.de/index.php/SST_Schelmenlaune.html",
        "https://ulisses-regelwiki.de/index.php/SST_Schelmenmaske.html",
        "https://ulisses-regelwiki.de/index.php/SST_Schelmenrausch.html",
        "https://ulisses-regelwiki.de/index.php/SST_Tauschrausch.html",
        "https://ulisses-regelwiki.de/index.php/SST_Verschwindibus.html",
        "https://ulisses-regelwiki.de/index.php/SST_ZagibuUbigaz.html",
    ],
    "rites_of_domination": [
        "https://ulisses-regelwiki.de/index.php/Ausbruchunterdr.html",
        "https://ulisses-regelwiki.de/index.php/FigurderSchmerzen.html",
        "https://ulisses-regelwiki.de/index.php/FluchderPestilenz.html",
        "https://ulisses-regelwiki.de/index.php/FluchderSchlaflosigkeit.html",
        "https://ulisses-regelwiki.de/index.php/Herrschaft_Kristall_der_Herrschaft.html",
        "https://ulisses-regelwiki.de/index.php/MachtueberSchlafwandler.html",
        "https://ulisses-regelwiki.de/index.php/MH_WurzelDesBlutes.html",
    ],
    "witch_curses": [
        "https://ulisses-regelwiki.de/index.php/HSF_BeißaufGranit.html",
        "https://ulisses-regelwiki.de/index.php/HSF_Beute.html",
        "https://ulisses-regelwiki.de/index.php/fluch_Fellwechsel.html",
        "https://ulisses-regelwiki.de/index.php/HSF_Geschmackssinn.html",
        "https://ulisses-regelwiki.de/index.php/HSF_Gestankanheften.html",
        "https://ulisses-regelwiki.de/index.php/HSF_Hagelschlag.html",
        "https://ulisses-regelwiki.de/index.php/HSF_Hexenschuss.html",
        "https://ulisses-regelwiki.de/index.php/HSF_Hungerwecken.html",
        "https://ulisses-regelwiki.de/index.php/HSF_Juckreizverursachen.html",
        "https://ulisses-regelwiki.de/index.php/HSF_Kornfaeule.html",
        "https://ulisses-regelwiki.de/index.php/HDF_Kroetenkuss.html",
        "https://ulisses-regelwiki.de/index.php/HSF_MieseLaune.html",
        "https://ulisses-regelwiki.de/index.php/HSF_Blindheit.html",
        "https://ulisses-regelwiki.de/index.php/HSF_PechandenHalswuenschen.html",
        "https://ulisses-regelwiki.de/index.php/HSF_Pestilenz.html",
        "https://ulisses-regelwiki.de/index.php/HSF_Schlafrauben.html",
        "https://ulisses-regelwiki.de/index.php/HSF_Todesfluch.html",
        "https://ulisses-regelwiki.de/index.php/1178.html",
        "https://ulisses-regelwiki.de/index.php/HSF_Viehverstuemmelung.html",
        "https://ulisses-regelwiki.de/index.php/HSF_Warzensprießen.html",
        "https://ulisses-regelwiki.de/index.php/HSF_Wollustverursachen.html",
        "https://ulisses-regelwiki.de/index.php/HSF_Zungelaehmen.html",
        "https://ulisses-regelwiki.de/index.php/HSF_ZweilinkeHaende.html",
        "https://ulisses-regelwiki.de/index.php/HSF_AengsteMehren.html",
    ],
    "zibilija_rituals": [
        "https://ulisses-regelwiki.de/index.php/zr_Band_zur_Ware.html",
        "https://ulisses-regelwiki.de/index.php/zr_Bienenfleiß.html",
        "https://ulisses-regelwiki.de/index.php/zs_Bienenkoenigin.html",
        "https://ulisses-regelwiki.de/index.php/zr_Bienensuche.html",
        "https://ulisses-regelwiki.de/index.php/zs_Bienentanz.html",
        "https://ulisses-regelwiki.de/index.php/zs_Sicheres_Lager.html",
        "https://ulisses-regelwiki.de/index.php/zs_Siegel_des_Grabes.html",
        "https://ulisses-regelwiki.de/index.php/zr_Traumerinnerung.html",
        "https://ulisses-regelwiki.de/index.php/zs_Traumseherin.html",
        "https://ulisses-regelwiki.de/index.php/zs_Unglücksgefaeß.html",
        "https://ulisses-regelwiki.de/index.php/zs_Wachshaut.html",
        "https://ulisses-regelwiki.de/index.php/zs_Wachskonservierung.html",
        "https://ulisses-regelwiki.de/index.php/zs_Wachsmumie.html",
        "https://ulisses-regelwiki.de/index.php/zs_Warenchronik.html",
        "https://ulisses-regelwiki.de/index.php/zs_Weisheit_der_Schrift.html",
    ]
}

for action in magic_actions:
    print(action)
    x_j_data = []
    for url in magic_actions[action]:
        r = http_pool.request('GET', url)
        if r.status != 200:
            print("Couldn't get html file {}".format(url))
            continue  
        else:
            soup = BeautifulSoup(r.data, features="html.parser")
            div = soup.findAll("div", {"class": "ce_text"})[0]
            publication_block = soup.findAll("div", {"class": "ce_text"})[1].findAll("p")[0].text.replace("Publikationen:", "")
            name = div.findAll("h1")[0].text
            texts = div.findAll("p")

            json_data = {
                "_id": "",
                "publication": publication_block
            }

            for i,t in enumerate(texts):
                xtext = t.text
                xtext_splits = xtext.split(':', 1)
                if len(xtext_splits) != 2:
                    json_data["annotation"] = xtext_splits[0]
                    continue
                a = xtext_splits[0]
                b = xtext_splits[1]
                if a == "Probe":
                    p_splits = b.strip().split("/")
                    json_data["test"] = {}
                    for i,p in enumerate(p_splits):
                        json_data["test"][i] = p.strip()
                elif a == "Wirkung":
                    json_data["effect"] = b.strip()
                elif a == "AsP-Kosten":
                    json_data["asp_cost"] = b.strip()
                elif a == "Wirkungsdauer":
                    json_data["effective_period"] = b.strip()
                elif a == "Merkmal":
                    json_data["feature"] = b.strip()
                elif a == "Talent":
                    json_data["talent"] = b.strip()
                elif a == "Publikation":
                    json_data["publication"] = b.strip()
                elif a == "Stammestradition":
                    b_splits = b.replace(" ", "").split(",")
                    json_data["tribal_tradition"] = {}
                    for i,p in enumerate(b_splits):
                        json_data["tribal_tradition"][i] = p.strip()
                elif a == "Steigerungsfaktor":
                    json_data["growth_factor"] = b.strip()
                elif a == "Zauberdauer":
                    json_data["cast_time"] = b.strip()
                elif a == "Reichweite":
                    json_data["range"] = b.strip()    
                elif a == "Zielkategorie":
                    json_data["target_category"] = b.strip()       
                elif a == "Dauer":
                    json_data["duration"] = b.strip()    
                elif a == "Ritualdauer":
                    json_data["ritual_duration"] = b.strip()        
                elif a == "Voraussetzungen":
                    json_data["requirements"] = b.strip()                 
                elif a == "Musiktradition":    
                    b_splits = b.replace(" ", "").split(",")
                    json_data["music_tradition"] = {}
                    for i,p in enumerate(b_splits):
                        json_data["music_tradition"][i] = p.strip()
                elif "QS" in a:
                    qs_x = a.split(" ")[1]
                    if not "QL" in json_data:
                        json_data["QL"] = {}
                    json_data["QL"][qs_x] = b.strip()
                elif "Stufe" in a:
                    qs_x = a.split(" ")[1]
                    if not "level" in json_data:
                        json_data["level"] = {}
                    json_data["level"][qs_x] = b.strip()
                else:
                    if not "fluff" in json_data:
                        json_data["fluff"] = ""
                    json_data["fluff"] += a
                    json_data["fluff"] += b
                    json_data["fluff"] += "\r\n"

                    print("No case found for: {}".format(a))
                    print(url)
                    print(b)


            x_j_data.append(json_data)


    with open('out\\{}.json'.format(action), 'w', encoding='utf-8') as f:
        json.dump(x_j_data, f, ensure_ascii=False, indent=4)