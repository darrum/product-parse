# Produktu web-lapu pieejamības analizēšana tirgus situācijas izvertēšanai

## 🎯 Projekta mērķis
Šīs projekts demonstrē Selenium Webdriver izmantošanu, lai analizētu tīmekļī produktu weblapas un iegūtu nepieciešamo informāciju, šajā gadījumā saites uz weblapām.

Šīs projekts tika veidots uz darba uzdevuma pamata. Man bija pieejami vairāki excel faili ar dažādiem partner - uzņēmumu produktu sarakstiem, kuros ietilpst ierīces modeļa numurs, nosaukums, tehniskie parametri, izmēri u.c. Šī projekta ietvaros es apskatīšu tikai vienu no tiem. Konfidenciālas informācijas dēļ es izdzēsu dažu kolonnu saturu. To sarakstu vidū bija iekļauti produkti, kuri vairs netiek ražoti. Ar šādu neaktuālo informāciju ir grūti izvertēt situāciju un veikt uzņemējdarbības lēmumus, līdz ar to darba uzdevums iekļāva sevī mērķi atzīmēt neaktuālos produktus. 

Kā arī sakarā ar to, ka pasūtījumi tiek pieņemti izmantojot mājaslapā esošo kontaktformu, darbiniekiem bija jāvelta lielāks laiks meklējot visu informāciju par produktu un tā pieejamību. Līdz ar to bija nepieciešams pievienot saites un katra produkta weblapu.

## 📦 Izmantotas bibliotēkas
- [openpyxl](https://openpyxl.readthedocs.io/en/stable/) — manipulācijām ar Excel tabulām (lasīšanai un rakstīšanai);
- [selenium](https://www.selenium.dev/documentation/) — lai atdarinātu tīmekļa pārlūkprogrammas darbību un iegūtu informāciju no tīmekļa lapām.

## 📈 Darba metodes
Šis projekts izmanto `openpyxl`, lai iegūtu produktu modeļu numurus no Excel tabulas, lai izmantotu tos turpmākā produkta web-lapas meklēšanā;
Tālāk tiek izmantots `Selenium Webdriver`, lai automātiski atvērtu meklēšanas lapu pārlūkprogrammā, automātiski meklējot noteiktu produktu.
Ja šāds produkts ir pieejams, notiek pāreja uz produkta lapu, no kuras tiek nokopēta saite un saglabāta Excel tabulā. Ja tāda produkta nav, tad automātiski Excel tabulā saites vietā ir rakstīts, ka produkts nav pieejams.

## 🔧 Instalēšana
```commandline
pip install -r requirements.txt
```

## 🚀 Palaišana
```commandline
python main.py
```

## 🏁 Rezultāti un secinājumi

Augstāk aprakstītie mērķi tika veiksmīgi sasniegti. Izpildot kodu, Excel tabulā tiek saglabātas saites tikai uz tiem produktiem, kuri šobrīd tiek pieejami klientiem, kā arī ir viegli pamanāmi produkti, no kuru ražošanas mūsu partnieri nolēma atteikties. Pateicoties Excel faila apstrādei, tas ļāva uzņemuma vadītājiem izanalizēt tirgus situāciju un, pamatojoties uz šo informāciju, pieņemt stratēģiski svarīgus lēmumus.

Analizējot izstrādes sarežģītos posmus, es varētu teikt, ka vislielākas grūtības sagādāja noteikta elementa meklēšana izmantojot XPATH, līdz ar to es turpināsu attīstīt savas prasmes šajā jomā.

Secinot, izstrādājot šo projektu, man kļuva saprotamāka automatizēta pieeja datu apstrādei. Tas palīdzēja veltīt laiku svarīgākiem uzdevumiem un optimizēt darba laika izmantošanu. 
