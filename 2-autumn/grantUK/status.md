## Rozbor aktuálneho stavu riešenia témy projektu
Vzhľadom na dokázateľnú nemožnosť analytického vyriešenia problému $N$ telies
je nutné všetky výpočty vykonávať numericky s diskrétnymi časovými krokmi.
V súčasnosti sa na numerickú integráciu dráh používajú predovšetkým symplektické integrátory
ako Verletov, SABA, WM a pod.; prípadne integrátory vysokých rádov s adaptívnou
veľkosťou kroku (IAS15) [@rein+ias15].

Vhodným frameworkom na výpočty je softvérový balík REBOUND [@rein+rebound],
ktorý v súčasností tvorí de facto štandard v oblasti simulácií gravitačných interakcií viacerých telies.
Aktuálne však nepodporuje akceleráciu pomocou grafickej výpočtovej jednotky (GPU),
ktorá by umožnila masívne paralelné výpočty polôh vzájomne neinteragujúcich testovacích telies.

Pri redukcii dát z tradičných vizuálnych alebo prístrojových pozorovacích metód
sa zatiaľ obvykle neuvažujú výberové efekty (_selection bias_).
Do zaznamenaných pozorovaní vstupuje rad prirodzených aj inštrumentálnych vplyvov, ktoré skresľujú výslednú štatistickú vzorku.
Automatické videostanice, fotografické prístroje aj vizuálne pozorovania prirodzene
preferujú meteory s väčšou zdanlivou jasnosťou a dĺžkou dráhy a menšou vzdialenosťou od zenitu.
Tieto efekty je potrebné zmerať a vyvinúť procedúry na ich odstránenie. Ďalšie parametre
populácie je možné určiť až po oprave štatistického súboru o výberové efekty.

V súčasnosti disponujeme vhodnými nástrojmi na simuláciu a analýzu virtuálnych
populácií meteorov v zemskej atmosfére [@balaz+2020] aj všeobecnými metódami
na numerickú integráciu dráh. Hlavnými chýbajúcimi článkami sú prispôsobenie integračných metód
pre veľké množstvo vzájomne neinteragujúcich častíc a robustná metóda na redukciu
dráh medziplanetárnych častíc do zemskej atmosféry.

### Referencie
