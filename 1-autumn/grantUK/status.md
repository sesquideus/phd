## Rozbor aktuálneho stavu riešenia témy projektu



Hlavným parametrom konkrétnej populácie meteoroidov je _hmotnostný exponent_ $s$,
ktorým popisujeme distribúciu hmotností častíc ako mocninnú závislosť $N(m) \propto m^{-s}$ [@pokorny-brown2016].
Pre častice 
súčasné modely sú vo viacerých ohľadoch nedostatočné.


Pri redukcii dát z tradičných vizuálnych alebo prístrojových pozorovacích metód sa obvykle neuvažujú výberové efekty (selection bias).
Do zaznamenaných pozorovaní vstupuje rad vplyvy, ktoré skresľujú výslednú štatistickú vzorku.
Tieto efekty môžeme rozdeliť na

- prirodzené, teda spôsobené fyzikálnymi danosťami prostredia, napríklad
    - rôzne vzdialenosti medzi pozorovateľom a meteorom,
    - pokles intenzity kvôli absorpcii v atmosfére,
    - prírodné alebo umelé svetelné znečistenie;
    
- inštrumentálne, čiže spôsobené nedokonalosťou prístroja, ako napríklad
    - vinetácia (pokles osvitu senzora smerom k okrajom zorného poľa),
    - nehomogenity optickej cesty alebo čipu,
    - softvérové chyby a chyby pri spracovaní obrazu.

Automatické videostanice, fotografické prístroje aj priame vizuálne pozorovania prirodzene
preferujú meteory s väčšou zdanlivou jasnosťou, väčšou zdanlivou dĺžkou dráhy a menšou vzdialenosťou od zenitu.
Tieto efekty je potrebné zmerať a vyvinúť procedúry na ich odstránenie.
Alternatívnym spôsobom korekcie je numerická simulácia, v ktorej vytvoríme populáciu
meteoroidov, simulujeme ich vstup do atmosféry a následne štatisticky vyhodnocujeme
pozorovaný súbor meteorov. Porovnaním výstupu simulácie so skutočnými pozorovaniami za
rovnakých podmienok získavame mieru zhody. Postupnými zmenami parametrov simulácie
a veľkosti výberových efektov sme schopní určiť hodnoty parametrov, pre ktoré je dosiahnutá najlepšia
možná zhoda medzi simuláciou a pozorovaním a simulovanú populáciu vyhlásiť za model
rozloženia meteoroidných častíc.

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
pôsobiacich výberových efektov. Publikované dáta [@hughes1995] [@krisciunas1980] udávajú hodnoty $s$ približne \num{1.85},
prípadne iba \num{1.7} [@belkovich2006]. Tieto hodnoty však nie sú konzistentné s výsledkami simulácií,
keďže najlepšia zhoda s experimentálnymi dátami je dosiahnutá až pri podstatne vyššej hodnote $s = \num{2.15}$.
Pravdepodobným vysvetlením je práve nízka detekčná schopnosť pozorovateľov pri zaznamenávaní menej hmotných častíc.

### Referencie
