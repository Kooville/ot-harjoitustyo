# Food diary

Sovellus tulee toimimaan ruokapäiväkirjana, johon käyttäjä pystyy merkitä päivän aikana syömänsä ateriat ja sovellus koostaa niistä olennaiset tiedot yhteenvetoon. Sovellukseen voi lisätä ruoka-aineita listaamalla ravinto-aineet ja koostaa niistä aterioita. Lisäksi sovellus tulee pitämään sisällään yhteenvedon aiemmista päivistä.

## Dokumentaatio
[Vaatimusmäärittely](https://github.com/Kooville/ot-harjoitustyo/blob/main/food-app/dokumentaatio/vaatimusmaarittely.md)

[Työaikakirjanpito](https://github.com/Kooville/ot-harjoitustyo/blob/main/food-app/dokumentaatio/tyoaikakirjanpito.md)

[Changelog](https://github.com/Kooville/ot-harjoitustyo/blob/main/food-app/dokumentaatio/changelog.md)

[Arkkitehtuurikuvaus](https://github.com/Kooville/ot-harjoitustyo/blob/main/food-app/dokumentaatio/arkkitehtuuri.md)

[Viikon 5 release](https://github.com/Kooville/ot-harjoitustyo/releases/tag/viikko5)

## Asennus

1. Lataa repositorio omalle tietokoneellesi

2. Asenna riippuvuudet siirtymällä repositorioon ja suorittamalla komennon:

```bash
poetry install
```

3. Alusta tietokanta komennolla:

```bash
poetry run invoke build
```

4. Käynnistä sovellus komennolla:

```bash
poetry run invoke start
```

Muita suoritettavia komentoja

- Testien suorittaminen
```bash
poetry run invoke test
```

- Pylint tarkistus
```bash
poetry run invoke lint
```

- Testikattavuusraportti
```bash
poetry run invoke coverage-report
```
