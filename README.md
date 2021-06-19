# Quadruped Ava
![QEFRONT](https://user-images.githubusercontent.com/53890241/120611873-f4236c00-c497-11eb-89dc-f8c86aae2deb.png)
![QEBCK](https://user-images.githubusercontent.com/53890241/120611885-f71e5c80-c497-11eb-8ec9-91af1f57dc68.png)



## Overview
This repository will contain the code, bill of materials for my quadruped robot using a Nvidia Jetson Nano I developed as well as stl files to 3D print the design. There is still much to work on and I will update this repository as I progress on this project :).

## Existing Designs and Code Used
I would like to thank Miguel Ayuso Parrilla as I used his quadruped leg design and learnt alot from his project at:

https://hackaday.io/project/171456-diy-hobby-servos-quadruped-robot

I also learnt much and based my design from the work done by the SpotMicroAi community here:

https://spotmicroai.readthedocs.io/en/latest/

## To Do List
- [x] Assemble EVE 
- [ ] Upload STL files for 3D printing
- [x] Complete inverse kinematics of model
- [x] Teleoperate using bluetooth controller
- [ ] Get EVE to walk
- [ ] Implement different gaits (walk, creep, run)
- [ ] Dynamic walking using reinforcement learning and closed loop control
- [ ] Implement computer vision and machine learning
- [ ] Implement behaviours through motion routines and neopixel LED
- [ ] Upload code, bill of materials and assembly instructions

## Current Progress
I did not fully document the assembly and manufacturing process and will come back to this later. For 3D printing I printed using PLA plastic on my Ender 3 v2. I will detail all the settings later as different settings were used for different parts but generally I printed using 0.16mm layer height with a wall line count of 4 and an infill density between 20 - 50%. I also used the alternate wall setting in Cura for added strength.

### Assembly of Ava
![A1](https://user-images.githubusercontent.com/53890241/120613535-ac9ddf80-c499-11eb-9ddf-0ac0ceb77be2.png)
![A2](https://user-images.githubusercontent.com/53890241/120614284-68f7a580-c49a-11eb-85c5-6f84f531884d.png)

### Inverse Kinematics and Teleoperating from Bluetooth Controller

https://photos.app.goo.gl/DhuuCmUEwGPbDo13A\

