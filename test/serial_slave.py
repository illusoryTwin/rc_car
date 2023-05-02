import serial
from struct import pack, unpack
from time import perf_counter, sleep

CMD_SIZE = 6
REPLY_SIZE = 24

port = '/dev/ttyUSB0'

ser = serial.Serial(port, baudrate=57600, bytesize=8,
                    parity='N', stopbits=1, timeout=None)

CMD = 200

STATE_FORMAT = '<BBIhhhhhhhhh'
CMD_FORMAT = '<BBhh'

ticks_0 = 0
ts = 0
FREQ = 0.000001


recv_buf = bytearray(CMD_SIZE)


# print('Press any key to continue...')
# input()
# cmd_cntrl = TORQUE_CMD
no_rcv_count = 0

desired_torques = [0, 0]
tick_0 = perf_counter()
try:
    # STATE_FORMAT
    cmd = 200  # 1 byte
    error_code = 0  # 1 bytes
    tick = 0  # 4 bytes

    while True:
        tick = int((perf_counter() - tick_0)*1E6)
        # sleep(0.1)
        # sleep_us(100)
        # -------------------
        # STATE OF DEVICE
        # -------------------
        accel_x = 134
        yaw_angle = 5476
        angular_speed = 242
        position_x = 1234
        position_y = 35
        speed_x = -124
        speed_y = 1234
        alt = 1241
        lt = 2112

        while True:
            if ser.in_waiting > 0:
                no_rcv_count = 0
                rcv = ser.read(1)
                # print(rcv)
                if rcv[0] == 200:

                    state_bytes = pack(STATE_FORMAT,
                                       rcv[0],
                                       error_code,
                                       tick,
                                       accel_x,
                                       yaw_angle,
                                       angular_speed,
                                       position_x,
                                       position_y,
                                       speed_x,
                                       speed_y,
                                       alt,
                                       lt)

                    send_bytes = state_bytes
                    rcv_bytes = ser.read(CMD_SIZE - 1)
                    rcv_data = unpack(CMD_FORMAT, rcv + rcv_bytes)

                    steering = rcv_data[2]
                    throttle = rcv_data[3]
                    print(steering, throttle)

                    ser.write(send_bytes)

                    break
            else:
                no_rcv_count += 1
                if no_rcv_count >= 10:
                    steering = 0
                    throttle = 0
                    # print('No cmd')
                break
        # print(desired_torques)
                # print('No command')
                # NO COMMAND RECEIVED
        # tick2 = ticks_us()
        # print(tick2 - tick)


except KeyboardInterrupt:
    print('Exit by interrupt')
# except Exception as e:
#     print(e)
finally:

    ser.close()
