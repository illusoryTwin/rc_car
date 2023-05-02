from smbus import SMBus 

bus = SMBus(0)

data = bus.read_byte_data(0x50, 0x55)
print(hex(data))
bus.close()