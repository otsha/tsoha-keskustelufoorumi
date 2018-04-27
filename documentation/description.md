# Projektin määrittelydokumentti

Kerrataan aluksi vielä projektin kuvaus.

## Kuvaus

*Harjoitustyössä tehdään keskustelufoorumi jonkin yhteisön, vaikkapa opiskelijajärjestön sisäiseen käyttöön. Käyttäjä voi lukea järjestelmän tallennettuja kirjoituksia ja lisätä tietokantaan uusia kirjoituksia, jotka voivat olla myös vastineita aiempiin kirjoituksiin. Kirjoituksia voi hakea kirjoittajan nimen tai aiheen tai artikkelin iän perusteella. Lukija voi seurata myös vastinepolkua. Oletusarvoisesti lukijalle näytetään kaikki tietty ikää tuoreemmat artikkelit varustettuna informaatiolla siitä onko lukija itse ja ovatko kaikki yhteisön jäsenet jo lukeneet artikkelin. Lukija identifioi aina itsensä ja artikkeleihin liitetään tieto henkilöistä jotka ovat lukeneet ne. Tämä tieto on kaikkien lukijoiden saatavissa.*

*Järjestelmän ylläpitäjällä on oma liittymä, jonka kautta hän ylläpitää järjestön käyttäjien jäsentietoja ja heidän kuulumistan eri ryhmiin, siivota kirjoituskantaa ja määrittellä aiheita, joiden perusteella kirjoituksia voi ryhmitellä.*

## Toimintoja

- [x] Kirjautuminen
- [x] Kirjoituksen lisääminen
  - [x] Kirjoituksen kategorian määrittely
- [x] Kirjoitusten poistaminen
- [x] Kirjoitusten näyttäminen eri kriteerein
  - [x] Kategorioittain
  - [x] Järjestäminen päiväyksen tai otsikon mukaan (toistaiseksi vain kategorioissa)
  - [x] Hakutoiminnallisuus (viestien otsikoista)
- [x] Vastineen laatiminen ja muokkaus
  - [x] Laatiminen ja poisto
  - [x] Muokkaus
- [x] Langan luetuksi merkkaaminen
- [x] Langan lukeneiden käyttääjien listaaminen
- [x] Käyttäjän profiilin tarkastelu
  - [x] Käyttäjän aloittamien lankojen listaaminen
  - [x] Käyttäjän admin-statuksen muuttaminen
- [x] Kategorioiden määrittely ja poisto
- [ ] Ryhmän jäsenen lisääminen, muokkaaminen ja poistaminen

## Tietokanta
### Kuvaus
*Tietokannassa on 4 taulua (Käyttäjä, Lanka, Vastaus ja Kategoria), joihin tallennetaan sovelluksen kannalta oleellinen data. Tietokannassa on myös yksi liitostaulu Käyttäjän ja Langan välillä, jolla pidetään kirjaa Langan luetuksi merkinneistä käyttäjistä.*

#### Tietokohteet
* Käyttäjä
* Lanka (artikkeli, aloitusviesti)
* Vastaus (aina ja vain lankaan)
* Kategoria (aihe, tag, ylläpitäjän määrittelemä)

### Tietokantakaavio
*Todellisuudessa kaikilla tietokannan tauluilla on attribuutit date_created ja date_edited, mutta koska niitä ei koskaan käytetä sovelluksen toiminnassa, on ne jätetty selkeyden vuoksi pois tietokantakaaviosta.*

![Projektin tietokantakaavio](https://yuml.me/7069ca1d.png)

[PDF](http://yuml.me/7069ca1d.pdf) | [yUML](http://yuml.me/edit/7069ca1d)
