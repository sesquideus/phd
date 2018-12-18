## Rozbor aktuálneho stavu riešenia témy projektu
súčasné modely sú vo viacerých ohľadoch nedostatočné.

Bežné vizuálne alebo prístrojové pozorovacie metódy obvykle neberú do úvahy výberové efekty (selection bias).
Do zaznamenaných pozorovaní vstupuje rad efektov, ktoré skresľujú výslednú štatistickú vzorku.
Tieto vplyvy môžeme rozdeliť na

- prirodzené, teda spôsobené fyzikálnymi danosťami prostredia, napríklad
    - rôzne vzdialenosti medzi pozorovateľom a meteorom,
    - pokles intenzity kvôli absorpcii v atmosfére,
    - prírodné alebo umelé svetelné znečistenie;
    
- inštrumentálne, čiže spôsobené nedokonalosťou prístroja, ako napríklad
    - vinetácia (pokles osvitu senzora smerom k okrajom zorného poľa),
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
dát pri pozemských pozorovaniach meteorov [@gural2002].

nadväzuje na numerickú simuláciu častíc,
ktorá bola vyvinutá v rámci diplomovej práce [@balaz2018]

podozrenie, že udávané hodnoty hmotnostného exponentu $s$ sú všeobecne skreslené nedostatočným
zahrnutím všetkých pôsobiacich výberových efektov. Publikované dáta následne často udávajú podstatne nižšie
hodnoty $s$, ako je reálne.

### Referencie
