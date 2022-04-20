# Rendszerterv
## Osztálydiagramm
![uml class diagramm](/docs/uml_class.PNG)
### Parser
#### Áttekintés
Az osztály alapvetően a log file parseolásáért felelős, valamint Message  objektumok létrehozásáért.
#### Attribútomok
1. -input: file
A bemenetként használt file-t tartalmazza
##### Függvények
1. +parse(input): Message [1..*]
Kigyűjti a releváns üzeneteket, és Message objektumokat készt belőlük, amiket egy tömbbe gyűjt.
2. patternCheck(str): bool
Ellenőrzi, hogy adott üzenet releváns-e.
### Message
#### Áttekintés
Az alapegységül szolgáló osztály. Egy üzenet fontos információit tartalmazó objektum.
#### Attribútumok
1. -id: int
Általunk generált azonosítószám.
2. -timestamp: str
Üzenet időbélyege.
3. -sending_Component: str
Az üzenetet küldő  komponens.
4. -event_Type: str
Az üzenet eseményének típusa.
5. -sending_File: str
Melyik fileból indult az üzenetküldés
6. -operation_Type: str
Az üzenetküldési operáció típusa
7. -receiving_Component: str
A fogadó komponens
8. -message_Type: str
Milyen függvény indította az üzenetküldést
9. parameter_Keys: str[1..*]
A paraméterek kulcsai
#### Függvények
1. +Message
Konstruktor az objektumhoz
2. +get_SendingComponent()
A küldő komponens lekérése
3. +get_ReceivingComponent()
A fogadó komponens lekérése
4. +get_OperationType()
Az üzenetküldési operáció típusának lekérése
5. +get_SendingFile()
Annak lekérése, hogy melyik fileból indult az üzenetküldés
6. get_MessageType()
Az üzenetküldést indító függvény lekérése
7. get_ParameterKeys()
A paraméterek kulcsainak lekérése
### MessagesByComponents
#### Áttekintés
Tárolóosztály a Message obejtumok tárolására, valamint a GUI felé történő átadásra.
#### Attribútumok
1. -messages: Message[1..*]
A tárolt üzenetek
### GUI
#### Áttekintés
A megjelenítést végző osztály.
#### Attribútumok
1. -messages: Message[1..*]
A megjelenítendő üzenetek
#### Függvények
1. +draw(messages)
A megjelenített kép (újra)rajzolása
2. +show()
Az aktuálisan megjelenített kép mutatása a felhasználó felé
## Szekvencia diagramm
![uml sequence diagramm](/docs/uml_sequence.PNG)
### Általános folyamat
Az alábbi diagramm ábrázolja az általános folyamatát a parseolás valamint megjelenítés működését illetően.