# 🎮 REACTO
REACTO ist eine kompakte mobile Spielkonsole, mit der man allein oder im Multiplayer-Modus durch vielseitige Steuerungen Minispiele spielen kann – perfekt, um überall Spass zu haben und das Gehirn zu trainieren.

<img width="430" height="289" alt="Reacto" src="https://github.com/user-attachments/assets/a9a0d931-f5b3-475a-a81e-e3a1c7fe9652" />

## 🧩 Konzept
Dieses Projekt entstand im Rahmen des Moduls Physical Prototyping und wurde innerhalb von sieben Wochen umgesetzt.

Als zentrale Leitfrage diente uns folgender One Sentence Brief:
Erfinde ein Spiel oder gestalte eines neu, indem du seine bestehende Interaktivität in Frage stellst oder eine neue Interaktivität entwickelst, die über den Bildschirm hinausgeht.

**Konzept**
Mit REACTO entwickelten wir eine physische Spielkonsole, die verschiedene schnelle Mini-Games vereint und dabei ein breites Spektrum an Interaktionen nutzt. Im Zentrum stand die Übertragung digitaler Spielmechaniken in ein haptisches, greifbares Format. Durch Aktionen wie Push it, Twist it oder Move it sowie weitere sensorische Interaktionen sollte das Gerät ein unmittelbares, körperlich erfahrbares Spielerlebnis ermöglichen.
Die Konsole dient dabei als modularer Rahmen: Sie stellt Grundfunktionen, Sensorik und Feedbackmechanismen bereit, während unterschiedliche Spielmodi auf denselben Hardwareprinzipien aufbauen. Dadurch entsteht ein flexibles System, das sowohl technisch als auch spielerisch erweiterbar ist.

**Zielsetzung**
Unser Ziel war es, ein interaktives Spielgerät zu entwickeln, das klassische Bildschirmgrenzen überschreitet und physische Interaktionen in den Mittelpunkt stellt. REACTO sollte Spieler*innen aktiv einbinden, indem es vielfältige Eingaben ermöglicht — von Drücken, Drehen und Schütteln bis hin zu sensorbasierten Erkennungen wie Mustern. Dabei sollte eine schnelle, zugängliche und kompetitive Spielerfahrung entstehen, die Reaktion, Geschicklichkeit und Timing herausfordert. Die Konsole sollte robust konstruiert sein, intuitiv bedienbar bleiben und gleichzeitig genügend technisches Potenzial bieten, um zukünftige Mini-Games unkompliziert integrieren zu können.

**Motivation**
Unsere Motivation entsprang dem Wunsch, digitales Spielen wieder stärker an physische Erlebnisse zu koppeln. Viele moderne Spiele konzentrieren sich auf visuelle und audiovisuelle Reize, während haptische und körperliche Elemente oft in den Hintergrund treten. Mit REACTO wollten wir bewusst untersuchen, wie sich diese physische Dimension in den Vordergrund rücken lässt und welche neuen Dynamiken dadurch beim Spielen entstehen.
Darüber hinaus reizte uns der Gedanke, ein Gerät zu entwickeln, das nicht nur ein einzelnes Spiel beherbergt, sondern als Plattform für unterschiedliche, schnelle Herausforderungen dient. Der soziale Charakter — kurze Duelle, spontanes Weitergeben, gemeinsame Reaktionen — war dabei ein wesentlicher Treiber.
Die Entwicklung einer eigenen Konsole bot uns ausserdem die Möglichkeit, Hard- und Software kreativ miteinander zu verbinden und im Sinne eines praktischen Prototypings experimentell auszutesten, wie verschiedene Interaktionen technisch erfasst und spielerisch sinnvoll umgesetzt werden können.

## 🕹️ Wie man spielt
1. REACTO über den **Button XY** einschalten  
2. Anzahl der Spieler auswählen  
3. Ein Spiel auswählen
4. Mit dem Spiel beginnen

### Verfügbare Spiele

- ⏱️ Time Guess – Schätze, wann eine bestimmte Zeitspanne abgelaufen ist.
- 🔍 Hide and Seek – Finde REACTO wieder! 
- ⚡ Speed it up – Wie schnell kannst du REACTO drehen?
- 🔥 Hot Potato Mode – Gib REACTO rechtzeitig weiter, bevor der Timer endet.
- 🔶 Pattern Match – Merke dir zufällige LED-Muster und drücke sie anschliessend korrekt nach.
- 🎤 Action Commands – Reagiere auf Kommandos auf dem Display wie „Twist it!“ oder „Shake it!“.

### Interaktionen
- 👉 Push it
  GIF ???
- 🔄 Twist it
  GIF ???
- 🤾 Move it
  GIF ???
- 🤝 Pass it
  GIF ???
- 🔍 Find it



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

#### Aufbau
<img width="921" height="461" alt="image" src="https://github.com/user-attachments/assets/b7103f5a-0551-4d7b-a830-a01696e64cdf" />




## 🛠️ Zusammenbau

### Verkabelung

Die Modulino-Module werden über Daisy-Chaining miteinander verbunden.  
<img width="1071" height="328" alt="image" src="https://github.com/user-attachments/assets/967cc28f-8a67-4829-bc6c-2cf2bcff96b2" />


### Gehäuse

Das Gehäuse ist ein 3D-gedrucktes Case. Wir haben uns für einene 3D-Druck entschieden, da dieser für uns am praktischsten ist. 
<img width="1031" height="627" alt="image" src="https://github.com/user-attachments/assets/8ef0601b-9db7-4b22-a9bb-134dbf643c84" />
<img width="856" height="897" alt="image" src="https://github.com/user-attachments/assets/d4561c5b-d1ef-4acc-84fb-cef0c0b59ac2" />
<img width="1336" height="1124" alt="image" src="https://github.com/user-attachments/assets/cace1330-773a-44af-84e6-826c44a515e0" />





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


## 📄 Lizenz
Dieses Projekt steht unter der **MIT License**.  
Du darfst den Code frei verwenden, anpassen, erweitern und verbreiten – solange die ursprüngliche Lizenz erhalten bleibt.
