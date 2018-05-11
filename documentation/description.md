# Projektin määrittelydokumentti

*Tässä dokumentissa esitellään sovelluksen aihe, käyttötapaukset ja heikkoudet yleisellä tasolla. Tarkempi kuvaus sovelluksen toiminnasta löytyy [arkkitehtuuridokumentista](https://github.com/otsha/tsoha-keskustelufoorumi/blob/master/documentation/architecture.md).*

**Aihe:** Keskustelufoorumi

**Toteutus:** Python + Flask + SQLAlchemy + Jinja2

## Kuvaus

*Harjoitustyössä tehdään keskustelufoorumi jonkin yhteisön, vaikkapa opiskelijajärjestön sisäiseen käyttöön. Käyttäjä voi lukea järjestelmän tallennettuja kirjoituksia ja lisätä tietokantaan uusia kirjoituksia, jotka voivat olla myös vastineita aiempiin kirjoituksiin. Kirjoituksia voi hakea kirjoittajan nimen tai aiheen tai artikkelin iän perusteella. Lukija voi seurata myös vastinepolkua. Oletusarvoisesti lukijalle näytetään kaikki tietty ikää tuoreemmat artikkelit varustettuna informaatiolla siitä onko lukija itse ja ovatko kaikki yhteisön jäsenet jo lukeneet artikkelin. Lukija identifioi aina itsensä ja artikkeleihin liitetään tieto henkilöistä jotka ovat lukeneet ne. Tämä tieto on kaikkien lukijoiden saatavissa.*

*Järjestelmän ylläpitäjällä on oma liittymä, jonka kautta hän ylläpitää järjestön käyttäjien jäsentietoja ja heidän kuulumistan eri ryhmiin, siivota kirjoituskantaa ja määrittellä aiheita, joiden perusteella kirjoituksia voi ryhmitellä.*

## Toiminnot

### Rekisteröitymätön käyttäjä voi...
- Selata foorumin sisältöä vapaasti:
  - Lukea viestejä
  - Lukea vastauksia
  - Selata viestejä kategorioittain
  - Käyttää järjestys- ja rajoitustoimintoja
  - Hakea viestejä niiden nimen tai nimen osan perusteella
  - Tarkastella käyttäjäprofiileita
- Rekisteröityä uudeksi käyttäjäksi

### Rekisteröitynyt käyttäjä voi...
- Toteuttaa kaikki rekisteröitymättömälle käyttäjälle määritellyt toiminnot
- Kirjautua sisään/ulos
- Aloittaa uuden keskustelulangan haluamaansa kategoriaan
- Vastata muiden käyttäjien aloittamiin keskustelulankoihin
- Poistaa ja muokata omia kirjoituksiaan

### Admin-tason käyttäjä voi...
- Toteuttaa kaikki sekä rekisteröityneelle että rekisteröitymättömälle käyttäjälle määritellyt toiminnot
- Poistaa ja muokata muiden käyttäjien kirjoituksia
- Luoda ja poistaa kategorioita
- Muuttaa muiden rekisteröityneiden käyttäjien admin-tasoa
- Luopua admin-oikeuksistaan

*Tarkemmat ohjeet toimintojen käyttämiseen [käyttöohjeessa](https://github.com/otsha/tsoha-keskustelufoorumi/blob/master/documentation/usermanual.md).*

## Sovelluksen puutteet ja heikkoudet
- Ilmeisin puute sovelluksessa on kuvauksessa/tehtävänannossa määriteltyjen käyttäjäryhmien puute. Sovelluksessa on käytännössä vain kaksi varsinaista käyttäjäryhmää rekisteröitymättömien käyttäjien lisäksi: tavallinen käyttäjä ja admin-käyttäjä.

- Myös hakutoiminnallisuus on vajavainen, sillä se toimii vain lankojen otsikoiden perusteella.

- Ehdottomasti **vakavin** puute sovelluksessa on salasanojen tallentaminen tietokantaan plaintext-muodossa.

- Arkkitehtuurillisesti suurin heikkous on se, että sovellukseen on toteutettu viestilistausnäkymä käytännössä kolmesti: yksi Dashboard-näkymää varten ``application/templates/messages/list.html``, toinen kategorian sisältönäkymää varten ``àpplication/templates/categories/category.html`` ja kolmas haun tulosnäkymää varten ``application/templates/messages/search.html``. Vähän enemmällä ajankäytöllä (ja toki hieman monimutkaisemmalla koodilla) yhtä näkymää olisi voinut käyttää kaikkiin tarkoituksiin.

## Omat kokemukset
- Uuden ohjelmointikielen ja webkehitystyövälineiden oppiminen toi mukavaa haastetta projektiin, muttei ollut liian raskasta, ainakaan heti *Tietokantojen perusteiden* jälkeen. Itseasiassa rohkenisin jopa sanoa, että Flask ja Jinja ovat suoraviivaisempia käyttää kuin Spark ja Thymeleaf.
- Yllättäen omaksi suosikkiasiakseni kurssilla muodostui Bootstrap - ehkä juuri yksinkertaisuutensa (mutta myös muokattavuutensa) vuoksi.
