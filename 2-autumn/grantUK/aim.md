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
teda zoskupení telies s podobnými geocentrickými dráhami. Projekcia na oblohu vytvára ilúziu bodového zdroja, čiže *radiantu*.

Dominantným zdrojom meteoroidov sú malé telesá Slnečnej sústavy, najmä kométy
a blízkozemské asteroidy, ktoré pri preletoch blízko Slnka uvoľňujú drobné telieska,
prípadne fragmentujú pri vzájomných zrážkach.
Mierne odlišnosti počiatočných rýchlostí telies, gravitačné perturbácie pochádzajúce od planét
a negravitačné efekty pôsobiace na častice spôsobujú, že ich dráhy sa na dlhých časových škálach
pomaly menia a diverzifikujú. Na škálach stoviek až tisícov rokov vytvoria široký prstenec
okolo pôvodnej orbity svojho materského telesa. Na ešte dlhších škálach sa prstence rozpadajú
a prispievajú do *sporadického pozadia*, teda zdroja rozptýlených
meteoroidov na zdanlivo náhodných dráhach [@jenniskens1998].

Mimo zemskej atmosféry tieto telieska predstavujú vážne nebezpečenstvo pre ľudské misie a komerčné satelity.
Potreba presných dát o priestorovej koncentrácii a toku meteoroidných častíc v okolí Zeme a jej dráhy sa bude s narastajúcim vedeckým a komerčným využívaním
kozmického priestoru neustále zvyšovať. Detailné poznanie dráhových charakteristík, početnosti a distribúcie veľkostí
častí je dôležité aj pre zhodnotenie ohrozenia povrchu Zeme. Objekty s rozmermi viac ako 10 metrov predstavujú nebezpečenstvo
a majú potenciál spôsobiť značné škody, od lokálnych materiálnych škôd až po katastrofy globálneho charakteru.

V práci sa zameriame na pôvod a dynamický vývoj prúdov meteoroidov od ich vzniku až po zánik v\ atmosfére.
Cieľom projektu je vytvoriť ucelený model ich priestorového rozloženia vo vnútornej Slnečnej sústave.
Vhodným nástrojom na výskum dráhovej dynamiky a evolučných ciest meteorických rojov sú numerické $N$-body simulácie.
Výsledok simulácie je možné štatisticky porovnať s\ observačnými dátami a následne optimalizačnými metódami nájsť
najlepšiu možnú zhodu. Takto získaná virtuálna populácia dobre popisuje skutočné rozloženie častíc.
Primárnym zdrojom observačných dát na našom pracovisku sú kamery systému AMOS (All-sky Meteor Orbit System),
ktorý bol vyvinutý a je prevádzkovaný Oddelením astronómie a astrofyziky KAFZM FMFI UK [@zigo2013; @toth2015].
Počas riešenia projektu očakávame splnenie nasledujúcich úloh:

- návrh $N$-body simulácie s využitím masívnej paralelizácie pomocou grafického procesora (GPU),
- implementácia simulácie v jazyku Python alebo C++,
- vývoj porovnávacích algoritmov a optimalizačných procedúr,
- porovnanie výsledkov s inými modelmi, napríklad [@ryabova2013].

V rámci projektu sa taktiež plánujeme zúčastniť na konferencii **Meteoroids 2019**, ktorú
v tomto roku organizuje Univerzita Komenského v Bratislave, a prezentovať dovtedy získané výsledky
vo forme príspevku alebo postera; prípadne tiež na konferencii **IMC 2019** v Bollmannsruh v Nemecku.

### Referencie
