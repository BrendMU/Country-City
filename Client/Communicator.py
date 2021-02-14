import socket
import Constants

class Communicator:
    
    instance = None
    
    def __init__(self):
        super().__init__()
    
        if Communicator.instance is not None:
            raise Exception("Singleton Was Already Created")
        
        Communicator.instance = self
        self.connected = False
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    @staticmethod
    def get_instance():
        if Communicator.instance is None:
            Communicator()
            
        return Communicator.instance   
    
    def connect(self):
        if self.connected:
            return 
        
        self.client_socket.connect((Constants.SERVER_ADDRESS, Constants.SERVER_PORT))
        
    def send_data(self):
        if not self.connected:
            self.connect()
        
        self.client_socket.send("greate".encode())

        
        