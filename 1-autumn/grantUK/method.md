## Návrh metódy riešenia projektu
Projekt nadväzuje na našu diplomovú prácu [@balaz2018] a rozširuje výsledky

Výsledky sú priamo porovnateľné s hodnotami získanými inými metódami, napríklad
vizuálnymi pozorovaniami vykonanými skupinou pozorovateľov, priamou
redukciou dát z kamerových systémov (AMOS [@zigo2013] a CILBO [@koschny2013])
alebo inými metódami [@blaauw2016].
Špeciálnu pozornosť venujeme porovnaniu s analýzami konkrétnych pozorovacích nocí,
publikovanými napríklad portálom `MeteorFlux.io` [@meteorflux].



V nasledujúcej fáze navrhujeme metódu, ktorou je možné získané výsledky rozšíriť na oblasť vnútornej Slnečnej sústavy,
resp. oblasť dráhy Zeme, keďže pozemské pozorovanie meteorov neumožňujú vykonávať priame merania
vo vzdialenejších oblastiach. Dáta je však možné priamo extrapolovať do blízkeho okolia.
Základom metódy je numerická $N$-body simulácia s využitím masívnej paralelizácie pomocou GPU.

Simulácia vytvára jednotlivé častice pri známych materských telesách meteoroidov
a následne numerickou integráciu pohybových rovníc určuje ich budúcu polohu.
Mierne odlišnosti počiatočných rýchlostí, gravitačné perturbácie pochádzajúce planét
a negravitačné efekty pôsobiace na častice spôsobujú, že dráhy častíc sa na dlhých časových škálach
líšia, až vytvoria široký prstenec okolo orbity pôvodného materského telesa.

Celkové silové pôsobenie je dané najmä gravitačným pôsobením Slnka ako centrálneho telesa,
rušiacimi gravitačnými vplyvmi planét a krátkodobo aj pôsobením materského objektu.
Pre častice s veľmi malými rozmermi sú dôležité aj negravitačné vplyvy, najmä
tlak slnečného žiarenia a Poynting-Robertsonov efekt [@cite-something].
Jednotlivé častice sú nezávislé a ich vzájomné silové pôsobenie môžeme úplne zanedbať.
Pri využití masívnej paralelizácie pomocou GPU očakávame podstatné zvýšenie výpočtového výkonu
na úroveň miliárd integračných krokov za sekundu, čo umožní simulovať milióny častíc [@nvidia2008].
Vysoký počet simulovaných častíc je dôležitý, keďže k zrážkam so Zemou dochádza pomerne zriedkavo,
kým pre účely štatistického vyhodnotenia súboru potrebujeme získať dostatočne početnú populáciu.

Ak počas integrácie dôjde ku kolízii niektorej z častíc so Zemou, daná častica je označená ako
spozorovaná. Sumárny štatistický súbor všetkých týchto častíc je po aplikácii výberových efektov
možné porovnať s pozemskými pozorovaniami a určiť zhodu s experimentálnymi dátami. Variáciou parametrov
simulácie a minimalizáciou odchýlok sme schopní určiť skutočnú distribúciu a pôvodnú dráhu telies.

### Referencie
