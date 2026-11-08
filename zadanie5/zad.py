from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

FOLDER = Path(__file__).parent

def wczytaj_cytaty(sciezka=FOLDER / "cytaty.json"):
    df = pd.read_json(sciezka)
    if "author" not in df.columns and "author" in df.index:
        df = df.T
    return df

def cytaty_autora(df, autor):
    return df[df["author"] == autor]["text"]


def unikalne_tagi(df):
    return sorted(df["tags"].explode().dropna().unique())


def cytaty_ze_slowem(df, slowo):
    return df[df["tags"].apply(lambda tagi: slowo in tagi)]


def wczytaj_nauczycieli_surowe(sciezka=FOLDER / "nauczyciele.csv"):
    return pd.read_csv(sciezka, sep=";", decimal=",", dtype={"Kod": str}, encoding="utf-8")


def przygotuj_dane(surowe):
    df = surowe.copy()
    df = df.dropna(axis=1, how="all")
    df = df[df["Nazwa"] != "POLSKA"]
    df = df.drop(columns="Kod")
    df["Nazwa"] = df["Nazwa"].str.capitalize()

    dlugie = df.melt(id_vars="Nazwa", var_name="opis", value_name="liczba")
    czesci = dlugie["opis"].str.split(";", expand=True)
    czesci.columns = ["stanowisko", "plec", "typ", "rok", "jednostka"]
    dlugie = pd.concat([dlugie["Nazwa"].rename("wojewodztwo"), czesci[["stanowisko", "plec", "typ", "rok"]],
                        dlugie["liczba"]], axis=1)
    dlugie["rok"] = dlugie["rok"].astype(int)
    dlugie["liczba"] = dlugie["liczba"].astype(float)
    return dlugie


def suma_uczelni(df, stanowisko, plec="ogółem"):
    d = df[(df["stanowisko"] == stanowisko) & (df["plec"] == plec)]
    return d.groupby(["wojewodztwo", "rok"])["liczba"].sum().unstack("rok")


def wykres_wojewodztwa(df):
    dane = suma_uczelni(df, "nauczyciele akademiccy")
    dane.plot(kind="bar", figsize=(12, 6))
    plt.title("Nauczyciele akademiccy w latach 2014-2018 wg województw")
    plt.xlabel("województwo")
    plt.ylabel("liczba osób")
    plt.legend(title="rok")
    plt.xticks(rotation=60, ha="right")
    plt.grid(True, axis="y", linestyle="--", alpha=0.6)
    plt.tight_layout()
    plt.show()


def wykres_stanowiska_slaskie(df):
    d = df[(df["wojewodztwo"] == "Śląskie") & (df["plec"] == "ogółem")
           & (df["stanowisko"].isin(["asystenci", "adiunkci", "profesorowie"]))]
    dane = d.pivot_table(index="rok", columns="stanowisko", values="liczba", aggfunc="sum")
    dane.plot(kind="bar", figsize=(8, 5))
    plt.title("Stanowiska nauczycieli akademickich w woj. śląskim")
    plt.xlabel("rok")
    plt.ylabel("liczba osób")
    plt.xticks(rotation=0)
    plt.legend(title="stanowisko")
    plt.grid(True, axis="y", linestyle="--", alpha=0.6)
    plt.tight_layout()
    plt.show()


def wykres_plec_slaskie(df):
    d = df[(df["wojewodztwo"] == "Śląskie") & (df["stanowisko"] == "nauczyciele akademiccy")]
    p = d.pivot_table(index=["typ", "rok"], columns="plec", values="liczba")
    p["mężczyźni"] = p["ogółem"] - p["kobiety"]
    p = p[["kobiety", "mężczyźni"]]

    fig, osie = plt.subplots(1, 2, figsize=(11, 5), sharey=True)
    for ax, typ in zip(osie, p.index.get_level_values("typ").unique()):
        p.loc[typ].plot(kind="bar", ax=ax)
        ax.set_title(typ)
        ax.set_ylim(0, p.values.max() * 1.25)
        ax.set_xlabel("rok")
        ax.set_ylabel("liczba osób")
        ax.tick_params(axis="x", rotation=0)
        ax.grid(True, axis="y", linestyle="--", alpha=0.6)
    fig.suptitle("Nauczyciele akademiccy w woj. śląskim wg płci")
    fig.tight_layout()
    plt.show()


def wartosci_dla_wojewodztwa(df, wojewodztwo):
    d = df[df["wojewodztwo"] == wojewodztwo]
    return d.pivot_table(index=["stanowisko", "plec", "typ"], columns="rok", values="liczba")


def najwiecej_najmniej(df, rok=2018):
    razem = suma_uczelni(df, "nauczyciele akademiccy")[rok]
    return razem.idxmax(), razem.max(), razem.idxmin(), razem.min()


def kobiety_ponad_srednia(df, rok=2018):
    kobiety = suma_uczelni(df, "nauczyciele akademiccy", "kobiety")[rok]
    srednia = kobiety.mean()
    return srednia, kobiety[kobiety > srednia].sort_values(ascending=False)


print("Zadanie 1: Za pomocą biblioteki pandas odczytaj z pliku cytaty.json (metoda read_json()).")
cytaty = wczytaj_cytaty()
print(cytaty.head())

print("\n1.1 Cytaty przypisane Albertowi Einsteinowi")
for cytat in cytaty_autora(cytaty, "Albert Einstein"):
    print("-", cytat)

print("\n1.2 Unikalne słowa kluczowe")
tagi = unikalne_tagi(cytaty)
print("Liczba unikalnych słów kluczowych:", len(tagi))
print(tagi)

print("\n1.3 Cytaty ze słowem kluczowym \"love\"")
for _, wiersz in cytaty_ze_slowem(cytaty, "love").iterrows():
    print("-", wiersz["author"], ":", wiersz["text"])

print("\nZadanie 2.1: Wczytaj plik nauczyciele.csv")
surowe = wczytaj_nauczycieli_surowe()
print(surowe.shape)
print(surowe.iloc[:5, :6])

print("\n2.2 Przygotuj dane do dalszej analizy (usuń zbędne wiersze i kolumny, zwróć uwagę na typ danych)")
nauczyciele = przygotuj_dane(surowe)
print(nauczyciele.dtypes)
print(nauczyciele.head())

print("\n2.3a Wykres: nauczyciele akademiccy w latach 2014-2018 z podziałem na województwa")
wykres_wojewodztwa(nauczyciele)

print("\n2.3b Wykres: stanowiska (asystenci, adiunkci, profesorowie) w latach 2014-2018 w województwie śląskim")
wykres_stanowiska_slaskie(nauczyciele)

print("\n2.3c Wykres: uniwersytety i szkoły techniczne z podziałem na płcie w województwie śląskim")
wykres_plec_slaskie(nauczyciele)

print("\n2.4a Wartości dla województwa śląskiego")
print(wartosci_dla_wojewodztwa(nauczyciele, "Śląskie"))

print("\n2.4b Województwa z największą i najmniejszą liczbą zatrudnionych nauczycieli akademickich (2018)")
woj_max, ile_max, woj_min, ile_min = najwiecej_najmniej(nauczyciele, 2018)
print(f"Najwięcej: {woj_max} ({ile_max:.1f} osób)")
print(f"Najmniej: {woj_min} ({ile_min:.1f} osób)")

print("\n2.4c Województwa, które zatrudniają kobiety ponad średnią (2018)")
srednia, powyzej = kobiety_ponad_srednia(nauczyciele, 2018)
print(f"Średnia liczba zatrudnionych kobiet na województwo: {srednia:.1f}")
print(powyzej)