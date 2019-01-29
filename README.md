# Präferenzverknüpfungsservice

_Proof-of-Concept_ Implementierung der _Verknüpfungssservice_ -Komponente der _Privacy Proxy_ Architektur.

Es handelt sich um ... tbd.

## Nutzung

Im folgenden werden mögliche Wege aufgezeigt, um den Verknüpfungsservice zu testen.

### Anforderungen

Zur Speicherung von Präferenzen nutzt der Webservice im Hintergrund die Datenbank [MongoDB](https://www.mongodb.com/de/what-is-mongodb). Die Zugangsdaten zu dieser werden über Umgebungsvariablen an den Service übergeben:

    'mongodb_url' --> URL des Datenbankservers
    ‘mongodb_user’ --> Kennung d. Datenbanknutzers
    'mongodb_pw' --> Passwort des Datenbanknutzers

Angaben zu erforderlichen Programmbibliotheken und Erweiterungen finden sich in der Datei `requirements.txt`.


### a) Lokale Ausführung
Es wird die Nutzung einer vituellen Umgebung [(_virtualenv_)](https://www.dpunkt.de/common/leseproben//12951/2_Ihre%20Entwicklungsumgebung.pdf#page=15) empfohlen.

Nach der [Installation](https://docs.mongodb.com/manual/installation/)  von MongoDB oder der Registrierung einer gehosteten Instanz der Datenbank (z.B. [hier](https://www.mongodb.com/cloud/atlas)) sowie dem Setzen der oben genannten Umgebungsvariablen werden folgende Anweisungen in der Konsole aufgerufen:

    >> git clone https://github.com/EMIDD-Projekt/PraeferenzVerknuepfungsService.git

    >> pip install -r requirements.txt

    >> python PolProvServ.py

Anschließend steht der Service unter [`http://127.0.0.1:5000/`]( http://127.0.0.1:5000/) zur Verfügung.

### b) Ausführung als Cloud Service
tbd.
