# Vaatimusmäärittely

## Sovelluksen tarkoitus
Sovellus toimii ruokapäiväkirjana auttaen käyttäjää esimerkiksi diettaamisen kanssa. Sovellukseen voi lisätä päiväkohtaisesti aterioita ja se kokoaa niistä koosteen sekä vertaa sitä käyttäjän asettamaan tavoitteeseen. Sovellusta voi käyttää useammalla eri käyttäjällä ja jokaisella on oma yksityinen ruokapäiväkirjansa.


## Käyttäjät
Ainakin alkuvaiheessa sovelluksella on vain normaali käyttäjärooli, mutta myöhemmin saattaa nousta tarve useammalle roolille kuten pääkäyttäjä, jolla on enemmän oikeuksia.


## Suunnitellut toiminnallisuudet

### Ennen kirjautumista
- [x] Sovelluksen käyttäjä pystyy luoda uuden käyttäjän sovellukseen

  - [ ] Tarkastus että salasana on riittävä ja käyttäjätunnus ei käytössä

  - [ ] Käyttäjä voi asettaa tavoitteen itsellensä sekä mahdollisesti muita tietoja

- [x] Käyttäjä voi kirjautua sovellukseen olemassa olevalla tunnuksella

  - [x] Tarkastus että salasana vastaa tunnukseen


### Kirjautuneena
- [x] Sovellus näyttää valikon josta voi navigoida:

  - [x] Nykyiseen päivään

    - [ ] Sovellus näyttää kyseiselle päivälle tallennetut ateriat

    - [ ] Mahdollisuus lisätä uusi ateria
      - [ ] Kokonaan uusi ateria tai valita tallennetuista aterioista

    - [ ] Sovellus näyttää koosteen päivästä esim. alareunassa jossa näkyy päivän aterioiden kokonaiskalorit jaoteltuna makroravinteisiin ja käyttäjän asettama tavoite

    - [ ] Painike jolla siirrytään seuraavaan päivään, jolloin päivän tiedot tallentuvat pidemmän ajan koosteeseen

  - [ ] Käyttäjän tietoihin
    - [ ] Asetettu tavoite

  - [ ] Koosteeseen aiempien päivien tiedoista

  - [ ] Tallennettujen aterioiden listaan

    - [ ] Mahdollisuus lisätä ja poistaa aterioita

    - [ ] Käyttäjä voi tallentaa sovellukseen aterioita, ruoka-aine kohtaisesti valitsemillaan määrillä ja sovellus hakee niiden tiedot ja koostaa siitä yhden aterian jonka käyttäjä voi nimetä ja sen voi lisätä sen jälkeen suoraan listasta

- [x] Käyttäjä voi kirjautua ulos sovelluksesta

