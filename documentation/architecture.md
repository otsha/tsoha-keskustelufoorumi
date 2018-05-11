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
Sovelluksen käynnistää nimellisesti repositorion juuressa sijaitseva ``run.py``. Varsinaisesta initialisaatiosta - mm. kirjastojen tuonnista, tietokannan konfiguroinnista ja alustuksesta - vastaa kansion ``/application`` tiedosto ``__init__.py``.

Sovelluksen käyttämät tietueet sijaitsevat kansion ``/application`` alikansioissa niin, että jokaisen alikansion sisältö vastaa yhtä sovelluksen osa-aluetta. Esimerkiksi kansio ``/application/auth`` sisältää kaiken autentikaatioon ja käyttäjätileihin liittyvän koodin ja ``/application/message`` kaiken viesteihin liittyvän koodin.

Tietuekansioiden sisällä ``views.py`` hoitaa tietueeseen liittyvien näkymien ja käyttäjän palvelimelle lähettämien pyyntöjen käsittelystä, kun taas ``models.py`` sisältää sovelluksen käyttämän mallin tietokannan tauluista. Mahdollinen ``forms.py`` puolestaan määrittelee tietueeseen liittyvien lomakkeiden sisällön ja validointivaatimukset.

Käyttäjälle näytettävä sisältö - käyttöliittymä - sijaitsee kansiossa ``/application/templates``, jossa sisältö on myöskin jaettu alikansioihin osa-alueittain.

## Käyttöliittymä
Kansioon ``/application/templates`` sijoitettu käyttöliittymä on toteutettu HTML:llä [Bootstrap](https://getbootstrap.com/) -kirjastoa tyylittelyssä apua käyttäen. Tietokannan tiedon näyttäminen (palvelimen ja käyttöliittymän välinen tiedonvälitys) on toteutettuna [Jinja2](http://jinja.pocoo.org/):lla.

Käyttöliittymän runko sijaitsee tiedostossa ``/application/templates/layout.html``, jossa määritellään Bootstrapin käyttöönotto, sivuston otsikko (``<title>``), navigointipalkki ja varsinaiselle sisällölle varattu ``container``, jolla sivuston sisältö keskitetään mielekkäästi ruudun keskelle. Kaikki käyttöliittymän sivut toteuttavat käyttöliittymärungon.

## Tietokanta
### Tietokannan kuvaus
Sovelluksen käyttämä tietokannanhallintajärjestelmä riippuu sen käyttöympäristöstä. Jos sovellus suoritetaan paikallisesti, pyrkii se käyttämään SQLite-tietokantaa. Jos sovellus taas huomaa käynnistyneensä Herokussa (tarkistetaan ``application/__init__.py`` alussa), käyttää se postgreSQL-tietokantaa.

Tietokannassa on 4 taulua (Käyttäjä, Lanka, Vastaus ja Kategoria), joihin tallennetaan sovelluksen kannalta oleellinen data. Tietokannassa on myös yksi liitostaulu Käyttäjän ja Langan välillä, jolla pidetään kirjaa Langan luetuksi merkinneistä käyttäjistä.

#### Tietokohteet
* Käyttäjä
* Lanka (artikkeli, aloitusviesti)
* Vastaus (aina ja vain lankaan)
* Kategoria (aihe, keskustelualue, määritellään langalle sitä aloittaessa)

### Tietokantakaavio
*Todellisuudessa kaikilla tietokannan tauluilla on attribuutit date_created ja date_edited, sillä ne perustuvat yhteiseen Base-malliin (``application/models.py``), mutta koska niitä ei koskaan käytetä sovelluksen toiminnassa, on ne jätetty selkeyden vuoksi pois tietokantakaaviosta.*

![Projektin tietokantakaavio](https://yuml.me/7069ca1d.png)

[PDF](http://yuml.me/7069ca1d.pdf) | [yUML](http://yuml.me/edit/7069ca1d)

### SQL-kyselyt
Taulujen luominen tietokantaan ja yksinkertaiset listaukset on pääsääntöisesti toteutettu SQLAlchemyn avulla. Kuvataan kuitenkin CREATE TABLE -lauseet ja joitakin sovelluksen päätoiminnallisuuksia SQL -muodossa.

#### CREATE TABLE -lauseet
##### Account (Käyttäjä, User)
```SQL
CREATE TABLE account (
        id INTEGER NOT NULL,
        date_created DATETIME,
        date_modified DATETIME,
        username VARCHAR(30) NOT NULL,
        password VARCHAR(144) NOT NULL,
        "isSuper" BOOLEAN NOT NULL,
        PRIMARY KEY (id),
        CHECK ("isSuper" IN (0, 1))
);
```

##### Category (Kategoria)
```SQL
CREATE TABLE category (
        id INTEGER NOT NULL,
        date_created DATETIME,
        date_modified DATETIME,
        name VARCHAR(140) NOT NULL,
        PRIMARY KEY (id)
);
```

##### Message (Langan aloitusviesti)
```SQL
CREATE TABLE message (
        id INTEGER NOT NULL,
        date_created DATETIME,
        date_modified DATETIME,
        name VARCHAR(140) NOT NULL,
        content VARCHAR(1000) NOT NULL,
        read BOOLEAN NOT NULL,
        account_id INTEGER NOT NULL,
        category_id INTEGER NOT NULL,
        PRIMARY KEY (id),
        CHECK (read IN (0, 1)),
        FOREIGN KEY(account_id) REFERENCES account (id),
        FOREIGN KEY(category_id) REFERENCES category (id)
);
```

##### Reply (Vastausviesti)
```SQL
CREATE TABLE reply (
        id INTEGER NOT NULL,
        date_created DATETIME,
        date_modified DATETIME,
        content VARCHAR(1000) NOT NULL,
        account_id INTEGER NOT NULL,
        message_id INTEGER NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY(account_id) REFERENCES account (id),
        FOREIGN KEY(message_id) REFERENCES message (id)
);
```

##### Read_Message (Liitostaulu - viestien merkitseminen luetuksi)
```SQL
CREATE TABLE read_message (
        id INTEGER NOT NULL,
        date_created DATETIME,
        date_modified DATETIME,
        account_id INTEGER NOT NULL,
        message_id INTEGER NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY(account_id) REFERENCES account (id),
        FOREIGN KEY(message_id) REFERENCES message (id)
);
```

#### Yhteenvetokyselyt

##### Oletusviestilistaus (10 uusinta)
```SQL
SELECT * FROM Message
        ORDER BY Message.date_created DESC
        LIMIT 10;
```
Todellisuudessa sovellus pyytää kaikki viestit järjestettynä uusimmasta vanhimpaan ja sitten näyttää vain 10 ensimmäistä pythonin taulukosta SQL-limitin sijaan, mutta kyselyn voisi toteuttaa kokonaisuudessaan myös näinkin. Nykyratkaisu on käytössä koodin selkeyttämiseksi.

##### Kategorialistaus (aakkosjärjestyksessä)
```SQL
SELECT * FROM Message
        WHERE Message.category_id = ?
        ORDER BY Message.name ASC;
```

##### Viestin kaikki vastaukset (vanhin ensin)
```SQL
SELECT Reply.id, Reply.account_id from Reply
        WHERE Reply.message_id = ?
        ORDER BY Reply.date_created ASC;
```

##### Etsi mahdollinen read_message (Onko käyttäjä lukenut viestin?)
```SQL
SELECT DISTINCT account_id FROM read_message
        WHERE read_message.message_id = ?
        AND read_message.user_id = ?;
```
Jos kyselyn tuloksena on yksikin rivi (rivejä ei pitäisi olla useampaa), on käyttäjä merkinnyt viestin luetuksi.
