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

    - [ ] Sovellus näyttää kyseiselle päivälle kirjatut ateriat

    - [x] Mahdollisuus valita aterioita jo luoduista aterioista

    - [ ] Sovellus näyttää koosteen päivästä esim. alareunassa jossa näkyy päivän aterioiden kokonaiskalorit jaoteltuna makroravinteisiin ja käyttäjän asettama tavoite

    - [ ] Painike jolla siirrytään seuraavaan päivään, jolloin päivän tiedot tallentuvat pidemmän ajan koosteeseen

  - [ ] Käyttäjän tietoihin
    - [ ] Asetettu tavoite

  - [ ] Koosteeseen aiempien päivien tiedoista

  - [x] Tallennettujen aterioiden listaan

    - [x] Mahdollisuus lisätä ja poistaa aterioita

    - [x] Käyttäjä voi tallentaa sovellukseen aterioita, koostamalla tallentamistaan ruoka-aineista tai myöhemmin tuotteiden nimillä ja määrillä
  
  - [x] Käyttäjä voi lisätä ruoka-aineita
    
    - [x] Aluksi itse kirjaamalla ravintoarvot

    - [ ] Myöhemmin jos mahdollista niin tuotteen nimellä haetaan julkisesta tietokannasta tiedot

- [x] Käyttäjä voi kirjautua ulos sovelluksesta

