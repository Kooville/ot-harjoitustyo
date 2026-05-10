# Vaatimusmäärittely

## Sovelluksen tarkoitus
Sovellus toimii ruokapäiväkirjana auttaen käyttäjää esimerkiksi diettaamisen kanssa. Sovellukseen voi lisätä päiväkohtaisesti aterioita ja se kokoaa niistä koosteen sekä vertaa sitä käyttäjän asettamaan tavoitteeseen. Sovellus helpottaa aterioiden seuraamista ja kirjanpitoa. Sovellusta voi käyttää useammalla eri käyttäjällä ja jokaisella on oma yksityinen ruokapäiväkirjansa.


## Käyttäjät
Sovelluksella on vain normaali käyttäjärooli.


## Toiminnallisuudet

### Ennen kirjautumista
- [x] Sovelluksen käyttäjä pystyy luoda uuden käyttäjän sovellukseen

  - [x] Tarkastus että käyttäjätunnus ei käytössä

- [x] Käyttäjä voi kirjautua sovellukseen olemassa olevalla tunnuksella

  - [x] Tarkastus että salasana vastaa tunnukseen


### Kirjautuneena
- [x] Sovellus näyttää valikon josta voi navigoida:

  - [x] Nykyiseen päivään

    - [x] Sovellus näyttää kyseiselle päivälle kirjatut ateriat

    - [x] Mahdollisuus valita aterioita jo luoduista aterioista

    - [x] Sovellus näyttää koosteen päivästä esim. alareunassa jossa näkyy päivän aterioiden kokonaiskalorit jaoteltuna makroravinteisiin ja käyttäjän asettama tavoite

  - [x] Käyttäjän tietoihin

    - [x] Asetettu tavoite

    - [x] Käyttäjä voi asettaa tavoitteen itsellensä sekä mahdollisesti muita tietoja

  - [x] Tallennettujen aterioiden listaan

    - [x] Mahdollisuus lisätä ja poistaa aterioita

    - [x] Käyttäjä voi tallentaa sovellukseen aterioita, koostamalla tallentamistaan ruoka-aineista tai myöhemmin tuotteiden nimillä ja määrillä
  
  - [x] Käyttäjä voi lisätä ruoka-aineita
    
    - [x] Aluksi itse kirjaamalla ravintoarvot

- [x] Käyttäjä voi kirjautua ulos sovelluksesta

## Jatkokehitysideoita
 - Mahdollisuus tarkastella menneitä päiviä tai koostetta niistä
 - Ruoka-aineiden ravintoarvojen hakeminen julkisesta tietokannasta tuotteen nimellä
