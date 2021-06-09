import adafruit_lsm303
import board
import time
import pwmio
import busio

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_lsm303.LSM303(i2c)
motorA1 = pwmio.PWMOut(board.D13, frequency=5000, duty_cycle=0)
motorA2 = pwmio.PWMOut(board.D12, frequency=5000, duty_cycle=0)

motorB1 = pwmio.PWMOut(board.D2, frequency=5000, duty_cycle=0)
motorB2 = pwmio.PWMOut(board.D6, frequency=5000, duty_cycle=0)

while True:

    raw_accel_x, raw_accel_y, raw_accel_z = sensor.raw_acceleration
    accel_x, accel_y, accel_z = sensor.acceleration
    raw_mag_x, raw_mag_y, raw_mag_z = sensor.raw_magnetic
    mag_x, mag_y, mag_z = sensor.magnetic
    print((accel_x, accel_y))
    # print('Acceleration raw: ({0:6d}, {1:6d}, {2:6d}), (m/s^2): ({3:10.3f}, {4:10.3f}, {5:10.3f})'.format(raw_accel_x, raw_accel_y, raw_accel_z, accel_x, accel_y, accel_z))
    # print('Magnetometer raw: ({0:6d}, {1:6d}, {2:6d}), (gauss): ({3:10.3f}, {4:10.3f}, {5:10.3f})'.format(raw_mag_x, raw_mag_y, raw_mag_z, mag_x, mag_y, mag_z))
    # print('')
    time.sleep(.2)

    # the difference between the two determines the speed.
    # whichever pin is higher determines the direction
    # max is 65535 (2^16), motor stalls when less than ~40000
    # difference of 0, it stops
    # difference 40000+ increases speed as difference increases

    motorA1.duty_cycle = 0
    motorB1.duty_cycle = 0

    motorA2.duty_cycle = 60000
    motorB2.duty_cycle = 60000
    print("spins fast in d1")
    time.sleep(1)

    motorA1.duty_cycle = 0
    motorB1.duty_cycle = 0

    motorA2.duty_cycle = 0
    motorB2.duty_cycle = 0
    print("stops")
    time.sleep(1)

    motorA1.duty_cycle = 60000
    motorB1.duty_cycle = 60000

    motorA2.duty_cycle = 0
    motorB2.duty_cycle = 0
    print("spins fast in d2")
    time.sleep(1)

    # x accel
    # -3 -------- 0 ---------- +3
    # wheel speed
    # try multiplying by 20000
    # if x is 1 then diff is 20000
    # if x is 2 then diff is 40000, etc
    # -60000 ---- 0 ---------- +60000

