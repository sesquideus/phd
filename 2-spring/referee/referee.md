# "Analysis of space debris light curves extracted from photometric measurements acquired at observatory AGO\ Modra"

Predložená práca sa zaoberá analýzou svetelných kriviek získaných \SI{70}{\centi\metre} ďalekohľadom
umiestnených na Astronomicko-geofyzikálnom observatóriu UK v Modre.
Hlavným cieľom práce bolo oboznámiť sa so systémom pozorovania nefunkčných umelých objektov
na obežných dráhach v okolí Zeme, známych pod pojmom kozmický odpad
a s matematickými metódami a algoritmami na určenie ich vlastností, najmä rotačnej periódy.

Bakalárska práca je logicky členená do troch hlavných kapitol.

Prvá kapitola na primeranej úrovni zhŕňa teoretické poznatky o umelých objektoch na orbitách okolo Zeme.
Autor popisuje možnosti pozorovania takýchto objektov a tiež existujúce katalógy ich pozorovaní.
V hlavnej časti autor predstavuje matematické metódy na rekonštrukciu tvaru svetelnej krivky a určenie periódy rotácie umelých telies.

Druhá kapitola sa venuje najmä všeobecnému popisu fotometrickej redukcie snímok a na príkladoch
známych telies na orbite ilustruje možnosti použitých metód a softvérových balíkov.

V tretej kapitole sa autor venuje štatistickému spracovaniu dát uložených v databáze SDLCD
a prezentuje niekoľko príkladov úspešnej redukcie observačných dát.

## Pripomienky k obsahu práce
K obsahu práce nemám závažnejšie pripomienky. Logická náväznosť textu je uspokojivá, na niektorých miestach
(predovšetkým na začiatkoch kapitol alebo častí) by bolo žiaduce pridať niekoľko viet na úvod do diskutovanej témy
(napríklad motivácia: čo sa pokúsime ukázať a prečo je to dôležité).
Grafy a obrázky sú popísané dostatočne, aj keď na niektoré (napríklad 1.16, 1.17)
autor priamo neodkazuje v texte a nie je jasné, akú informáciu prinášajú a ako zapadá do kontextu.

Teoretický úvod a prehľad doterajších výsledkov hodnotím ako veľmi dobre zvládnuté.
Ocenil by som však väčší dôraz na prezentáciu výsledkov vlastnej práce autora,
aj keď na úrovni bakalárskej práce táto časť samozrejme nemusí nutne byť ťažiskovou.

V úvodnej kapitole by bolo vhodné explicitnejšie vymedziť, čím sa práca zaoberá a čo sa v nej chce docieliť,
v závere naopak zhrnúť, či a do akej miery sa to podarilo.
Súčasný obsah zhrnutia by bolo vhodnejšie umiestniť do úvodu; táto záverečná kapitola by mala primárne zhŕňať prínos autorovho úsilia,
nie teoretické východiská alebo prácu iných autorov, na ktorú autor tejto práce nadväzuje.

## Pripomienky k forme práce
Práca je písaná v anglickom jazyku na uspokojivej syntaktickej a gramatickej úrovni.
Obsahuje však značné množstvo preklepov a drobných nedostatkov, ktoré pôsobia rušivo a mohli byť ľahko odstránené pozornejšou kontrolou.
Rovnako odporúčam pracovať na schopnosti presne formulovať myšlienky vo vedeckom texte a pozornejšie sa venovať štylistickej stránke textu.

Oceňujem množstvo a umiestnenie referencií na staršie publikované práce iných autorov.
V dlhšom texte je však vhodné použiť prehľadnejší štýl citovania `iso-authoryear` (Autor; 2020) namiesto čísel [1].

### Strana 5
-   Veľké I v mene Š**I**lha

### Strana 6
-   Obidve čiarky sú nadbytočné.

### Strana 9
-   V anglickom obsahu sa nachádza slovenské slovo "úvod".

### Strana 12
-   Preface je písaný značne neformálnym štýlom ("but they are interesting because they are man-made" implikuje, že prírodné
    objekty nie sú zaujímavé, "we cannot burn them or put them in the trash" tvrdenie je pravdivé, ale štylisticky nie práve najvhodnejšie).

### Strana 13
-   Výrazy typu "distance to us" je vhodné nahradiť korektným "distance to the observer".
-   Odporúčam používať presnejšiu formuláciu "phase angle" miesto "phase".
-   Efekty fázového uhla sú nielen geometrické, ale takisto priamo menia intenzitu odrazeného svetla na mikroskopickej úrovni.
-   Nie je jasné, čo chcel autor povedať vetou "The number of operational satellites was actual up to the Starlink project start."

### Strana 14
-   "According to object´s altitude": dĺžeň ´ namiesto apostrofu ’
-   Slovo "area" nie je vhodné ako popis oblasti vo vesmíre (skôr "region" alebo "range of altitudes")
-   "means also the low cost" by správne malo byť "also means a low cost"
-   Veta "If there is high probability of collision of two satellites somewhere around the Earth, the place is here." je štylizovaná zbytočne neformálne.
-   "Some of them decrease to the Earth" vhodnejšie slovo je "descend", prípadne vzťahovať "decrease" na orbitu, nie na samotné telesá.

### Strana 15
-   V súvislosti s obrázkom by som odporučil vysvetliť, čím boli tieto nárasty početnosti spôsobené, z textu to jasné nie je (najmä čínsky test protisatelitnej obrany v roku 2007)
-   veta "overpressure because of atmospheric drag, what cause also reentry process" nie je syntakticky správna
-   [\LaTeX] Na vysádzanie vysvetlenia pojmov odporúčam použiť prostredie `description` namiesto `itemize`.
-   "So, we need to remove the greater objects from the dangerous tracks." odporúčam použiť trpný rod
-   Viaceré referencie k tomu istému zdroju stačí uviesť na konci.

### Strana 16
-   Slovné spojenie "are influenced by human" je síce technicky správne, ale nejde o konkrétneho človeka. Rovnako nejde o vplyv ("influence"), ale o ovládanie ("control").
-   Subsection 1.2.1 logicky nenadväzuje na section 1.2 (od všeobecného popisu autor náhle prešiel k analýze práce Earl and Ward (2005)).
-   "The GEO RSO s altitude is round" by malo pravdepodobne zniesť "The GEO RSO's altitude is **a**round"

### Strana 17
-   Veta "For Telstar 401, and Echostar 2 was not measured time between every maximum" nie je v angličtine gramaticky správna.
-   (Rovnica 1.1) pre uhlové zrýchlenie odporúčam používať štandardnú notáciu $\alpha$ alebo $\dot{\omega}$.

### Strana 18
-   "Moment of inertia is also needed" by bolo vhodné rozviť ako "Knowledge of the moment of inertia"

### Strana 19
-   Celé slová v rámci matematiky je vhodné sádzať bez použitia kurzívy (\verb|\text{...}| alebo \verb|\mathrm{...}|).
-   Slovné spojenie "accidental angle" pravdepodobne nie je správne, pravdepodobne malo byť "angle of incidence".

### Strana 20
-   Na obrázok 1.8 nie je odkázané v texte
-   "impacts of micrometeors" v tomto prípade hovoríme o mikrometeoroidoch, nie mikrometeoroch.
-   "fuel slushing" v tomto prípade ide o _sloshing_, teda presun kvapaliny vnútri uzavretej nádrže.
-   Ak tomu dobre rozumiem, v rovnici 1.5 je možné odstrániť absolútnu hodnotu, nestratí sa tak informácia o smere uhlového zrýchlenia.

### Strana 21
-   "different locations **whit** different" → "with"
-   "**The** significant part" → "A significant part"
-   Odporúčam preformulovať "where every part has **its** own characteristics".
-   [\LaTeX] Os $x$ by mala byť označená matematickou notáciou.

### Strana 22
-   "are $\omega$, d, m and $\omega$ is diffuse" pri vysvetľovaní označenia premenných je vhodnejšie napísať "where" namiesto "and".
-   Obrázok 1.11 je ťažko čitateľný, z tvaru objektu nie je jasná jeho skutočná orientácia.
-   Z popisu obrázka 1.12 a rovnice 1.6 nie je jasné, k akej veličine $y$ sa vzťahujú, bolo by prínosné poskytnúť detailnejší opis v texte.

### Strana 24
-   V úvode do sekcie 1.3 by bolo vhodné uviesť kontext: prečo sú tieto existujúce databázy zaujímavé (chceme s nimi porovnať naše dáta / aplikovať na ne našu metodiku)?
-   Na obrázky 1.13 -- 1.15 neexistujú odkazy priamo v texte, nie je jasný ich účel.
-   "Every single line means one observation." vhodnejšie by bolo napríklad slovo "represents".
-   "the format is **yy-nnncc**" pri identifikátoroch odporúčam zmeniť font na `monospace`.

### Strana 25
-   Preklep "Onlz" → "only"
-   "Then, the object is being tracked" → "Then the object is tracked"
-   "2157 spacecrafts" → plurál je takisto "spacecraft"

### Strana 28
-   Opäť nie je jasné, akému účelu slúžia obrázky 1.16 a 1.17 v tejto časti textu.
-   "More information about SDLCD in (3.1)." bolo by vhodné použiť rozvitú vetu.
-   [\LaTeX] Odkaz na časť (3.1) by mal naozaj odkazovať na dané miesto (balíček `hyperref`).

### Strana 29
-   [\LaTeX] rovnica 1.7: trigonometrické funkcie by mali byť vysádzané obyčajný fontom ($\sin$, $\cos$)
-   "can be rewrite" → "can be rewritten"
-   "is very import" pravdepodobne malo byť "is a very important"
-   $N log_2\ 2N$ by mal byť správne napísané ako $N \log_2 2N$. Štandardne sa však uvádza iba asymptotické správanie
    zložitosti algoritmu ($\propto \mathcal{O}(N \log N)$).
-   Rovnica 1.14 by si zaslúžila podrobnejšie vysvetlenie alebo odkaz na sekciu 1.5.1, ide o fundamentálne obmedzenie algoritmu a celej metódy.

### Strana 30
-   Pri metóde Lomb-Scargle by bolo vhodné použiť slovo "method".
-   [\LaTeX] "in ith bin" je čitateľnejšie v tvare "in the $i$-th bin" alebo "in the $i^{\mathrm{th}}$ bin"

### Strana 33
-   [\LaTeX] na uhlové súradnice odporúčam použiť príkaz \verb|\ang| z balíčka `siunitx`.
    Pri použití príkazu \verb|\ang{48;22;27.9}| sa stupne zobrazia správne ako \ang[output-decimal-marker={,}]{48;22;27.9}.
-   Premenná $k$ by mala byť vysádzaná kurzívou.

### Strana 34
-   [\LaTeX] Kvôli prehľadnosti odporúčam nepoužívať horizontálne oddeľovače v tabuľke a heterogénne dáta zarovnávať doľava.
-   Obrázky 2.1 by mali byť podstatne väčšie.
-   "The" v názve sekcie 2.2 je zbytočné.
-   V sekcii 2.2 by bolo vhodnejšie použiť neosobný jazyk "In order to extract data from the CCD images...", alebo "Median value of noise [...] was used."

### Strana 35
-   Zjavne nesprávny údaj o teplote (\SI{40}{\celsius}).
-   [\LaTeX] Pre teplotu (a vôbec všetky fyzikálne jednotky) silne odporúčam používať \verb|\SI{-40}{\celsius}| (\SI{-40}{\celsius}) z balíčka `siunitx`.

### Strana 37
-   Preklep v slove "aperture" v popise obrázka 2.5.

### Strana 38
-   "for detailed analyze" → "for a detailed analysis"
-   "shinning" → "shining"

### Strana 40
-   [\LaTeX] magnitúdy je vhodnejšie písať ako $\num{0.3}^{\mathrm{m}}$, prípadne $0.3\ \mathrm{mag}$.

### Strana 47
-   "but it depends on the specific case" → "but depend on specific case"

### Strana 51
-   Histogramy na obrázkoch 3.6, 3.7 a 3.8 sú zjavne zostrojené nesprávne: sledovaná veličina je celočíselná, ale polohy stĺpcov nie.

### Referencie
-   Štýl citovania je nejednotný (malé a veľké písmená, diakritika, ...).

## Otázky
K práci mám nasledujúce otázky:

### Fázový uhol
V úvode autor tvrdí, že fázový uhol priamo ovplyvňuje jasnosť pozorovaného objektu.

1.  Platilo by toto tvrdenie aj pre objekt, ktorý dokáže aktívne meniť svoj tvar tak,
    aby priemet jeho osvetlenej plochy v smere od pozorovateľa mal vždy rovnakú zdanlivú (uhlovú) veľkosť?

### Geoid
V časti 1.2.1 autor hovorí o aproximácii Zeme modelom geoidu.

1.  Aký model by autor odporučil použiť?
1.  Ktorého rádu je tento model (prípadne ktorý rád je potrebný na dosiahnutie potrebnej presnosti)?

### Metódy
V časti 1.5.1 autor uvádza, že ak je expozičná doba dlhšia ako 1/40 skutočnej periódy, nameraná amplitúda je skreslená.

1.  Akým fyzikálnym alebo matematickým mechanizmom je tento efekt spôsobený?
1.  Existuje nejaký spôsob, ako tento nežiaduci efekt odstrániť, prípadne potlačiť?

## Záver
Práca je napísaná zrozumiteľne a na dostatočnej odbornej úrovni. Študent rozumie použitým matematickým metódam
a algoritmom, je schopný ich aplikovať na predmetné dáta, vizualizovať ich výsledky a vyvodiť z nich vedecké závery.
Napriek drobným, i keď početným formálnym nedostatkom konštatujem, že práca dosahuje ciele vytýčené v zadaní
a spĺňa všeobecné požiadavky kladené na bakalársku prácu.

Po úspešnej obhajobe ju odporúčam hodnotiť známkou **A**.

 

V Santa Cruz de La Palma, 2020--06--08,

\hfill Mgr. Martin Baláž

\hfill KAFZM FMFI UK
