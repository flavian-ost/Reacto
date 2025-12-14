from modulino import ModulinoMovement
movement = ModulinoMovement()
from math import sqrt
from time import sleep_ms

time_count = 0
values = []

while time_count < 50:
  a = movement.accelerometer
  g = movement.gyro
  power = sqrt(a[0]**2 + a[1]**2 + a[2]**2)
  print(power)
  values.append(power)
  time_count += 1
  sleep_ms(100)
print()
best = max(values)
print(best)
score = 100 / 11 * (best + 1)
score_rounded = int(score)
print(f"Your score is {score_rounded}!")
  