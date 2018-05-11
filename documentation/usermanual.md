# Käyttöohje

## Sisällysluettelo
- [Käyttöönotto](#sovelluksen-käyttöönotto)
  - [Suorittaminen paikallisesti](#suorittaminen-paikallisesti)
    - [Ensimmäiset admin-tunnukset](#ensimmäiset-admin-tunnukset)
- [Käyttäjät](#käyttäjät)
  - [Rekisteröityminen ja kirjautuminen](#rekisteröityminen-ja-kirjautuminen)
    - [Uuden käyttäjätunnuksen luominen](#uuden-käyttäjätunnuksen-luominen)
    - [Sisäänkirjautuminen](#sisäänkirjautuminen)
  - [Käyttäjäprofiilien tarkastelu](#käyttäjäprofiilien-tarkastelu)
  - [Admin-oikeudet](#admin-oikeudet)
- [Kirjoitukset](#kirjoitukset)
  - [Uuden keskustelulangan avaaminen](#uuden-keskustelulangan-avaaminen)
  - [Vastineen laatiminen](#vastineen-laatiminen)
  - [Kirjoitusten muokkaaminen](#kirjoitusten-muokkaaminen)
- [Foorumin yleiset toiminnot](#foorumin-yleiset-toiminnot)
  - [Kategoriat](#kategoriat)
    - [Dashboard](#dashboard)
  - [Hakeminen](#hakeminen)
  - [Järjestäminen](#järjestäminen)
  - [Rajaaminen](#rajaaminen)

## Sovelluksen käyttöönotto
### Suorittaminen paikallisesti
- Paikallisesti suoritettuna tarvitset:
  - Vähintään Pythonin version 3.5
  - Pythonin liitännäisten hallintaan tarkoitetun pip:in
  - Jonkin Python-virtuaaliympäristön hallintaan soveltuvan liitännäisen - esim. venv

- Kloonaa repositorio omalle laitteellesi.
- Asenna sovelluksen vaatimat liitännäiset suorittamalla komento ``pip install -r requirements.txt`` repositorion juuressa.
- Käynnistä virtuaaliympäristö - jos käytät venviä, komennolla ``source venv/bin/activate``.
- Nyt voit käynnistää palvelimen paikallisesti komennolla ``python3 run.py``
- Sovellukseen pääset menemällä web-selaimella osoitteeseen ``localhost:5000``.

#### Ensimmäiset admin-tunnukset
Admin-oikeudet täytyy antaa ensimmäiselle admin-tason käyttäjälle manuaalisesti.

  - Varmista, että sinulla on jokin SQL-tietokannanhallintajärjestelmä asennettuna laitteellesi (esim. SQLite)

Avaa tietokanta menemällä repositorion alikansioon ``/application`` ja suorittamalla:
```
sqlite3 database.db
```

Kopioi seuraava komento ja paina Enter: 
```SQL
UPDATE account SET isSuper = 1 WHERE account.id = 1;
```

Jos käytät jotakin muuta tietokannanhallintajärjestelmää kuin SQLite (esimerkiksi Herokussa postgreSQL:ää), komento voi olla hieman erilainen. postgreSQL-muodossa: 
```
UPDATE account SET "isSuper" = true WHERE account.id = 1;
```

## Käyttäjät
### Rekisteröityminen ja kirjautuminen
#### Uuden käyttäjätunnuksen luominen
- Valitse sivuston oikeasta yläkulmasta valikkopalkista "Register"
- Kirjoita lomakkeeseen haluamasi käyttäjätunnus ja salasana 
  - (**HUOM!!!** Salasanat on toistaiseksi tallennettu plaintext-muodossa, joten tietoturvasi vuoksi on erityisen tärkeää, ettet käytä salasanaa, jota käytät jossakin muussa palvelussa.)
- Klikkaa "Register" -painiketta
- Uusi käyttäjätunnus on nyt luotu ja voit kirjautua sisään

#### Sisäänkirjautuminen
- Jos et ole vielä rekisteröitynyt, luo uusi tunnus
- Valitse sivuston oikeasta yläkulmasta valikkopalkista "Login"
- Täytä lomakkeeseen käyttäjätunnuksesi ja salasanasi
- Klikkaa "Log in" -painiketta
- Olet nyt kirjautunut sisään ja sinut ohjataan viestilistaukseen
- Jos haluat kirjautua ulos, valitse sivuston oikeasta yläkulmasta "Log out"

### Käyttäjäprofiilien tarkastelu
- Jos olet kirjautunut sisään, näet oman profiilisi valitsemalla sivuston oikeasta yläkulmasta valikkopalkista "Logged in as [käyttäjätunnus]"
- Profiilisivullasi näet:
  - Onko tunnuksellasi admin-status
  - Milloin olet liittynyt sivustolle
  - Kaikki aloittamasi langat (vanhin ensin)
- Jos olet admin-tason käyttäjä, voit myös luopua oikeuksistasi klikkaamalla "Demote from admin" -painiketta (**HUOM!** Kun luovut oikeuksistasi, voit saada ne takaisin vain toiselta admin-tason käyttäjältä!)
- Muiden käyttäjien profiilien tarkastelu onnistuu klikkaamalla heidän käyttäjätunnuksiaan viestien yhteydessä.

### Admin-oikeudet
- Admin-tason käyttäjän tunnistaa käyttäjänimen vieressä näkyvästä punaisesta tunnisteesta, jossa lukee 'ADMIN'.
- Admin-tason käyttäjät voivat:
  - Muokata ja poistaa mitä tahansa viestejä keskustelupalstalla
  - Luoda ja poistaa viestikategorioita
  - Muuttaa toisten käyttäjien admin-statusta

## Kirjoitukset
### Uuden keskustelulangan avaaminen
- Valitse sivuston vasemmasta yläkulmasta "New message"
- Valitse kategoria, johon haluat kirjoituksesi päätyvän
- Syötä lomakkeeseen haluamasi otsikko ja viestisi sisältö
- Klikkaa "Post" -painiketta
- Uusi kirjoitus on nyt luotu ja se on kaikkien tarkasteltavissa valitussa kategoriassa ja 'Dashboard' -sivulla

### Vastineen laatiminen
- Valitse foorumilta lanka, johon haluat vastata, ja avaa se.
- Valitse langan ensimmäisen viestin sisällön alta "Reply".
- Sinut ohjataan vastaussivulle, jossa näet langan ensimmäisen viestin sisällön ja voit syöttää haluamasi vastauksen.
- Kun olet kirjoittanut vastineesi, klikkaa "Reply" -painiketta.
- Vastineesi on nyt tallennettu ja listataan alkuperäisen viestin alla (järjestyksessä vanhin ensin)

### Kirjoitusten muokkaaminen
- Voit muokata vain omia kirjoituksiasi.
- Etsi viesti, jota haluat muokata.
- Valitse sen oikeasta alareunasta "Edit" tai "Delete", jos haluat poistaa kyseisen kirjoituksen kokonaan.
- Sinut ohjataan muokkausnäkymään, jossa näet viestisi alkuperäisen sisällön. Jos muokkaat langan ensimmäistä viestiä, voit myös valita langalle uuden otsikon.
- Kun olet tehnyt muokkauksesi, klikkaa "Confirm" -painiketta
- Muokkauksesi on nyt tallennettu.

## Foorumin yleiset toiminnot
### Kategoriat
- Keskustelufoorumille uutta lankaa aloittaessa on sille valittava kategoria.
- Kaikkia foorumin kategorioita on mahdollista tarkastella valitsemalla navigointipalkista "Categories".
- Voit myös klikata haluamasi kategorian nimeä nähdäksesi kaikki kyseiseen kategoriaan aloitetut langat.

#### Dashboard
- Dashboard on sivu, jolla listataan kaikki foorumin langat tuoreusjärjestyksessä (uusimmasta vanhimpaan) riippumatta niiden kategoriasta.

### Hakeminen
- Hakeminen onnistuu foorumin yläpalkin vasemmalla puoliskolla sijaitsevalla lomakkeella.
- Voit hakea viestejä niiden otsikon tai otsikon osan perusteella kirjoittamalla hakupalkkiin jotakin ja klikkaamalla "Search".
- Haun tulokset listataan järjestyksessä uusimmasta vanhimpaan.
- Jos jätät haun tyhjäksi, sinut ohjataan "Dashboard"-sivulle.

### Järjestäminen
- Keskustelupalstalle aloitettuja lankoja on mahdollista tarkastella erilaisissa järjestyksissä:
  - "Age (Newest First)" on foorumin oletusjärjestys. Tällöin uusimmat viestit näytetään ylimpänä.
  - "Age (Oldest First)" järjestää viestit vanhimmasta uusimpaan niiden luontipäiväyksen mukaan.
  - "Title (Ascending)" järjestää viestit aakkosjärjestyksessä A:sta Ö:hön.
  - "Title (Descending)" puolestaan järjestää viestit käänteiseen aakkosjärjestykseen.

### Rajaaminen
- Oletuksena keskustelufoorumi näyttää 10 ensimmäistä viestiä ottaen huomioon valitsemasi järjestysvaihtoehdon.
  - "Limit to 10" näyttää 10 ensimmäistä viestiä
  - "Limit to 20" näyttää 20 ensimmäistä viestiä
  - "Limit to 50" näyttää 50 ensimmäistä viestiä
  - "Show all" ei rajoita viestien määrää listauksessa.
