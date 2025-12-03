# 🎮 REACTO
REACTO is a compact mobile gaming console that enables players to enjoy a variety of mini-games either solo or in multiplayer mode. Its diverse interaction methods make it ideal for quick entertainment anywhere while simultaneously training cognitive and motor skills.

<img width="430" height="289" alt="Reacto" src="https://github.com/user-attachments/assets/a9a0d931-f5b3-475a-a81e-e3a1c7fe9652" />

## 🧩 Concept
This project was developed as part of the Physical Prototyping module and completed over the course of seven weeks.

Our guiding principle was the following One Sentence Brief:
Invent a game or redesign an existing one by questioning its current interactivity or developing a new interaction that goes beyond the screen.

**Concept**
With REACTO, we designed a physical game console that unites several fast-paced mini-games and makes use of a broad spectrum of interactions. The central idea was to translate typical digital game mechanics into a tangible, tactile experience. Interactions such as Push it, Twist it, and Move it, together with additional sensor-based actions, create an immediate and physically engaging form of play.
The console functions as a modular platform: it provides core functionality, sensors, and feedback mechanisms, while multiple game modes operate on top of this shared hardware foundation. This approach results in a flexible system that can be expanded both technically and playfully.

**Objective**
The objective of the project was to develop an interactive device that surpasses conventional screen-based gameplay and places physical interaction at its core. REACTO was designed to actively involve players through a wide variety of inputs—ranging from pressing, twisting, and shaking to pattern recognition and other sensor-driven interactions.
Our aim was to create a fast, intuitive, and competitive experience that challenges reaction time, dexterity, and timing. The device needed to be robust, user-friendly, and technically adaptable to support the integration of future mini-games without major modifications.

**Motivation**
Our motivation stemmed from the desire to reconnect digital gaming with physical experience. While modern games often focus on visual and auditory stimulation, tactile and bodily interaction tends to play a secondary role. With REACTO, we sought to explore how reintroducing physicality into gameplay can create new dynamics and enhance social engagement.
We were particularly intrigued by the idea of developing a device that functions not as a single game, but as a platform for multiple quick challenges. The social aspect—short duels, passing the device around, reacting together—was a significant driver for the project.
Additionally, building our own console gave us the opportunity to merge hardware and software in a creative and experimental way, allowing us to investigate how different interactions can be captured technologically and transformed into meaningful gameplay.

## 🕹️ How to play
1. Turn on REACTO using Button XY
2. Select the number of players 
3. Choose a game
4. Start playing


### Available Games

- ⏱️ Time Guess – Estimate when a given time interval has elapsed.
- 🔍 Hide and Seek – Find REACTO!
- ⚡ Speed it up – Spin REACTO as fast as possible.
- 
  ???
- 🔥 Hot Potato Mode – Pass REACTO before the timer expires.
- 🔶 Pattern Match – Memorize random LED patterns and reproduce them accurately.
- 🎤 Action Commands – React to on-screen commands such as “Twist it!” or “Shake it!”.
  ???

### Interactions
- 👉 Push it
  GIF ???
- 🔄 Twist it
  GIF ???
- 🤾 Move it
  GIF ???
- 🤝 Pass it
  GIF ???
- 🔍 Find it



## 🧰 Benötigte Components
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

### Code-Libraries
*(Hier können spezifische Libraries ergänzt werden.)*

#### Aufbau
Main.py
Games.py
....????



## 🛠️ Assembly

### Wiring
The Modulino modules are connected via daisy-chaining.
(A wiring diagram can be added here.)

### Housing
The housing is a 3D-printed enclosure. We opted for 3D printing as it provided the most practical and customizable solution for our prototype.
(STL files can be linked here.)



## ❓Troubleshooting / FAQ

### REACTO does not power on 
- Is the battery charged?
- Check the connection between the ESP32 and the power module
- Verify the button wiring

### Display remains blank
- Is the I2C address correct?
- Is the display connected to the correct Grove Pad port?

### NeoPixel ring does not light up 
- Check data lines (DIN/DOUT)
- Ensure neopixel is initialized correctly
- Some rings require 5V signal levels — a level shifter may be necessary

### A Modulino module is not detected
- Verify the daisy chain connection
- Check that the correct port is defined in the code
- Test the module individually

### Code upload fails
- Is MicroPython installed on the board?
- Correct COM port/device selected in the IDE?
- Resetting the board during upload may help


## 📄 License
This project is released under the **MIT License**.
You are free to use, modify, extend, and distribute the code as long as the original license is included.


