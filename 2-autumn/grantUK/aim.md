## Charakteristika vedeckých cieľov projektu
Meteoroidy, čiže malé kamenné alebo železné telieska obiehajúce okolo Slnka,
sú jedným z najcennejších zdrojov informácií o pôvode a vývoji Slnečnej sústavy.
Za meteoroidy považujeme telesá s rozmermi v rozpätí \SI{30}{\micro\metre} až
\SI{1}{\metre} [@imo-meteor]; pričom väčšie telesá nazývame asteroidmi
a pri menších telesách hovoríme o medziplanetárnom prachu.
Pri súčasnom stave techniky nie je možné meteoroidy možné pozorovať priamo
v otvorenom medziplanetárnom priestore. Naše znalosti o nich pochádzajú najmä zo sledovania
ich interakcie s vrchnými vrstvami atmosféry Zeme. Ak dráha meteoroidu križuje dráhu Zeme
a teleso vstúpi do zemskej atmosféry, jeho kinetická energia je dostatočná na roztavenie a ionizáciu materiálu.
Vznikajúcu svetelnú stopu následne môžeme pozorovať ako meteor.

Zdanlivý pohyb meteorov je oproti ostatným nebeským telesám veľmi rýchly.
Pravdepodobne aj preto boli meteory historicky považované skôr za meteorologický, než astronomický úkaz,
a ich kozmický pôvod bol definitívne potvrdený až v roku 1798 [@czegka2000].
Pozorovaním meteorov zo zemského povrchu je možné zistiť, že sú často združené do *meteorických rojov*,
teda zoskupení telies s podobnými geocentrickými dráhami a rýchlosťami.
Projekcia na oblohu vytvára ilúziu bodového zdroja, ktorý nazývame *radiantom*.

Dominantným zdrojom meteoroidov sú malé telesá Slnečnej sústavy, najmä kométy
a blízkozemské asteroidy. Tieto telesá sa pri priblíženiach k Slnku zahrievajú
a následne uvoľňujú drobné úlomky, prípadne fragmentujú pri vzájomných zrážkach.
Mierne odlišnosti počiatočných rýchlostí telies, gravitačné perturbácie pochádzajúce od planét
a rôzne negravitačné efekty pôsobiace na častice spôsobujú, že ich dráhy sa počas dlhých časových období
pomaly menia a diverzifikujú. Na škálach stoviek až tisícov rokov vytvoria široký prstenec
okolo pôvodnej orbity svojho materského telesa. Na ešte dlhších škálach sa prstence rozpadajú
a prispievajú do *sporadického pozadia*, teda zdroja rozptýlených
meteoroidov na zdanlivo náhodných dráhach [@jenniskens1998].

Meteoroidy spravidla zanikajú vo vrchných vrstvách atmosféry. Ojedinele môžu byť fragmenty zabrzdené
odporom atmosféry bez roztavenia a následne dopadnú na zemský povrch ako meteority.
Vzhľadom na ich nízku dopadovú rýchlosť a vzácnosť však nepredstavujú výrazné nebezpečentvo pre ľudské aktivity.
Mimo zemskej atmosféry však vážne ohrozujú misie s ľudskou posádkou ako aj komerčné satelity.
Potreba presných dát o priestorovej koncentrácii a toku meteoroidných častíc v okolí Zeme a jej dráhy sa bude s narastajúcim vedeckým a komerčným využívaním
kozmického priestoru neustále zvyšovať. Detailné poznanie dráhových charakteristík, početnosti a distribúcie veľkostí
častí je dôležité aj pre zhodnotenie ohrozenia povrchu Zeme. Objekty s rozmermi viac ako 10 metrov predstavujú nebezpečenstvo
a majú potenciál spôsobiť značné škody, od lokálnych materiálnych škôd až po katastrofy globálneho charakteru.

Primárnym cieľom projektu je vytvorenie detailného modelu priestorového rozloženia malých častíc vo vnútornej Slnečnej sústave.
Model popisuje hustotu častíc v závislosti od šiestich orbitálnych elementov v heliocentrickej sústave,
doplnenú o informácie o populačnom indexe $s$ v konkrétnom mieste fázového priestoru
a spektrálnom type, resp. chemickom zložení meteoroidov v tomto priestore.

Pre porovnanie modelu s observačnými dátami je nutné model zredukovať na zemský povrch,
čiže určiť množstvo častíc, ktoré vstúpia do atmosféry v konkrétnom čase a mieste a teda je možné ich detegovať.
Po redukcii získame vedľajší produkt projektu, ktorým je časovo-priestorová mapa meteorickej aktivity na oblohe
pre ľubovoľné miesto na zemskom povrchu. Následne bude porovnávaním simulácie s reálnymi observačnými dátami
a dolaďovaním jej parametrov až do dosiahnutia optimálnej zhody možné modelovať
skutočnú populáciu meteoroidov v okolí Zeme.
Primárnym zdrojom observačných dát na našom pracovisku sú kamery systému AMOS (All-sky Meteor Orbit System),
ktorý bol vyvinutý a je prevádzkovaný Oddelením astronómie a astrofyziky KAFZM FMFI UK [@zigo2013; @toth2015].

Počas riešenia projektu očakávame splnenie nasledujúcich čiastkových úloh:

- implementácia $N$-body simulácie meteoroidov,
- zostrojenie modelu populácie meteoroidov v okolí Zeme,
- vývoj metód redukciu modelu na zemskú oblohu,
- porovnanie výsledkov s inými modelmi, napríklad [@vaubaillon+2005].

Simuláciu by malo byť možné prípadne integrovať do softvérového balíka REBOUND
a následne sprístupniť pre odbornú verejnosť v oblasti výskumu dynamiky malých častíc.

V rámci projektu plánujeme prezentovať čiastkové výsledky na konferencii **IMC 2020**,
ktorá sa uskutoční v septembri 2020 v Hortobágy v Maďarsku.

### Referencie
