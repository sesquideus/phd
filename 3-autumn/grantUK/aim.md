## Charakteristika vedeckých cieľov projektu
Meteoroidy, čiže malé kamenné alebo železné telieska obiehajúce okolo Slnka,
sú jedným z najcennejších zdrojov informácií o pôvode a vývoji Slnečnej sústavy.
Za meteoroidy považujeme telesá s rozmermi v rozpätí \SI{30}{\micro\metre} až
\SI{1}{\metre} [@imo-definitions]; pričom väčšie telesá nazývame asteroidmi
a pri menších telesách hovoríme o medziplanetárnom prachu.
Pri súčasnom stave techniky nie je možné meteoroidy pozorovať priamo
v otvorenom medziplanetárnom priestore. Ak však dráha meteoroidu križuje dráhu Zeme
a teleso vstúpi do zemskej atmosféry, jeho kinetická energia je dostatočná
na roztavenie a ionizáciu materiálu, z ktorého je zložený.
Vznikajúcu svetelnú stopu následne môžeme pozorovať ako meteor.

Dominantným zdrojom meteoroidov sú malé telesá Slnečnej sústavy, najmä kométy
a blízkozemské asteroidy. Tieto telesá sa pri priblíženiach k Slnku zahrievajú
a následne uvoľňujú drobné úlomky, prípadne fragmentujú pri vzájomných zrážkach.
Mierne odlišnosti počiatočných rýchlostí telies, gravitačné perturbácie pochádzajúce od planét
a rôzne negravitačné efekty pôsobiace na častice spôsobujú, že ich dráhy sa počas dlhých časových období
pomaly menia a diverzifikujú. Na škálach stoviek až tisícov rokov vytvoria široký prstenec
okolo pôvodnej orbity svojho materského telesa. Na ešte dlhších škálach sa prstence rozpadajú
a prispievajú do *sporadického pozadia*, teda zdroja rozptýlených
meteoroidov na zdanlivo náhodných dráhach [@jenniskens1998].

Metódy pozorovania meteorov v zemskej atmosfére zahŕňajú priame pozorovanie voľným okom,
záznam fotografickými kamerami s dlhou expozíciou alebo videokamerami, a tiež radarové pozorovania.
Na oddelení astronómie a astrofyziky KAFZM FMFI bol vyvinutý
automatický videosystém AMOS, čiže All-sky Meteor Orbit System [@zigo+2013].
Stanica systému AMOS pozostáva z celooblohovej kamery,
zosilňovača jasu obrazu a počítača s detekčným softvérom.
Pri detekcii meteoru kamerou počítač analyzuje videozáznam a údaje odošle na centrálny server.

Problematickou časťou automatického spracovania pozorovaní je určenie
jasnosti meteoru v jednotlivých snímkach videozáznamu,
primárne kvôli šumu a nehomogenitám zosilňovača jasu obrazu.
Takisto nie je známe, nakoľko je spoľahlivý softvérový diskriminátor, čiže procedúra,
ktorá rozhodne, či v danom úseku videozáznamu je viditeľný meteor.
Zatiaľ čo falošné detekcie je možné manuálne vymazať neskôr,
kvôli obmedzenej kapacite pevných diskov nie je možné
uchovávať záznamy z celého priebehu pozorovania. Množstvo meteorov preto nie je
zaznamenané napriek tomu, že sú jasnejšie, ako teoretický spodný
detekčný limit jasnosti pre daný pozorovací systém.

Primárnym cieľom projektu je určiť skutočnú citlivosť kamier systému AMOS porovnaním
s inými detekčnými systémami, prípadne voľným okom. Na základe kalibrácie pomocou svetelných zdrojov
so známymi parametrami sa následne pokúsime odhadnúť pravdepodobnostť
detekcie meteoru (*detection probability function* -- DPF) ako funkciu jeho zdanlivej jasnosti
v mieste pozorovateľa, prípadne od iných merateľných parametrov (napríklad výšky nad obzorom
alebo uhlovej rýchlosti).

Počas riešenia projektu očakávame splnenie čiastkových úloh:

- organizácia observačnej expedície počas viditeľnosti niektorého z význačných meteorických rojov,
- súčasný záznam meteorického roja viacerými systémami (AMOS, fotografický záznam, vizuálni pozorovatelia),
- vzájomná korelácia záznamov z rôznych systémov a určenie limitnej magnitúdy systému AMOS.

Výsledné dáta by výrazne prispeli k našej schopnosti určiť skutočný počet meteorov pozorovateľných systémom AMOS
a následne stanoviť hodnoty toku a priestorovej hustoty meteoroidov v blízkosti dráhy Zeme.
V rámci projektu plánujeme prezentovať čiastkové výsledky na konferencii **IMC 2021**,
ktorá sa uskutoční v septembri 2021 v Hortobágy v Maďarsku.

### Referencie
