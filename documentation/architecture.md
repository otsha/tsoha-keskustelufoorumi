# Arkkitehtuuri

- [Projektin readme](https://github.com/otsha/tsoha-keskustelufoorumi/blob/master/README.md)
- [Projektin kuvaus](https://github.com/otsha/tsoha-keskustelufoorumi/blob/master/documentation/description.md)

## Sisällysluettelo
- [Sovelluksen rakenne](#sovelluksen-rakenne)
- [Käyttöliittymä](#käyttöliittymä)
- [Tietokanta](#tietokanta)
  - [Tietokannan kuvaus](#tietokannan-kuvaus)
    - [Tietokohteet](#tietokohteet)
  - [Tietokantakaavio](#tietokantakaavio)
  - [SQL-kyselyt](#sql-kyselyt)
    - [CREATE TABLE -lauseet](#create-table--lauseet)
    - [Yhteenvetokyselyt](#yhteenvetokyselyt)

## Sovelluksen rakenne

## Käyttöliittymä

## Tietokanta
### Tietokannan kuvaus
Sovelluksen käyttämä tietokannanhallintajärjestelmä riippuu sen käyttöympäristöstä. Jos sovellus suoritetaan paikallisesti, pyrkii se käyttämään SQLite-tietokantaa. Jos sovellus taas huomaa käynnistyneensä Herokussa (tarkistetaan ``application/__init__.py`` alussa), käyttää se postgreSQL-tietokantaa.

Tietokannassa on 4 taulua (Käyttäjä, Lanka, Vastaus ja Kategoria), joihin tallennetaan sovelluksen kannalta oleellinen data. Tietokannassa on myös yksi liitostaulu Käyttäjän ja Langan välillä, jolla pidetään kirjaa Langan luetuksi merkinneistä käyttäjistä.

#### Tietokohteet
* Käyttäjä
* Lanka (artikkeli, aloitusviesti)
* Vastaus (aina ja vain lankaan)
* Kategoria (aihe, tag, ylläpitäjän määrittelemä)

### Tietokantakaavio
*Todellisuudessa kaikilla tietokannan tauluilla on attribuutit date_created ja date_edited, sillä ne perustuvat yhteiseen Base-malliin (``application/models.py``), mutta koska niitä ei koskaan käytetä sovelluksen toiminnassa, on ne jätetty selkeyden vuoksi pois tietokantakaaviosta.*

![Projektin tietokantakaavio](https://yuml.me/7069ca1d.png)

[PDF](http://yuml.me/7069ca1d.pdf) | [yUML](http://yuml.me/edit/7069ca1d)
