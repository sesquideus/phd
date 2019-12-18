## Návrh metódy riešenia projektu
Navrhovaný projekt nadväzuje na predchádzajúce výsledky v oblasti meteorickej astronómie.



[@ceplecha]


integrátor REBOUND [@rebound] a 




Projektom nadväzujeme na diplomovú prácu [@balaz2018], v ktorej sme sa zaoberali tokom meteoroidných
častíc v hornej atmosfére. Prirodzeným ďalším krokom je rozšírenie zamerania práce na pôvod a vývoj týchto telies,
teda na obdobie od ich uvoľnenia z materského telesa až po zánik v zemskej atmosfére.

Základom metódy je numerická $N$-body simulácia s využitím masívnej paralelizácie pomocou grafického procesora (GPU).
V\ simulácii budeme vytvárať jednotlivé častice pri známych materských telesách meteoroidov
a následne numerickou integráciou pohybových rovníc určíme ich budúcu polohu.
Celkové silové pôsobenie je dané najmä gravitačným pôsobením Slnka ako centrálneho telesa,
rušiacimi gravitačnými vplyvmi planét a krátkodobo aj pôsobením materského objektu.
Pre častice s veľmi malými rozmermi sú dôležité aj negravitačné vplyvy, najmä
tlak slnečného žiarenia a Poyntingov-Robertsonov efekt.

Ak počas integrácie dôjde ku kolízii niektorej z častíc so Zemou, daná častica je označená ako
spozorovaná. Sumárny štatistický súbor všetkých takýchto častíc je po aplikácii výberových efektov
možné porovnať s pozemskými pozorovaniami a určiť zhodu s experimentálnymi dátami. Variáciou parametrov
simulácie a minimalizáciou odchýlok sme schopní určiť skutočnú distribúciu a pôvodnú dráhu telies.
Opätovné spustenie simulácie s optimálnymi hodnotami parametrov spolu so znalosťou dráhy skutočného
materského telesa nám umožnia identifikovať jednotlivé prúdy častíc, predpovedať
aktivitu zodpovedajúcich meteorických rojov a určiť tok a distribúciu častíc v danej oblasti
Slnečnej sústavy.

### Referencie
