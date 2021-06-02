# Self-Balancing Robot

### Resources

* [Maker.pro](https://maker.pro/arduino/projects/build-arduino-self-balancing-robot)

### Materials

* Driver
* Metro Express
* Accelerometer: LSM303DLHC [library](https://github.com/hnovak94/SelfBalancingRobot/blob/main/adafruit_lsm303_accel.mpy)
* Battery pack
* Acryllic 
* 2 motors (withe wheels)

### Created Parts

[Onshape Document](https://cvilleschools.onshape.com/documents/5b15c4cd2f6854dc4cc32ff8/w/ed23d40d7b31ab41a2311be3/e/2e2d58ec8adab28d16997f49)

3 parts need designing. 
2 : 1 size ratio of parts. 

**Sides:** (150 mm by 80 mm) Hole on one side for battery pack wires (5 mm in diameter), slot in the middle for middle level. 

<img src = "https://github.com/hnovak94/SelfBalancingRobot/blob/main/sidewall.png" height = "250">

**Bottom :** (170 mm by 100 mm)Two holes for the motors, and 3 holes for 9V battery holder.


**Top:** (170 mm by 80 mm) 2 holes for battery pack.

<img src = "https://github.com/hnovak94/SelfBalancingRobot/blob/main/topbottomwall.png" height = "250">

**Middle:** (170 mm by 80 mm) 4 holes for Metro, H-bridge, and accelerometer. 

<img src = "https://github.com/hnovak94/SelfBalancingRobot/blob/main/middlewall.png" height = "250">

### Wiring

<img src= "https://github.com/hnovak94/SelfBalancingRobot/blob/main/wd.jpeg" height = "400">

#### Accelerometer

Vin: 5V

GND: Ground

SDA: SDA

SCL: SCL


#### Driver

AOUT: wires of the motor, red right, black left

BOUT: wires of second motor, red right black left

AIN1: 13

AIN2: 12

SLP: 3.3

BIN1: 2

BIN2: 6

GND: Ground


#### Motors

Connect to AOUT and BOUT of driver


#### Battery Pack

Two wires connect to driver


### Code

Test [code](https://github.com/hnovak94/SelfBalancingRobot/blob/main/intromotor) for motors
Test [code](https://github.com/hnovak94/SelfBalancingRobot/blob/main/introaccel.py) for accelerometer
Test [code](https://github.com/hnovak94/SelfBalancingRobot/blob/main/accelmotor.py) for motor + accel. together

#### Libraries:

* board

* pwmio

* busio

* [adafruit_lsm303](https://github.com/hnovak94/SelfBalancingRobot/blob/main/adafruit_lsm303_accel.mpy)

### Timeline

**WEEK 1:** Project Proposal

**WEEK 2:** The CAD design on Onshape. The design should be relatively simple since it's only 2 parts>

**WEEK 3:** Should have parts by this time. Get everything wired up with the libraries working. I don't want to underestimate the amount of time the libraries will take so this will be pushed to week 4 as well. 

**WEEK 4:** Figure out libraries and begin coding. 

**WEEK 5:** Coding

**WEEK 6:** Coding

[Trello board](https://trello.com/b/zZdArFdT/self-balancing-robot)
