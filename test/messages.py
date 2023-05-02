
from ..messages.message import Message

# DEFINE MESSAGES STRUCTS
# message struct is the dict with keys as attributes and tuples ('type', size)
# https://docs.python.org/3/library/struct.html for the reference of data types

# B : unsigned char (1 byte)
# h : short  (2 bytes)
# I : unsigned int (4 bytes)
# d : double (8 bytes)
# f : float  (4 bytes)

msg_struct = {'cmd_id': ('B', 1),
              'ticks': ('I', 1),
              'angle': ('f', 1),
              'pwm': ('h', 4),
              'gyro': ('d', 3), }

tx_msg = Message(message_struct=msg_struct)

# we may check the size of message with
print(f'The size of message in bytes: {tx_msg.size}\n')
# in order to populate message just set it's attributes
tx_msg.cmd_id = 4,
tx_msg.ticks = 124125,
tx_msg.angle = 3.5454,
tx_msg.pwm = range(4)
tx_msg.gyro = [-1243.141, 2331.556, 1/3]

# to convert msg to bytes (for instance to send over network) use:
tx_msg.pack()
# now you may find the bytes in .bytes attribute
tx_bytes = tx_msg.bytes 
print(f'The size raw bytes in message: {tx_msg.bytes}\n')


# if you "receive" bytes for this specific msg you may populate its attributes with: 
rx_msg = Message(message_struct=msg_struct)
print(f'Attributes of "received" message before "unpack":')
for key in msg_struct.keys():
    print(f' {key}: {getattr(rx_msg, key)}')
# set bytes to "recived" bytes
rx_msg.bytes = tx_bytes 
rx_msg.unpack()
print(f'\nAttributes of "received" message after "unpack":')
for key in msg_struct.keys():
    print(f' {key}: {getattr(rx_msg, key)}')
