# Projektin määrittelydokumentti

Kerrataan aluksi vielä projektin kuvaus.

## Kuvaus

*Harjoitustyössä tehdään keskustelufoorumi jonkin yhteisön, vaikkapa opiskelijajärjestön sisäiseen käyttöön. Käyttäjä voi lukea järjestelmän tallennettuja kirjoituksia ja lisätä tietokantaan uusia kirjoituksia, jotka voivat olla myös vastineita aiempiin kirjoituksiin. Kirjoituksia voi hakea kirjoittajan nimen tai aiheen tai artikkelin iän perusteella. Lukija voi seurata myös vastinepolkua. Oletusarvoisesti lukijalle näytetään kaikki tietty ikää tuoreemmat artikkelit varustettuna informaatiolla siitä onko lukija itse ja ovatko kaikki yhteisön jäsenet jo lukeneet artikkelin. Lukija identifioi aina itsensä ja artikkeleihin liitetään tieto henkilöistä jotka ovat lukeneet ne. Tämä tieto on kaikkien lukijoiden saatavissa.*

*Järjestelmän ylläpitäjällä on oma liittymä, jonka kautta hän ylläpitää järjestön käyttäjien jäsentietoja ja heidän kuulumistan eri ryhmiin, siivota kirjoituskantaa ja määrittellä aiheita, joiden perusteella kirjoituksia voi ryhmitellä.*

## Toimintoja

* Kirjautuminen
* Kirjoituksen lisääminen
* Kirjoitusten näyttäminen eri kriteerein
* Ryhmän jäsenen lisääminen, muokkaaminen ja poistaminen
* Vastineen laatiminen ja muokkaus
* Kirjoitusten poistaminen
* Aiheiden määrittely, muokkaus ja poisto

## Alustava tietokantakaavio
**Tietokohteet:**
* Ryhmä (käyttötarkoitus vielä pohdinnassa)
* Käyttäjä
* Lanka (artikkeli, aloitusviesti)
* Vastaus (aina ja vain lankaan)
* Kategoria (aihe, tag, ylläpitäjän määrittelemä)

![Projektin tietokantakaavio](https://yuml.me/504428db.png)

[PDF](https://yuml.me/504428db.pdf) | [yUML](https://yuml.me/edit/504428db)
