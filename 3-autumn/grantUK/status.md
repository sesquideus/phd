## Rozbor aktuálneho stavu riešenia témy projektu
Najjednoduchším modelom pre určenie pozorovateľnosti astronomických
objektov je model s konštantnou *limitnou magnitúdou* $m_0$.
Pozorovateľ (kamera, fotoaparát, ľudské oko...) je v ňom schopný zaznamenať všetky bodové objekty
vo svojom zornom poli, ktorých jasnosť je aspoň $m_0$, a žiadne bodové objekty s nižšou jasnosťou.
V prípade celooblohovej meteorovej kamery teda za detegované považujeme všetky geometricky
viditeľné meteory, ktorých zdanlivá magnitúda je najviac $m_0$.

Komplexnejším modelom je stochastický model, v ktorom je každý meteor detegovaný
s určitou pravdepodobnosťou, ktorá je funkciou jeho zdanlivej magnitúdy, prípadne ďalších
merateľných vlastností.
Všeobecný tvar tejto funkcie nie je vopred určený, z fyzikálnej teórie merania
je však možné učiniť niekoľko predpokladov. Obvykle uvažujeme funkcie klesajúce,
s oborom hodnôt $\left[0; 1\right]$:

- pravdepodobnosť detekcie jasnejšieho meteoru je všeobecne vyššia, ako menej jasného;
- pravdepodobnosť detekcie veľmi jasného meteoru je blízka 1;
- detekcia veľmi málo jasného meteoru je nulová.

Vhodnou triedou takýchto funkcií sú napríklad exponenciálne sigmoidy
$F(x; x_0, \omega) \equiv \frac{1}{1 + \mathrm{exp}\ \omega \left(x - x_0\right)}$ [@jedicke+1997].
Limitná magnitúda tu zodpovedá jasnosti, pre ktorú je pravdepodobnosť detekcie 1/2,
parameter $\omega$ popisuje rýchlosť poklesu tejto pravdepodobnosti so znižujúcou sa jasnosťou.
Degenerovaný prípad $\omega \to 0$ potom zodpovedá jednoduchému modelu s konštantnou limitnou magnitúdou.

Pre systém AMOS je známa kalibrácia pre jasnejšiu časť spektra ($m \leq -5$) podľa [@zsilinszka2018].
Distribúcia hviezdnych veľkostí meteorov je však približne mocninná a teda obsahuje výrazne
viac meteorov s nižími jasnosťami, ktoré touto publikáciou nie sú pokryté.
Predbežné dáta získané simuláciami [@balaz-thesis] naznačujú,
že skutočná limitná magnitúda systému AMOS je približne $0^{\mathrm{m}}$.

### Referencie
