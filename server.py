from time import perf_counter
from manager import NetworkManager
from messages import Message
from protocol import cmd_msg_struct, reply_msg_struct

# IP_ADDRESS = '127.0.0.1'
# PORT = 5005

network_manager = NetworkManager(client = False, 
                                 timeout=0.1)
udp_commands = Message(message_struct = cmd_msg_struct)
udp_reply = Message(message_struct = reply_msg_struct)

try:


    armed = True
    t0 = perf_counter()

    while True:
        t = perf_counter() - t0 

        # recive bytes and populate bytes of msg udp_commands
        udp_commands.bytes = network_manager.receive_bytes(udp_commands.size)

        # if there is bytes in message - unpack 
        if udp_commands.size == len(udp_commands.bytes):
            udp_commands.unpack()
        
        if network_manager.timeout_exceed:

            # if timeout exceeds - do something...
            print('[SERVER], there is no new udp_commands from UDP for timeout disarming vehicle!')
            armed = False
        else:
            # if timeout is not exceeds send message back
        
            # populate reply message  
            udp_reply.ticks = int(1000*t), 
            udp_reply.position = [0.2131, 1.12]
            udp_reply.gyro = [0.1256,12.431,54.112]
            udp_reply.accel = [0.1256,12.431,54.112]
            # pack message 
            udp_reply_bytes = udp_reply.pack()
            network_manager.send_bytes(udp_reply_bytes)
            

except Exception as e:
    print("Other exception: %s" % str(e))
except KeyboardInterrupt:
    print('Interrupted by user...')
finally:
    # DO SOMETHING IN END - TURNOFF VEHICLE 
    print('Exit....')
    
