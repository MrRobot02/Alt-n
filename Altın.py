# Bu araç @Hilas tarafından | @KekikAkademi için yazılmıştır.


import requests
from bs4 import BeautifulSoup

r = requests.get("http://www.altinkaynak.com/Altin/Kur/Guncel")

source = BeautifulSoup(r.content, "html.parser")

ara1 = source.find("span", class_="title")
ara2 = source.find("span", class_="date")
ara3 = source.find("i", class_="time")
print(ara1.text, ara2.text, ara3.text, "", end="")
print("")
print("-" * 31, sep="")

baslik = source.find("tr", class_="title")
print(baslik.text)

alSat = source.find("th", attrs={"id": "cphMain_cphSubContent_thBuy"})
satAl = source.find("th", attrs={"id": "cphMain_cphSubContent_thSell"})
print(" " * 24, alSat.text, "  ", satAl.text)
print(" " * 22, "-" * 7, "", "-" * 7)

hasaltın = source.find("td", attrs={}).text
hasaltın1 = source.find("td", attrs={"id": "tdHH_TBuy"}).text
hasaltın2 = source.find("td", attrs={"id": "tdHH_TSell"}).text
print(hasaltın, "     ", hasaltın1[:8], hasaltın2)
print("-" * 40)

külaltın = source.find("tr", attrs={"data-flag": "CH_T"}).text
külaltın1 = source.find("td", attrs={"id": "tdCH_TBuy"}).text
külaltın2 = source.find("td", attrs={"id": "tdCH_TSell"}).text
print(külaltın.replace("arrow", " " * 5)[:-17], külaltın1[:8], külaltın2[:])
print("-" * 40)

gramltın = source.find("tr", attrs={"data-flag": "GAT"}).text
gramltın1 = source.find("td", attrs={"id": "tdGATBuy"}).text
gramltın2 = source.find("td", attrs={"id": "tdGATSell"}).text
print(gramltın.replace("arrow", " " * 6)[:-17], gramltın1[:8], gramltın2[:])
print("-" * 40)

eskibilezik = source.find("tr", attrs={"data-flag": "B_T"}).text
eskibilezik1 = source.find("td", attrs={"id": "tdB_TBuy"}).text
eskibilezik2 = source.find("td", attrs={"id": "tdB_TSell"}).text
print(eskibilezik.replace("arrow", " " * 3)[:-17], eskibilezik1[:8], eskibilezik2)
print("-" * 40)

atacumhuriyet = source.find("tr", attrs={"data-flag": "A_T"}).text
atacumhuriyet1 = source.find("td", attrs={"id": "tdA_TBuy"}).text
atacumhuriyet2 = source.find("td", attrs={"id": "tdA_TSell"}).text
print(atacumhuriyet.replace("arrow", " " * 3)[:-20], atacumhuriyet1[:8], atacumhuriyet2[:8])
print("-" * 40)

eskiceyrek = source.find("tr", attrs={"data-flag": "EC"}).text
eskiceyrek1 = source.find("td", attrs={"id": "tdECBuy"}).text
eskiceyrek2 = source.find("td", attrs={"id": "tdECSell"}).text
print(eskiceyrek.replace("arrow", " " * 5)[:-16], eskiceyrek1[:8], eskiceyrek2[:8])
print("-" * 40)

eskiyarım = source.find("tr", attrs={"data-flag": "EY"}).text
eskiyarım1 = source.find("td", attrs={"id": "tdEYBuy"}).text
eskiyarım2 = source.find("td", attrs={"id": "tdEYSell"}).text
print(eskiyarım.replace("arrow", " " * 6)[:-18], eskiyarım1[:8], eskiyarım2[:8])
print("-" * 40)

eskiteklik = source.find("tr", attrs={"data-flag": "ET"}).text
eskiteklik1 = source.find("td", attrs={"id": "tdETBuy"}).text
eskiteklik2 = source.find("td", attrs={"id": "tdETSell"}).text
print(eskiteklik.replace("arrow", " " * 5)[:-18], eskiteklik1[:8], eskiteklik2[:8])
print("-" * 40)

gümüs = source.find("tr", attrs={"data-flag": "AG_T"}).text
gümüs1 = source.find("td", attrs={"id": "tdAG_TBuy"}).text
gümüs2 = source.find("td", attrs={"id": "tdAG_TSell"}).text
print(gümüs.replace("arrow", " " * 17)[:-12], gümüs1[:6], " " * 1, gümüs2[:8])
print("-" * 40)

print("")
print("")
print("")
print("")

baslik1 = source.find("h3", id="cphMain_cphSubContent_hSingle")
print(baslik1.text)
print("")
print("")

alSat = source.find("th", attrs={"id": "cphMain_cphSubContent_thBuy"})
satAl = source.find("th", attrs={"id": "cphMain_cphSubContent_thSell"})
print(" " * 24, alSat.text, "  ", satAl.text)
print(" " * 22, "-" * 7, "", "-" * 7)

bilezik_22 = source.find("tr", attrs={"data-flag": "B"}).text
bilezik_221 = source.find("td", attrs={"id": "tdBBuy"}).text
bilezik_222 = source.find("td", attrs={"id": "tdBSell"}).text
print(bilezik_22.replace("arrow", " " * 7)[:-16], bilezik_221[:8], bilezik_222[:8])
print("-" * 40)

altın_18 = source.find("tr", attrs={"data-flag": "18"}).text
altın_181 = source.find("td", attrs={"id": "td18Buy"}).text
altın_182 = source.find("td", attrs={"id": "td18Sell"}).text
print(altın_18.replace("arrow", " " * 9)[:-16], altın_181[:8], altın_182[:8])
print("-" * 40)

altın_14 = source.find("tr", attrs={"data-flag": "14"}).text
altın_141 = source.find("td", attrs={"id": "td14Buy"}).text
altın_142 = source.find("td", attrs={"id": "td14Sell"}).text
print(altın_14.replace("arrow", " " * 9)[:-16], altın_141[:8], altın_142[:8])
print("-" * 40)

ceyrek = source.find("tr", attrs={"data-flag": "C"}).text
ceyrek1 = source.find("td", attrs={"id": "tdCBuy"}).text
ceyrek2 = source.find("td", attrs={"id": "tdCSell"}).text
print(ceyrek.replace("arrow", " " * 10)[:-16], ceyrek1[:8], ceyrek2[:8])
print("-" * 40)

yarim = source.find("tr", attrs={"data-flag": "Y"}).text
yarim1 = source.find("td", attrs={"id": "tdYBuy"}).text
yarim2 = source.find("td", attrs={"id": "tdYSell"}).text
print(yarim.replace("arrow", " " * 11)[:-18], yarim1[:8], yarim2[:8])
print("-" * 40)

teklik = source.find("tr", attrs={"data-flag": "T"}).text
teklik1 = source.find("td", attrs={"id": "tdTBuy"}).text
teklik2 = source.find("td", attrs={"id": "tdTSell"}).text
print(teklik.replace("arrow", " " * 10)[:-18], teklik1[:8], teklik2[:8])
print("-" * 40)

gramse = source.find("tr", attrs={"data-flag": "G"}).text
gramse1 = source.find("td", attrs={"id": "tdGBuy"}).text
gramse2 = source.find("td", attrs={"id": "tdGSell"}).text
print(gramse.replace("arrow", " " * 10)[:-18], gramse1[:8], gramse2[:8])
print("-" * 40)

yeni_ata = source.find("tr", attrs={"data-flag": "A"}).text
yeni_ata1 = source.find("td", attrs={"id": "tdABuy"}).text
yeni_ata2 = source.find("td", attrs={"id": "tdASell"}).text
print(yeni_ata.replace("arrow", " " * 8)[:-18], yeni_ata1[:8], yeni_ata2[:8])
print("-" * 40)

resat = source.find("tr", attrs={"data-flag": "R"}).text
resat1 = source.find("td", attrs={"id": "tdRBuy"}).text
resat2 = source.find("td", attrs={"id": "tdRSell"}).text
print(resat.replace("arrow", " " * 11)[:-18], resat1[:8], resat2[:8])
print("-" * 40)

hamit = source.find("tr", attrs={"data-flag": "H"}).text
hamit1 = source.find("td", attrs={"id": "tdHBuy"}).text
hamit2 = source.find("td", attrs={"id": "tdHSell"}).text
print(hamit.replace("arrow", " " * 11)[:-18], hamit1[:8], hamit2[:8])
print("-" * 40)

gram = source.find("tr", attrs={"data-flag": "GA"}).text
gram1 = source.find("td", attrs={"id": "tdGABuy"}).text
gram2 = source.find("td", attrs={"id": "tdGASell"}).text
print(gram.replace("arrow", " " * 14)[:-18], gram1[:8], gram2[:8])
print("-" * 40)