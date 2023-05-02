#### Comunication with Jetson

Wi-fi: InnoRobotiсs // we need to connect exactly to this Wi-Fi then connecting to Jetson on IP: `10.100.20.30`: 
```bash
ssh nvidia@10.100.20.30 
password: nvidia
```




<!-- TERMINAL: //print these commands

ifconfig

ssh nvidia@10.100.20.30 


in vsCode

enter password nvidia<br>

sudo /usr/bin/python3.6 /home/nvidia/rc_car/i2c_test.py<br>
#0x30 <br>

sudo /usr/bin/python3.6 /home/nvidia/rc_car/test_imu.py //acceleration <br> -->


#### Useful links

* I2C in Linux with [I2C utilities](https://linuxhint.com/i2c-linux-utilities/)

* Connection of the [PWM module to Raspberry Pi](https://www.aranacorp.com/en/using-a-pca9685-module-with-raspberry-pi/) and some [code examples](https://learn.adafruit.com/16-channel-pwm-servo-driver/python-circuitpython) 
* Setting [multiple I2C devices](https://www.instructables.com/Raspberry-PI-Multiple-I2c-Devices/) on Raspberry Pi 
* Connecting and [reading from IMU sensor](https://makersportal.com/blog/2019/11/11/raspberry-pi-python-accelerometer-gyroscope-magnetometer) 
* [Headless setup for Jetson](https://www.youtube.com/watch?v=Ch1NKfER0oM&t=560s)
* [Remote development with VS code](https://www.youtube.com/watch?v=ZvVi8FhFpz8) 