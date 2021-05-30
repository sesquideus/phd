# Dynamické definovanie dopadových oblasti meteoritov a prachových častíc použitím dát z celooblohových kamier\ AMOS

Predložená práca sa zaoberá tvarom trajektórie meteoroidov počas tmavej fázy letu,
predovšetkým jej určeniu na základe dát získaných systémom AMOS vyvinutým na DAA KAFZM FMFI UK.
Hlavným cieľom práce bolo oboznámiť sa s problematikou dynamiky meteoroidov a mikrometeoroidov
pri vstupe do atmosféry Zeme a určiť tvar a polohu ich dopadovej oblasti.

Bakalárska práca je logicky členená do piatich hlavných kapitol.
Prvá a druhá kapitola na primeranej úrovni zhŕňajú teoretické poznatky o malých
telesách Slnečnej sústavy a o dynamike a fenomenológii meteoroidov pri vstupe do atmosféry.
V tretej a štvrtej kapitole autorka popisuje fyzikálny model preletu telesa zemskou atmosférou
a jeho implementáciu v programe ($\mu$)m-Trajectory. V záverečnej kapitole je
dôkladne popísaná aplikácia programu na konkrétny prípad bolidu `EN170420_223923`
Takisto sú v nej prezentované výsledky analýzy.

## Pripomienky k obsahu práce
K obsahu práce nemám závažné výhrady. Členenie a logická náväznosť textu sú
na výbornej úrovni a deklarované ciele práce boli naplnené.
Po dôkladnom preštudovaní nachádzam len dva výraznejšie nedostatky.

### Prachové častice
Na obrázku 20a, resp. 23 sú znázornené miesta dopadu simulovaných prachových častíc,
ktoré ležia prakticky na priamke. Pravdepodobne nejde o skutočný fyzikálny
jav, ale len o artefakt simulácie spôsobený konštantným smerom a rýchlosťou vetra v modeli.

Použitý model rýchlosti vetra pravdepodobne nie je aplikovateľný na takúto veľkú oblasť zemského povrchu.
Vzdialenosť miesta dopadu častice je potom zjavne priamo určená jej hmotnosťou a smer je prakticky nezávislý.
Uvádzať vzdialenosť na štyri platné cifier je pri takejto presnosti modelu taktiež značne prehnané.

### Diskusia
Tento nedostatok modelu sám o sebe nie je závažný -- je však potrebné obmedzenia použitého modelu
dôsledne popísať; prípadne aspoň teoreticky navrhnúť, ako ich obísť alebo odstrániť
(tu napríklad zjavne zahrnutím lepšieho modelu vetra, ktorý by bol závislý aj na zemepisnej šírke a dĺžke a čase,
prípadne zahrnutím chýb samotného modelu vetra a opakovanou simuláciou s mierne odlišnými hodnotami).
Za najproblematickejšiu časť práce preto považujem vyhodnotenie experimentálnych dát a diskusiu k nim.
Na úrovni bakalárskej práce síce nejde o kritický nedostatok,
je ale dôležité uvedomiť si mieru platnosti vlastných výsledkov.

## Pripomienky k forme práce
Práca je písaná v slovenskom jazyku na dobrej gramatickej a syntaktickej úrovni.
Odporúčam pracovať na schopnosti precízne formulovať myšlienky vo vedeckom texte
a vyvarovať sa používaniu vágnych tvrdení.

Oceňujem množstvo a umiestnenie referencií na publikované práce iných autorov.
Pri niektorých rovniciach však nie je z textu zrejmé, či ide o vlastnú myšlienku
autorky alebo o myšlienku prebratú. Takisto fakty, o ktorých sa dá predpokladať, že sú
čitateľovi zorientovanému v meteorickej astronómii všeobecne známe, nie je nutné citovať.

### Technická poznámka {#sec:technical}
-   Citácie a odkazy na obrázky sú podľa všetkého písané ručne a nie vytvorené automaticky.
    V budúcich prácach silne odporúčam použiť zodpovedajúce softvérové riešenie,
    v záujme ušetrenia množstva zbytočnej práce a predídenia prípadným chybám.

### Abstrakt
-   Viacero chýbajúcich určitých členov v anglickej verzii.

### Strana 13
-   "Na rozdiel od planét však nie sú schopné ich pôsobením gravitácie" --- vhodnejšie by bolo napísať "svojím pôsobením".

### Strana 14
-   Trpasličia planéta Ceres je v slovenčine ženského rodu.
-   Citácia (IAU, 2017) by nemala obsahovať názov publikácie [@sec:technical].

### Strana 15
-   "[...] sú uvoľnené excitované alebo ionizované častice, pozorovateľné optickými prístrojmi a radarovými meraniami."
    Priamo pozorovateľné nie sú častice, ale vyžiarené elektromagnetické žiarenia (pri pohľade na lampu nehovoríme
    o pozorovaní častíc žiarovky, ale vidíme svetlo).
-   "približne 42,5 km/s v mieste perihélia, ktorú dosahujú meteoroidy kometárneho pôvodu obiehajúce okolo Slnka"
    Tu by sa hodilo zdôrazniť, že ide o teoretický horný limit, nie všeobecnú charakteristiku.
-   Nepresná formulácia: "padajú ďalej k Zemi rýchlosťou danou gravitačným zrýchlením".

### Strana 16
-   "[...] kým nestratia väčšinu, prípadne celú hmotnosť, kedy končí svetlá fáza letu."
    Chýba kauzálna súvislosť -- svetlá fáza letu je definovaná inak.
-   Vágne, resp. nepresné tvrdenie "jasnosť meteoru je úmerná miere ablácie".
-   Tento druh citácie nie je potrebný (je to všeobecne známa definícia, a takisto to nie je originálna myšlienka autora citovanej práce)
    "Veľmi jasné meteory [...] sa nazývajú bolidy (Havrila, 2018)."

### Strana 17
-   "Prachové častice veľkosti od niekoľko mikrometrov až milimetrov" -- pri
    veľkosti rádovo niekoľko milimetrov už nie je možné hovoriť o prachu.

### Strana 21
-   Správne meno autora v referencii je "Jean-Baptiste Kikwa**y**a".

### Strana 23
-   Definícia v texte odporuje obrázku 5: "$v_h$ je vertikálna zložka, kladná v smere nahor"

### Strana 26
-   Netriviálna rovnica (6) nemá uvedený zdroj a nie je odvodená v texte.

### Strana 27
-   Netriviálna rovnica (11) nemá uvedený zdroj a nie je odvodená v texte.

### Strana 31
-   Python sa podľa štandardu píše s veľkým prvým písmenom.
-   "namiesto integračných krokov cez vzdialenosť (výšku) $\mathrm{d}h$ prebieha výpočet cez časové
    kroky $\mathrm{d}t$" -- z tohoto dôvodu by bolo vhodné v časti 3.2 uviesť rovnice s $\mathrm{d}t$,
    nie všeobecný popis.
-   Obrázok 9: správny termín je *používateľ*, nie *užívateľ* programu.

### Strana 32
-   "poznať fyzikálne charakteristiky tekutiny" -- vhodnejšie by bolo hovoriť o *prostredí*

### Strana 34
-   Referencia má byť správne (ECMWF, 2021) (viď Technickú poznámku).

### Strana 36
-   Vyjadrenie "Do svetlej fázy vstúpil vo výške 91,8 km nad zemou západne od zenitu" nemá zmysel
    bez udania pozorovateľa (v tomto prípade zjavne stanica Važec).

### Strana 41
-   "Jedná sa o ..." $\rightarrow$ "Ide o ..."

### Strana 43
-   Obrázok 16b: chýba určenie polynomickej funkcie a vysvetlenie, čo sú jej nezávislé premenné

### Strana 44
-   Vo vedeckej publikácii je primeranejšie uvádzať čas v sekundách, prípadne iných jednotkách
    vhodných pre danú škálu.


## Otázky
K práci mám nasledujúce otázky:

### Rýchlosť pri vstupe do atmosféry
(Strana 15) Rozpätie možných rýchlostí meteoroidov pri vstupe do atmosféry je autorkou uvedené ako
\SIrange{11.2}{72.8}{\kilo\metre\per\second}.

- Ide o vlastný výpočet autorky, alebo sú tieto hodnoty prevzaté?
- *Prečo* nie je možná menšia, resp. väčšia rýchlosť?

### Modely
-   Ako veľmi vplýva na presnosť určenia polohy prachovej častice pri dopade
    -   presnosť určenia polohy meteoroidu na konci svetelnej fázy letu;
    -   rýchlosti meteoroidu;
    -   rýchlosti vetra?
-   Ak na niečo také ešte máte čas: ako by sa zmenili výsledky simulácie, keby sa model vetra modifikoval
    tak, že pre každý beh simulácie jednej častice jemne náhodne zmeníme zložky $U$ a $V$
    (napríklad gaussovsky so $\sigma = 10\%$)?

## Záver
Práca je napísaná presne, zrozumiteľne a na odbornej úrovni. Študentka preukázala porozumenie
použitým matematickým metódam a algoritmom a je schopná ich aplikovať na získané experimentálne dáta
a vyvodiť z nich vedecké závery.
Napriek drobným formálnym nedostatkom konštatujem, že práca dosiahla ciele vytýčené v zadaní
a splnila všeobecné požiadavky kladené na bakalársku prácu.

Po úspešnej obhajobe ju odporúčam hodnotiť známkou **A**.

 

V Bratislave, 2021--06--01

\hfill Mgr. Martin Baláž

\hfill KAFZM FMFI UK
