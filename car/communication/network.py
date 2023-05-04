import socket

IP_ADDRESS = '127.0.0.1'
PORT = 5005
class NetworkManager:
    def __init__(self, 
                 address=IP_ADDRESS,
                 port=PORT, 
                 timeout=0.1, 
                 client = False,
                 recv_size = 1):

        # self.if_settings = if_settings
        # self.interface.active(True)
        # self.interface.ifconfig(self.if_settings)

        self.host = address 
        self.port = port
        self.server_address = (self.host, self.port)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.bytes_rcv = bytearray(recv_size)
        if not client:
            self.sock.bind(self.server_address)
            print(f"UDP socket is binded to {self.host}")
            # self.bytes_rcv = bytearray(recv_size)
            self.address = None
            print('Waiting for connection...')
            self.receive_bytes(recv_size)
            print(f'Got connection to {self.address}')
        else:
            self.address = self.server_address
            
            
        self.timeout = timeout
        self.set_timeout(self.timeout)

    def __del__(self):
        print("Closing connection to the server")
        self.sock.close()

    def send_bytes(self, bytes_snd):
        self.sent = self.sock.sendto(bytes_snd, self.address)

    def receive_bytes(self, size=10):
        try:
            self.bytes_rcv, self.address = self.sock.recvfrom(size)
            self.timeout_exceed = False
        except:
            self.timeout_exceed = True

        return self.bytes_rcv

    def set_timeout(self, timeout=0):
        self.sock.settimeout(timeout)
