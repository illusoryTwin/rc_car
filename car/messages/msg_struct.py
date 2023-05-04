# DEFINE MESSAGES STRUCTS
# message struct is the dict with kyes as atributes and tuples ('type', size)
# https://docs.python.org/3/library/struct.html for the reference of data types

# B : unsigned char (1 byte)
# h : short  (2 bytes)
# I : unsigned int (4 bytes)
# d : double (8 bytes)
# f : float  (4 bytes)

cmd_msg_struct = {'cmd_id': ('B', 1),
                  'arm': ('B', 1),
                  'ticks': ('I', 1),
                  'motor_velocity': ('f', 1),
                  'steering_angle': ('f', 1),
                  'lights': ('B', 1),
                  'pwm': ('h', 8),
                  'camera_tilt': ('h', 1), }

reply_msg_struct = {'cmd_id': ('B', 1),
                    'mode': ('B', 1),
                    'ticks': ('I', 1),
                    'longitude': ('d', 1),
                    'latitude': ('d', 1),
                    'position': ('d', 2),
                    'heading': ('d', 1),
                    'quat': ('f', 4),
                    'gyro': ('f', 3),
                    'accel': ('f', 3)}
