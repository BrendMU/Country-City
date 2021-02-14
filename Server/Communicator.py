import socket
import threading
import Constants

class Communicator:
    
    instance = None
    
    def __init__(self):
        super().__init__()
    
        if Communicator.instance is not None:
            raise Exception("Singleton Was Already Created")
        
        Communicator.instance = self
        self.binded = False
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    @staticmethod
    def get_instance():
        if Communicator.instance is None:
            Communicator()
            
        return Communicator.instance   
    
    def bind_and_listen(self):
        if self.binded:
            return 
        
        self.server_socket.bind((Constants.SERVER_ADDRESS, Constants.SERVER_PORT))
        self.server_socket.listen()
        self.binded = True
        
    def start_handling(self):
        if not self.binded:
            self.bind_and_listen()
            
            
        while True:
            
            client_socket, addr = self.server_socket.accept()
            thread = threading.Thread(target=self.handle_client, args=(client_socket,))
            thread.start()            
            
    def handle_client(self, client_socket):
        while True:
            pass
        
        client_socket.close()       
        
