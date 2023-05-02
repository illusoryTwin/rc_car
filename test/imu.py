
from ..hardware.imu import MPU9250
from time import perf_counter, sleep

try:
    imu = MPU9250()
    while True:
        t1 = perf_counter()
        gyro = imu.readGyro()
        accel = imu.readAccel()
        # magnet = imu.readMagnet()
        t2 = perf_counter()
        print(t2 - t1, accel)
        # sleep(0.001)

except KeyboardInterrupt:
    print('Exit with keyboard interrupt')
