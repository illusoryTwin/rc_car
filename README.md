### Autonomous RC Car

This repository is devoted to the development of an autonomous RC Car that is equipped with navigation features such as GPS, a compass, gyroscopes, and accelerometers (IMU). 

<!-- These components allow the car to make quick and accurate navigational decisions in order to reach its destination with minimal input from the user. Furthermore, the car's autonomous capabilities are enhanced by its ability to process data from its environment in real-time. -->

#### The Structure of Repository
The code is organized as follows:

```bash
├── communication # communication modules
│   ├── network.py # manager for network
│   └── serial.py # serial manager
├── hardware # hardware interfaces 
│   ├── gps.py
│   ├── ...
│   └── servo.py
├── messages # the module to facilitate messages 
│   ├── message.py
│   ├── ...
│   └── struct.py # the message structures
└── tests # scripts to test different modules
    ├── client.py
    ├── imu.py
    ├── ...
    ├── client.py
    └── server.py
```
