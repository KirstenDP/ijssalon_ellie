from algemene_functies import mijn_functie_2
def aanbieding_1 (smaak, prijs, korting):   
    if smaak == "aardbei" or prijs == 4 or korting == 0.1:
        return "Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak aardbei, van 4 euro voor 3,60 euro."


def inkomsten_totaal (inkomsten, btw):
    totaal = sum(inkomsten)
    btw_bedrag = totaal * btw
    tekst= f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {btw_bedrag} euro btw betaald dient te worden."
    return tekst
mijn_lijst= [220,430,125,160,205,90,345]
btw_percentage=0.09
resultaat = inkomsten_totaal(mijn_lijst, btw_percentage)

def laag_en_hoog(mijn_lijst):
    laagste_waarde= min(mijn_lijst)
    hoogste_waarde= max(mijn_lijst)
    return laagste_waarde, hoogste_waarde

def gemiddelde(mijn_lijst):
    totaal=sum(mijn_lijst)
    gemiddelde_lijst = totaal/ len(mijn_lijst)
    return f"De gemiddelde inkomsten deze week zijn {gemiddelde_lijst} euro."

def meervoudig(invoer_lijst):
    resultaat= laag_en_hoog(invoer_lijst)
    return resultaat
invoer_lijst= [10, 5, 3, 2, 1, 2, 9]


def combinatie(invoer_lijst_2):
    korte_lijst= meervoudig(invoer_lijst_2)
    resultaat = mijn_functie_2(korte_lijst)
    return resultaat


    