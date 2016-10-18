a) Hva er pseudokode og når får vi bruk for det? Lag en pseudokode av din egen kode, positivtTall(N), fra Øving 2 - Klassifisering av tall c).

Mer folkelig beskrivelse av en algoritme. Man kan beskrive de forskjellige stegene i en algoritme, men med en mer naturlig tone, uten å bruke programmeringssyntaks. Skrevet for å bli lest av mennesker, og ikke en datamaskin. Man vil altså utelukke modul-importeringer, og bare holde seg til å beskrive selve flyten til algoritmen. Bruksområder: Beskrive algoritmer til andre folk (som f.eks skal implementere den i et eller annet språk), forklare egen kode slik at man lettere kan forstå den i framtiden...

def isPositive(num):
    return num > 0

Definerer en funksjon med navnet isPositive som tar i mot et tall
  Hvis tallet er større enn 0:
    Returner True
  Hvis tallet ikke er større enn 0:
    Returner False

b) Hva er et flytdiagram?

En algoritme representert med forskjellige bokser som representerer et steg, bundet sammen med piler som viser rekkefølgen de skal utføres i og hvordan prosessen forgrener seg..

c) Hva er debugging?

Kunsten å finne feil i program for å så fikse dem.

d) Hva er forsjellen på et høynivå- og et lavnivå-programmeringsspråk?

Forskjellige nivåer av abstraksjon fra ren maskinkode. På bunnen har vi ren maskinkode, over der har man f.eks Assembly, så programmeringsspråk som C, som er lavnivå-programmeringsspråk. Deretter har man mange høytnivå-språk som Python, som lar deg fokusere mindre på det system-relaterte, da de håndterer ting som minne-allokering og garbage-collection automatisk, og tilbyr mange "bibliotek" som hjelper deg med utviklingen din.

e) Forklar de fem stegene i Hente/Utføre-kretsen.

Hent instruksjonen fra minnet

Dekod instruksjonen / finn ut hva instruksjonen skal gjøre med parametrene vi snart henter

Hent parametre som skal mates til instruksjonen

Utfør instruksjonen med parametrene

Returner resultatet fra evalueringen av funksjoen

f) Hva gjør programtelleren (Program Counter)?

I kontrolldelen av maskinen lagres adressen i minnet til den neste instruksjonen. Man hopper altså videre til neste byte i minnet med at programtelleren øker med 1 byte / 4 bits.
