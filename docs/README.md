# A programról
A program képes egy router log filejaiból kiszedni a SIP üzeneteket, valamint az időzítéshez köthető üzeneteket. 

# Felhasználói kézikönyv

A program indítása rendkívül  egyszerű, csak klónozzuk a kódbázist, majd a megfelelő mappába navigálva a Command Promtban vagy a Terminalban a mappába navigálva az alábbi paranccsal tudjuk elindítani a programot:
python app.py --file [feldolgozandó fájl]
Ezután két fájl generálódik, egy .png és egy .txt kiterjesztésű, mindkettőn egy szekvencia diagramm lesz látható. A komponensek lesznek a megjelenő aktorok, az üzenetek pedig a SIP üzenetek típusaival és az időzítők indításával, leállításával valamint timeoutjaival jelennek meg.