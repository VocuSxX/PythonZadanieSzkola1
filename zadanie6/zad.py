import json
import re
from pathlib import Path

import pandas as pd
import scrapy
from scrapy.crawler import CrawlerProcess

FOLDER = Path(__file__).parent
CYTATY_JSON = FOLDER / "cytaty_scrapy.json"
PRODUKTY_JSON = FOLDER / "produkty.json"


def parsuj_cene(tekst):
    tekst = tekst.replace("\xa0", "").replace(" ", "")
    liczby = re.findall(r"\d+[.,]\d{2}", tekst)
    return float(liczby[0].replace(",", ".")) if liczby else None


def ustawienia_feed(sciezka):
    return {
        "FEEDS": {str(sciezka): {"format": "json", "encoding": "utf8", "indent": 2, "overwrite": True}},
        "FEED_EXPORT_ENCODING": "utf-8",
    }


class CytatySpider(scrapy.Spider):
    name = "cytaty"
    start_urls = ["http://quotes.toscrape.com/"]
    custom_settings = ustawienia_feed(CYTATY_JSON)

    def parse(self, response):
        for cytat in response.css("div.quote"):
            yield {
                "text": cytat.css("span.text::text").get(),
                "author": cytat.css("small.author::text").get(),
                "tags": cytat.css("div.tags a.tag::text").getall(),
            }
        nastepna = response.css("li.next a::attr(href)").get()
        if nastepna:
            yield response.follow(nastepna, callback=self.parse)


def tekst_ceny(element):
    teksty = element.xpath(".//ins//text()").getall() or element.xpath(".//text()").getall()
    return " ".join(teksty)


class ProduktySpider(scrapy.Spider):
    name = "produkty"
    start_urls = ["https://esklep.polsl.pl/kategoria-produktu/gadzety/"]
    handle_httpstatus_list = [403, 404, 429, 503]
    custom_settings = {**ustawienia_feed(PRODUKTY_JSON), "DOWNLOAD_DELAY": 0.5}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.widziane = set()

    def produkty_z_kontenerow(self, response):
        for produkt in response.css("li.product, div.product"):
            nazwa = (produkt.css(".woocommerce-loop-product__title::text").get()
                     or produkt.css("h2 a::text, h3 a::text, h4 a::text").get())
            ceny = produkt.css(".price")
            yield {
                "nazwa": nazwa.strip() if nazwa else None,
                "cena": parsuj_cene(tekst_ceny(ceny[0])) if ceny else None,
                "url": produkt.css("a::attr(href)").get(),
            }

    def produkty_z_naglowkow(self, response):
        for h in response.xpath("//*[self::h2 or self::h3 or self::h4][a[contains(@href, '/produkt/')]]"):
            ceny = h.xpath("(following::*[contains(@class, 'price')])[1]")
            yield {
                "nazwa": h.xpath("normalize-space(.)").get(),
                "cena": parsuj_cene(tekst_ceny(ceny[0])) if ceny else None,
                "url": h.xpath("./a/@href").get(),
            }

    def zapisz_debug(self, response):
        sciezka = FOLDER / "debug_produkty.html"
        sciezka.write_text(response.text, encoding="utf-8")
        self.logger.error("Nie znaleziono produktów na %s (status %s). Zapisano stronę do %s",
                          response.url, response.status, sciezka)

    def parse(self, response):
        if response.status != 200:
            self.zapisz_debug(response)
            return
        znalezione = list(self.produkty_z_kontenerow(response)) or list(self.produkty_z_naglowkow(response))
        if not znalezione:
            self.zapisz_debug(response)
        for produkt in znalezione:
            if produkt["url"] in self.widziane:
                continue
            self.widziane.add(produkt["url"])
            yield produkt
        nastepna = (response.css("a.next::attr(href)").get()
                    or response.xpath('//a[normalize-space(text())="→"]/@href').get())
        if nastepna:
            yield response.follow(nastepna, callback=self.parse)


def uruchom_pajaki():
    proces = CrawlerProcess(settings={
        "USER_AGENT": "Mozilla/5.0 (zadanie scrapy – nauka)",
        "LOG_LEVEL": "WARNING",
    })
    proces.crawl(CytatySpider)
    proces.crawl(ProduktySpider)
    proces.start()


def wczytaj_json(sciezka):
    with open(sciezka, encoding="utf-8") as f:
        return json.load(f)


def analiza_produktow(df):
    df = df.dropna(subset=["cena"])
    srednia = df["cena"].mean()
    najdrozsze = df[df["cena"] == df["cena"].max()]
    najtansze = df[df["cena"] == df["cena"].min()]
    odleglosc = (df["cena"] - srednia).abs()
    najblizsze = df[odleglosc == odleglosc.min()]
    return srednia, najdrozsze, najtansze, najblizsze


print("Zadanie 1: Pobierz za pomocą scrapy cytaty ze strony http://quotes.toscrape.com/ i zapisz je w formacie .json")
print("Zadanie 2.1: Ze strony https://esklep.polsl.pl/kategoria-produktu/gadzety/ pobierz produkty i ich ceny, a uzyskane dane zapisz w formacie .json")
uruchom_pajaki()

cytaty = wczytaj_json(CYTATY_JSON)
print(f"\nPobrano cytatów: {len(cytaty)} (zapisano w {CYTATY_JSON.name})")
for c in cytaty[:3]:
    print("-", c["author"], ":", c["text"], c["tags"])

dane_produktow = wczytaj_json(PRODUKTY_JSON)
if not dane_produktow:
    raise SystemExit("Nie pobrano żadnych produktów.")
produkty = pd.DataFrame(dane_produktow)
print(f"\nPobrano produktów: {len(produkty)} (zapisano w {PRODUKTY_JSON.name})")
print(produkty[["nazwa", "cena"]].head(10))

print("\nZadanie 2.2: Z danych odczytaj, który produkt jest najdroższy, najtańszy i najbliższy cenie średniej")
srednia, najdrozsze, najtansze, najblizsze = analiza_produktow(produkty)
print(f"Cena średnia: {srednia:.2f} zł")
print("\nNajdroższy:")
print(najdrozsze[["nazwa", "cena"]].to_string(index=False))
print("\nNajtańszy:")
print(najtansze[["nazwa", "cena"]].to_string(index=False))
print("\nNajbliższy cenie średniej:")
print(najblizsze[["nazwa", "cena"]].to_string(index=False))