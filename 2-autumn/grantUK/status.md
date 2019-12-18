## Rozbor aktuálneho stavu riešenia témy projektu

Celkovú aktivitu meteorických rojov môžeme popísať pomocou dvoch priestorových a jednej časovej súradnice,


Priestorovými súradnicami sú sférická výška a dĺžka na oblohe, teda v ekvatoriálnej súradnicovej sústave
_deklinácia_ a _rektascenzia_ radiantu. Roj telies so spoločným pôvodom vykazuje iba veľmi pomalú zmenu
polohy radiantu v čase. Tento údaj je možné spolu s rýchlosťou častíc použiť na identifikáciu meteorického roja.

Variácie aktivity na časovej osi majú trojaký pôvod. Dominantným efektom je _periodická variácia_,
spôsobenú zmenou geometrie Zeme voči prúdu meteoroidov, s periódou s dĺžkou jedného roka.
Meteorické roje sú v zemskej atmosfére pozorovateľné iba vtedy, keď sa Zem nachádza v okolí výstupného
alebo zostupného uzla jeho dráhy. Typická šírka prúdu je o niekoľko rádov menšia, ako polomer zemskej dráhy,
takže vhodné podmienky nastávajú pre každý roj iba raz ročne.

Druhým opakujúcim sa vplyvom sú zmeny obežnej dráhy prúdu v dôsledku gravitačného pôsobenia
planét alebo negravitačných vplyvov, napríklad Jarkovského efektu [@yarkovsky] alebo Poynting-Robertsonovho efektu [@pr].
Tie sú zodpovedné za výrazné medziročné kolísanie aktivity meteorických rojov.
Výsledná perióda závisí od obežnej periódy materského telesa roja, prípadne rušiaceho telesa.
Typickým príkladom je výrazné dvanásťročné maximum aktivity Perzeíd alebo opakujúce sa
výrazné maximá Leoníd s periódou 33 rokov.

Na dlhých časových škálach môžeme pozorovať _sekulárne zmeny_ aktivity. Prúdy meteoroidov
spravidla vznikajú pomerne náhle po priblíženiach materského telesa k Slnku
a následne sa v dôsledku nerovnomerného pôsobenia rušiacich síl rozširujú.
Ak materiál nie je dopĺňaný počas ďalších priblížení materského telesa k Slnku,
meteorický roj v priebehu niekoľko tisíc rokov zanikne.
Celková zmena aktivity v čase je určená sumou všetkých vplývajúcich efektov.

Okrem polohových a časových súradníc môžeme mapu meteorickej aktivity doplniť ďalšími
informáciami, najmä o geocentrických rýchlostiach častíc alebo o distribúciách hmotností
meteoroidov v konkrétnych rojoch. S touto znalosťou budeme schopní určiť celkový tok
častíc a zmenu hmotnosti Zeme v dôsledku zrážok s medziplanetárnou hmotou.

REBOUND

(Kováčová)


Moderné siete fotografických staníc a videostaníc poskytujú dostatočne presné dáta na
určenie dráhových charakteristík pozorovaných telies [@borovicka1990].
Nemožnosť reprodukovania meteorov v laboratórnych podmienkach
však necháva veľké neistoty v určení hodnôt niektorých fyzikálnych
parametrov, ako napríklad skutočnej hmotnosti meteoroidov alebo distribúcie hmotností
v populácii.

Základným parametrom populácie meteoroidov je _hmotnostný exponent_ $s$,
ktorým popisujeme distribúciu hmotností častíc ako mocninnú závislosť $N(m) \propto m^{-s}$ [@pokorny-brown2016].
Súčasné modely určenia hmotnostného exponentu sú však vo viacerých ohľadoch nedostatočné.
Pri redukcii dát z tradičných vizuálnych alebo prístrojových pozorovacích metód sa obvykle neuvažujú výberové efekty (_selection bias_).
Do zaznamenaných pozorovaní vstupuje rad prirodzených aj inštrumentálnych vplyvov, ktoré skresľujú výslednú štatistickú vzorku.
Automatické videostanice, fotografické prístroje aj vizuálne pozorovania prirodzene
preferujú meteory s väčšou zdanlivou jasnosťou a dĺžkou dráhy a menšou vzdialenosťou od zenitu.
Tieto efekty je potrebné zmerať a vyvinúť procedúry na ich odstránenie. Ďalšie parametre
populácie je možné určiť až po oprave štatistického súboru o výberové efekty.

Alternatívnym spôsobom korekcie je numerická simulácia, v ktorej vytvoríme populáciu
meteoroidov, simulujeme ich vstup do atmosféry a pozorovaný súbor meteorov následne štatisticky vyhodnocujeme.
Porovnaním výstupu simulácie so skutočnými pozorovaniami za rovnakých podmienok získavame mieru zhody.
Postupnými zmenami parametrov simulácie a veľkosti výberových efektov sme schopní určiť hodnoty parametrov,
pre ktoré je dosiahnutá najlepšia možná zhoda medzi simuláciou a pozorovaním. Simulovanú populáciu potom
môžeme vyhlásiť za štatistický model skutočného rozloženia meteoroidných častíc.

Podobné postupy sú využívané na odstránenie výberových efektov pri astronomických pozorovaniach
blízkozemských asteroidov [@chesley2017], ale dosiaľ neboli aplikované na opravu štatistických
dát pri pozemských pozorovaniach meteorov. Úspešne však boli použité na odhad
celkového počtu viditeľných meteorov [@gural2002].
Výsledky sú priamo porovnateľné s hodnotami získanými inými metódami, napríklad
vizuálnymi pozorovaniami vykonanými skupinou pozorovateľov, priamou
redukciou dát z kamerových systémov AMOS [@zigo2013] a CILBO [@koschny2013]
alebo inými metódami [@blaauw2016].
Špeciálnu pozornosť sme venovali porovnaniu s analýzami konkrétnych pozorovacích nocí,
publikovanými napríklad portálom `MeteorFlux.io` [@meteorflux].

Predbežné výsledky [@balaz2018] indikujú, že udávané hodnoty hmotnostného exponentu $s$ sú všeobecne skreslené ignorovaním
pôsobiacich výberových efektov. Publikované dáta udávajú hodnoty $s$ približne \num{1.85} [@hughes1995; @krisciunas1980],
prípadne iba \num{1.7} [@belkovich2006]. Tieto hodnoty však nie sú konzistentné s výsledkami simulácií -- zhoda
s experimentálnymi dátami je dosiahnutá až pri podstatne vyššej hodnote $s = \num{2.15}$.
Pravdepodobným vysvetlením je práve nízka detekčná schopnosť pozorovateľov pri zaznamenávaní menej hmotných častíc
a z nej vyplývajúce podhodnotenie ich skutočného počtu.

### Referencie
