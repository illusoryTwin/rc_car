import serial
from struct import pack, unpack
import time 



CMD_SIZE = 6
REPLY_SIZE = 24

port = '/dev/ttyUSB0'

ser = serial.Serial(port, baudrate=57600, bytesize=8, parity='N', stopbits=1, timeout=None)

CMD = 200

STATE_FORMAT = '<BIhhhhhhhhh'
CMD_FORMAT = '<BBhh'

ticks_0 = 0
ts = 0 
FREQ = 0.1


throttle = 12 
steering  = 512
data_to_send = pack(CMD_FORMAT, 
                    CMD,0, 1221,-123)

rcvd_bytes = bytearray(32)

ticks_array = []

try:
    ts = time.perf_counter() 
    ser.write(data_to_send)
    print('sended')
    
    while True:
        if ser.in_waiting > 0:
            rcv = ser.read(1)
            if rcv[0] == 200:
                break
            
    rcvd_bytes = ser.read(REPLY_SIZE-1)
    
    while True:
        
        if time.perf_counter() - ts >= FREQ:
            ser.write(data_to_send)

            while True:
                if ser.in_waiting > 0:
                    rcv = ser.read(1)
                    if rcv[0] == 200:
                        break

            rcvd_bytes = ser.read(REPLY_SIZE - 1)
            data = unpack(STATE_FORMAT, bytearray(rcvd_bytes))
            ticks = data[1]
            
            print(data)
            ticks_0 = ticks
            ts = time.perf_counter() 

        
except KeyboardInterrupt:
    print('Exit by interrupt')
except Exception as e:
    print(e)
finally:
    ser.close()
    # print("SPI closed")
