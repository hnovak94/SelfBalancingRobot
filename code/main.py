import time
import board
import pwmio

motorA1 = pwmio.PWMOut(board.D13, frequency=5000, duty_cycle=0)  # contriols speed(?)
motorA2 = pwmio.PWMOut(board.D12, frequency=5000, duty_cycle=0)  # controls direction(?)

while True:
  motorA1.duty_cycle = 20000  # the difference between the two determines the speed.
  motorA2.duty_cycle = 60000  # max is 65535 (2^16), motor stalls when less than ~40000
  time.sleep(1)  # spins in direction one for one second
  motorA1.duty_cycle = 40000. # difference of four thousand same as above. motor turns at same speed.
  motorA2.duty_cycle = 0
  time.sleep(1)  # spins in direction two for one second
