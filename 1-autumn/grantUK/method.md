## Návrh metódy riešenia projektu
Projekt nadväzuje na našu diplomovú prácu [@balaz2018] a rozširuje platnosť získaných výsledkov
na všetky hlavné zdroje mete



V nasledujúcej fáze navrhujeme metódu, ktorou je možné získané výsledky rozšíriť na oblasť vnútornej Slnečnej sústavy,
resp. oblasť dráhy Zeme, keďže pozemské pozorovanie meteorov neumožňujú vykonávať priame merania
vo vzdialenejších oblastiach. Dáta je však možné priamo extrapolovať do blízkeho okolia.
Základom metódy je numerická $N$-body simulácia s využitím masívnej paralelizácie pomocou GPU.

Simulácia vytvára jednotlivé častice pri známych materských telesách meteoroidov
a následne numerickou integráciu pohybových rovníc určuje ich budúcu polohu.

Celkové silové pôsobenie je dané najmä gravitačným pôsobením Slnka ako centrálneho telesa,
rušiacimi gravitačnými vplyvmi planét a krátkodobo aj pôsobením materského objektu.
Pre častice s veľmi malými rozmermi sú dôležité aj negravitačné vplyvy, najmä
tlak slnečného žiarenia a Poynting-Robertsonov efekt.
Jednotlivé častice sú nezávislé a ich vzájomné silové pôsobenie môžeme úplne zanedbať.
Pri využití masívnej paralelizácie pomocou GPU očakávame podstatné zvýšenie výpočtového výkonu
na úroveň miliárd integračných krokov za sekundu, čo umožní simulovať milióny častíc [@nguyen2007].
Vysoký počet simulovaných častíc je dôležitý, keďže k zrážkam so Zemou dochádza pomerne zriedkavo,
kým pre účely štatistického vyhodnotenia súboru potrebujeme získať dostatočne početnú populáciu.

Ak počas integrácie dôjde ku kolízii niektorej z častíc so Zemou, daná častica je označená ako
spozorovaná. Sumárny štatistický súbor všetkých takýchto častíc je po aplikácii výberových efektov
možné porovnať s pozemskými pozorovaniami a určiť zhodu s experimentálnymi dátami. Variáciou parametrov
simulácie a minimalizáciou odchýlok sme schopní určiť skutočnú distribúciu a pôvodnú dráhu telies.
Opävotné spustenie simulácie s optimálnymi hodnotami parametrov spolu so znalosťou dráhy skutočného
materského telesa nám umožnia identifikovať prúdy častíc a predpovedať aktivitu meteorických rojov.

### Referencie
