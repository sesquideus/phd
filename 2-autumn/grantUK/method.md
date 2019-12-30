## Návrh metódy riešenia projektu
Základom metódy je numerická $N$-body simulácia.
V\ simulácii vytvárame jednotlivé častice v okolí známych materských telies
a následne numerickou integráciou pohybových rovníc určujeme ich budúcu polohu.
Celkové silové pôsobenie je dané najmä gravitačným pôsobením Slnka ako centrálneho telesa,
rušiacimi gravitačnými vplyvmi planét a pôsobením materského objektu.
Pre častice s veľmi malými rozmermi sú dôležité aj negravitačné vplyvy, najmä
tlak slnečného žiarenia a Poyntingov-Robertsonov efekt.

Ak počas integrácie dôjde ku kolízii niektorej z častíc so Zemou, daná častica je označená ako
spozorovaná. Sumárny štatistický súbor všetkých takýchto častíc je po aplikácii výberových efektov
možné porovnať s pozemskými pozorovaniami a určiť zhodu s experimentálnymi dátami. Variáciou parametrov
simulácie a minimalizáciou odchýlok sme schopní určiť skutočnú distribúciu a pôvodné dráhy telies.
Opätovné spustenie simulácie s optimálnymi hodnotami parametrov spolu so znalosťou dráhy skutočného
materského telesa nám umožnia identifikovať jednotlivé prúdy častíc, predpovedať
aktivitu zodpovedajúcich meteorických rojov a určiť priestorovú koncentráciu meteoroidov v priestore.

Získaný model je potrebné _redukovať_ na pozorovateľa, teda určiť, ktoré z častíc svojimi dráhami
pretnú atmosféru Zeme a teda budú môcť byť detegované ako meteor. Celkový súbor registrovaných meteorov,
opravený o výberové efekty spôsobené prírodnými javmi alebo vlastnosťami použitých prístrojov,
potom musí zodpovedať observačným dátam získaným pozemnými stanicami.

Aktivitu meteorických rojov môžeme popísať pomocou dvoch priestorových a jednej časovej súradnice.
Priestorovými súradnicami sú sférická výška a dĺžka na oblohe, teda v ekvatoriálnej súradnicovej sústave
_deklinácia_ a _rektascenzia_ radiantu. Roj telies so spoločným pôvodom vykazuje iba veľmi pomalú zmenu
polohy radiantu v čase. Tento údaj je možné spolu s rýchlosťou častíc použiť na identifikáciu meteorického roja.

Z vedeckého aj pozorovateľského hľadiska sú dôležitejšie zmeny aktivity roja v čase.
Variácie aktivity na majú trojaký pôvod. Dominantným efektom je _periodická variácia_,
spôsobená zmenou geometrie Zeme voči prúdu meteoroidov, s periódou s dĺžkou jedného roka.
Meteorické roje sú v zemskej atmosfére pozorovateľné iba vtedy, keď sa Zem nachádza v okolí výstupného
alebo zostupného uzla jeho dráhy. Typická šírka prúdu je o niekoľko rádov menšia, ako polomer zemskej dráhy,
takže vhodné podmienky nastávajú pre každý roj iba raz ročne.

Druhým opakujúcim sa vplyvom sú zmeny obežnej dráhy prúdu v dôsledku gravitačného pôsobenia
planét alebo negravitačných vplyvov, napríklad Jarkovského alebo Poynting-Robertsonovho efektu.
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
častíc a celkovú zmenu hmotnosti Zeme v dôsledku zrážok s medziplanetárnou hmotou.

Vhodným rozšírením by bola implementácia paralelného integrátora
pre súčasný výpočet dráh množstva vzájomne neinteragujúcich častíc.
Hmotné objekty (čiže Slnko a planéty, prípadne materské teleso roja) na seba vzájomne pôsobia
nezanedbateľnými silami, ktoré je nutné integrovať klasickým sekvenčným spôsobom pomocou CPU.
Gravitačný vplyv nami skúmaných drobných telies na veľké planéty však môžeme úplne zanedbať.
Preto je možné ich dráhy počítať s využitím masívnej paralelizácie pomocou GPU.

Spojením efektívnych numerických metód na výpočet pohybov telies v medziplanetárnom priestore
a simulácie vstupu častíc do atmosféry vrátane ablačných a dynamických efektov [@balaz+2020]
budeme schopní vytvoriť kompletný model životného cyklu malých častíc v Slnečnej sústave.

### Referencie
