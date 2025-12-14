# 🎮 REACTO
[German README](README_DE.md)  
REACTO is a compact mobile gaming console that enables players to enjoy a variety of mini-games either solo or in multiplayer mode. Its diverse interaction methods make it ideal for quick entertainment anywhere while simultaneously training cognitive and motor skills.


https://github.com/user-attachments/assets/2848db3a-7d19-459d-bda5-90f23dfa8c8d



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
1. Turn on REACTO using the side button
2. Select the number of players 
3. Choose a game
4. Start playing


### Available Games

- ⏱️ Time Guess – Estimate when a given time interval has elapsed.
- 🔍 Hide and Seek – Find REACTO!
- ⚡ Speed it up – Spin REACTO as fast as possible.
- 🔥 Hot Potato Mode – Pass REACTO before the timer expires.
- 🔶 Pattern Match – Memorize random LED patterns and reproduce them accurately.
- 🎤 Action Commands – React to on-screen commands such as “Twist it!” or “Shake it!”.

### Interactions
- 👉 Push it
![push](https://github.com/user-attachments/assets/7e04634c-4b55-46cd-8d59-09a958062b90)

- 🔄 Twist it
![twist](https://github.com/user-attachments/assets/97e8cb18-076e-4bcb-8303-c633e29573d7)

- 🤾 Shake it
![shake](https://github.com/user-attachments/assets/5e0e89ad-d2aa-4bd7-a198-ce356a6cd49a)




## 🧰 Required Components
REACTO consists of three main component groups.

### Hardware
* Arduino Nano ESP32  
* Nano Grove Pad  
* ModulinoBuzzer  
* ModulinoKnob  
* ModulinoMovement  
* LCD 1602 Display  
* Powerbank 

### Software
* MicroPython

### Code-Libraries
- [arduino-modulino-mpy](https://github.com/arduino/arduino-modulino-mpy)
- [micropython-i2c-lcd](https://github.com/brainelectronics/micropython-i2c-lcd/)

#### Code structure  
<img width="921" height="461" alt="image" src="https://github.com/user-attachments/assets/b7103f5a-0551-4d7b-a830-a01696e64cdf" />



## 🛠️ Assembly

### Wiring
The Modulino modules are connected via daisy-chaining.
<img width="1071" height="328" alt="image" src="https://github.com/user-attachments/assets/967cc28f-8a67-4829-bc6c-2cf2bcff96b2" />

### Housing
The housing is a 3D-printed enclosure. We opted for 3D printing as it provided the most practical and customizable solution for our prototype.
<img width="1031" height="627" alt="image" src="https://github.com/user-attachments/assets/8ef0601b-9db7-4b22-a9bb-134dbf643c84" />
<img width="856" height="897" alt="image" src="https://github.com/user-attachments/assets/d4561c5b-d1ef-4acc-84fb-cef0c0b59ac2" />
<img width="1336" height="1124" alt="image" src="https://github.com/user-attachments/assets/cace1330-773a-44af-84e6-826c44a515e0" />



## Video
https://ostch-my.sharepoint.com/:f:/r/personal/cristina_hagmann_ost_ch/Documents/03_Informatikseminar/Semester%201/Gruppenprojekt/Projektvideo?csf=1&web=1&e=Dj1fnU


## 📄 License
This project is released under the **MIT License**.
You are free to use, modify, extend, and distribute the code as long as the original license is included.


