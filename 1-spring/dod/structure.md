## Introduction
-   čo to je
    -   sieť kamier
        -   celooblohová kamera
        -   TLE, meteory, satelity, zánik nosných telies, čokoľvek
        -   poloha staníc, 4+2+2+2  (+2+2)
    -   ukázať fotky, GE
-   ako to funguje
    -   fisheye šošovka
    -   zosilňovač jasu obrazu, military grade
    -   20 FPS / 1600×1200 pixelov (\pm) 180×140°
    -   vnútri je navyše PC (žiaľ Windows)
    -   detekcia
        -   UFO
        -   Kvant AMOS
    -   posielanie dát
        -   redukcia dát
        -   databáza meteorov
-   načo to je
    -   detekcia meteorov z jednej stanice
    -   dvojstaničné
        -   heliocentrické dráhy
        -   určenie meteorických rojov + sporadické pozadie
        -   tok častíc + ohrozenie staníc
        -   pády meteoritov
    -   spektrálne kamery
        -   chemické zloženie
        -   napríklad Na poor blízko Slnka
        
## ASMODEUS
-   systém nie je dokonalý (má od toho riadne ďaleko)
    -   zďaleka nevidieť všetko
    -   potrebujeme zistiť detekčné parametre systému
        -   limitná magnitúda
        -   uhlová závislosť (výška nad obzorom)
        -   uhlová rýchlosť, dwell time
-   simulácia
    -   vytvoríme meteory
    -   simulujeme vstup do atmosféry
        -   zaznamenáme vlastnosti telies
    -   vygenerujeme sighting
        -   zredukujeme na body
        -   aplikujeme selekčné efekty (bias)
        -   porovnáme histogramy
    -   opakujeme až do nájdenia najlepšej zhody
-   výsledky
    -   celkový tok
    -   potrebujeme viac dát a lepšie -> databáza