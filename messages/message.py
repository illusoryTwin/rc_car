
from struct import pack, unpack, calcsize

# TODO REMOVE DEPENDENCY ON COMMAND AND REPLY

default_msg_struct = {'cmd_id': ('B', 1),
                      'ticks': ('I', 1),
                      'longitude': ('d', 1),
                      'latitude': ('d', 1),
                      'pos': ('d', 3),
                      'quat': ('f', 4),
                      'gyro': ('f', 3),
                      'depth': ('f', 1)}


class Message:
    def __init__(self,
                 message_struct=default_msg_struct):
        '''Initialize the message type, '''

        self.struct = message_struct

        # initialize structs
        message_format = '<'
        self.slots = self.struct.keys()
        for attribute in self.slots:
            attribute_type = self.struct[attribute][0]
            attribute_size = self.struct[attribute][1]
            message_format += attribute_type * attribute_size
        self.format = message_format
        self.size = calcsize(self.format)
        self.bytes = bytearray(self.size)
        self.attributes = len(self.slots)
        self.unpack()

        self.__message_data = self.attributes*[0]

    def unpack(self):
        '''unpack the message and populate the related attributes'''
        self.data = unpack(self.format, self.bytes)
        attribute_end = 0
        for attribute in self.slots:
            attribute_size = self.struct[attribute][1]
            attribute_start = attribute_end
            attribute_end = attribute_start + attribute_size
            attribute_data = self.data[attribute_start:attribute_end]
            vars(self)[attribute] = attribute_data
        return self

    def pack(self):
        """get the bytes from message"""

        attribute_end = 0
        for attribute in self.slots:
            attribute_size = self.struct[attribute][1]
            attribute_start = attribute_end
            attribute_end = attribute_start + attribute_size
            self.__message_data[attribute_start:attribute_end] = vars(self)[attribute]

        self.data = self.__message_data

        self.bytes = pack(self.format, *self.data)
        return self.bytes
