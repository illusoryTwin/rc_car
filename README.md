# car

Wi-fi: InnoRobotiсs // we need to connect exactly to this Wi-Fi
Jetson IP: 10.100.20.30 
(password: nvidia)

TERMINAL: //print these commands
ifconfig
ssh nvidia@10.100.20.30 


vsCode

enter password nvidia
sudo /usr/bin/python3.6 /home/nvidia/rc_car/i2c_test.py //0x30
sudo /usr/bin/python3.6 /home/nvidia/rc_car/test_imu.py //acceleration
