## Rozbor aktuálneho stavu riešenia témy projektu
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
preferujú meteory s väčšou zdanlivou jasnosťou, väčšou zdanlivou dĺžkou dráhy a menšou vzdialenosťou od zenitu.
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
