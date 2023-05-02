from manager import NetworkManager
from messages import Message
from protocol import cmd_msg_struct, reply_msg_struct

# IP_ADDRESS = '127.0.0.1'
# PORT = 5005

network_manager = NetworkManager(client = True)

udp_commands = Message(message_struct = cmd_msg_struct)
udp_reply = Message(message_struct = reply_msg_struct)

try:
    while True:
        # recive bytes and populate bytes of msg udp_commands
        udp_commands.arm = 1, 
        udp_commands.motor_velocity = 213.54, 
        udp_commands.steering_angle = 12.3,
        network_manager.send_bytes(udp_commands.pack())

        udp_reply.bytes = network_manager.receive_bytes(udp_reply.size)

        # if there is bytes in message - unpack 
        if udp_reply.size == len(udp_reply.bytes):
            udp_reply.unpack()
            print(udp_reply.ticks, udp_reply.position)
        

            

except Exception as e:
    print("Other exception: %s" % str(e))
except KeyboardInterrupt:
    print('Interrupted by user...')
finally:
    # DO SOMETHING IN END - TURNOFF VEHICLE 
    print('Exit....')
    
