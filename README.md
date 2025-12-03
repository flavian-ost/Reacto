# 🎮 REACTO
REACTO ist eine kompakte mobile Spielkonsole, mit der man allein oder im Multiplayer-Modus durch vielseitige Steuerungen Minispiele spielen kann – perfekt, um überall Spass zu haben und das Gehirn zu trainieren.

<img width="430" height="289" alt="Reacto" src="https://github.com/user-attachments/assets/a9a0d931-f5b3-475a-a81e-e3a1c7fe9652" />

## 🧩 Konzept
Dieses Projekt entstand im Rahmen des Moduls Physical Prototyping und wurde innerhalb von sieben Wochen umgesetzt.
Als zentrale Leitfrage diente uns folgender One Sentence Brief:
Erfinde ein Speil oder gestalte eines neu, indem du seine bestehende Interaktivität in Frage stellst oder eine neue Interaktivität entwickelst, die über den Bildschirm hinausgeht.
Auf dieser Grundlage sollte anschliessend ein physischer Prototyp entwickelt werden.


## 🕹️ Wie man spielt
1. REACTO über den **Button XY** einschalten  
2. Anzahl der Spieler auswählen  
3. Ein Spiel auswählen
4. Mit dem Spiel beginnen

### Verfügbare Spiele

- ⏱️ Time Guess – Schätze, wann eine bestimmte Zeitspanne abgelaufen ist  
- 🔍 Hide and Seek – Finde REACTO wieder! 
- ⚡ Speed it up – Wie schnell kannst du REACTO drehen?
- 🔥 Hot Potato Mode – Gib REACTO rechtzeitig weiter, bevor der Timer endet
-  Pattern Match - Random LED-Muster anzeigen, korrektes Nachdrücken erkennen
-  Action Commands - Voice Commands, Interaktion erkennen z.B. "Twist it"

### Interaktionen
- Push it
- Twist it
- Move it


## 🧰 Benötigte Komponenten
REACTO besteht aus drei Hauptkomponenten

### Hardware
* Arduino Nano ESP32  
* Nano Grove Pad  
* ModulinoPixels  
* ModulinoBuzzer  
* ModulinoButtons  
* ModulinoKnob  
* ModulinoMovement  
* LCD 1602 Display  
* NeoPixel Ring  
* Batterie (550 mAh, 3.7 V)  
* Button  

### Software
* MicroPython
* ???

### Code-Bibliotheken
*(Hier können spezifische Libraries ergänzt werden.)*


## 🛠️ Zusammenbau

### Verkabelung

Die Modulino-Module werden über Daisy-Chaining miteinander verbunden.  
*(Optional kann hier ein Wiring-Diagramm ergänzt werden.)*

### Gehäuse

Das Gehäuse ist ein 3D-gedrucktes Case. Wir haben uns für einene 3D-Druck entschieden, da dieser für uns am praktischsten ist.. 
*(STL-Files können hier verlinkt werden.)*



## ❓Troubleshooting / FAQ

### REACTO startet nicht  
- Batterie geladen?  
- Verbindung zwischen ESP32 und Power-Modul prüfen  
- Button-Anschluss kontrollieren

### Display zeigt nichts an  
- I2C-Adresse korrekt?  
- Display richtig am Grove Pad angeschlossen?  

### NeoPixel Ring leuchtet nicht  
- Datenverbindung (DIN/DOUT) prüfen  
- `neopixel` im Code korrekt initialisiert?  
- Manche Rings benötigen 5V-Level – ggf. Level-Shifter nutzen

### Ein Modulino wird nicht erkannt  
- Daisy-Chain richtig gesteckt?  
- Richtiger Port im Code?  
- Modul einzeln testen

### Code wird nicht übertragen  
- MicroPython wirklich installiert?  
- Richtigen COM-Port/Device in der IDE gewählt?  
- Reset während des Uploads kann helfen

---

## 📄 Lizenz
Dieses Projekt steht unter der **MIT License**.  
Du darfst den Code frei verwenden, anpassen, erweitern und verbreiten – solange die ursprüngliche Lizenz erhalten bleibt.
