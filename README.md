# Self-Balancing Robot

## ▷ Resources

* [Maker.pro](https://maker.pro/arduino/projects/build-arduino-self-balancing-robot)
* [Trello board](https://trello.com/b/zZdArFdT/self-balancing-robot)
* [Onshape Document](https://cvilleschools.onshape.com/documents/5b15c4cd2f6854dc4cc32ff8/w/ed23d40d7b31ab41a2311be3/e/2e2d58ec8adab28d16997f49)

## ▷ Materials

* Driver
* Metro Express
* Accelerometer: LSM303DLHC [library](https://github.com/hnovak94/SelfBalancingRobot/blob/main/adafruit_lsm303_accel.mpy)
* Battery pack
* Acryllic 
* 2 motors (withe wheels)

## ▷ Created Parts

### Walls

There are 4 walls connected by t-slots. The middle level fits into a rectangular slot in the middle of the sides. 

<img src="https://github.com/hnovak94/SelfBalancingRobot/blob/main/middlewall.png" height="200">
<img src="https://github.com/hnovak94/SelfBalancingRobot/blob/main/sidewall.png" height="200" >

The breadboard goes on top, the battery pack on the bottom of the top level, and the metro express on the middle level.

### Breadboard Holder

<img src="https://github.com/hnovak94/SelfBalancingRobot/blob/main/breadboardholder.png" height = "300">


## ▷ Wiring

<img src= "https://github.com/hnovak94/SelfBalancingRobot/blob/main/wd.jpeg" height = "400">

### Accelerometer

* Vin: 5V
* GND: Ground
* SDA: SDA
* SCL: SCL


### Driver

* AOUT: wires of the motor, red right, black left
* BOUT: wires of second motor, red right black left
* AIN1: 13
* AIN2: 12
* SLP: 3.3
* BIN1: 2
* BIN2: 6
* GND: Ground


### Motors

* Connect motor one to AOUT and and motor two to BOUT of driver


### Battery Pack

* Two wires connect to driver


## ▷ Code

### Libraries:

* board

* pwmio

* busio

* [adafruit_lsm303](https://github.com/hnovak94/SelfBalancingRobot/blob/main/adafruit_lsm303_accel.mpy)

### Motors

* Test [code](https://github.com/hnovak94/SelfBalancingRobot/blob/main/intromotor)

There are two different digital pins for each motor. They are set as A1, A2 (motor 1), and B1, B2 (motor 2). The difference between the numbers of the two pins determines the speed of the motor. Whichever pin is higher determines the direction e.g. if A1 = 60000 and A2 = 0 then the wheels will spin very quickly (the difference is high) in direction 1. If A1 = 0 and A2 = 60000, then the wheels will spin at the same speed (because the difference between the two numbers is the same) but in the opposite direction. The max number is 65535, which would be the highest speed. If the difference is 0 then the motors will stop spinning. 


### Accelerometer

* Test [code](https://github.com/hnovak94/SelfBalancingRobot/blob/main/introaccel.py)

Because the robot only goes forwards and backwards we are only concerned with the x-value of the accelerometer "accel_x". The range of x should not go lower than -3 or higher than 3. 

### Together

* Test [code](https://github.com/hnovak94/SelfBalancingRobot/blob/main/accelmotor.py)

The x-value must remain in between -3 and +3. Therefore the closer x is to -3 or 3, the faster the wheels need to spin. As x approaches 0, straight up and down, the difference between the two numbers for the motors should appreach 0. When x is zero and the difference between the digital pins is 0 the robot is standing still perfectly upright. 

Initially we tried using a ratio of 1:20. When accel_x = 1 or -1 the difference would be 20000, when accel_x = 2 or -2 the difference would be 40000.


## ▷ Timeline

**WEEK 1:** Project Proposal

**WEEK 2:** The CAD design on Onshape. The design should be relatively simple since it's only 2 parts>

**WEEK 3:** Should have parts by this time. Get everything wired up with the libraries working. I don't want to underestimate the amount of time the libraries will take so this will be pushed to week 4 as well. 

**WEEK 4:** Figure out libraries and begin coding. 

**WEEK 5:** Coding

**WEEK 6:** Coding
