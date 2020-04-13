import socket
import _thread
import time
soc = socket.socket()

class server:
    def __init__(self):
        self.clients = []
        import socket
        import _thread
        self.host = '127.0.0.1'
        self.port = 8887
        soc = socket.socket()
        self.buffer_size = 1024
        soc.bind((self.host, self.port))
        soc.listen(5)
        self.server_init_(soc)


        
    def send_thread(self, connection, x):
        print('send %s' % x ,'to', connection)
        
        connection.sendall(x.encode())
        print('done')
        _thread.exit()

        
    def server_init_(self, soc):
        while True:
            connection, address = soc.accept()
            self.clients += [connection]
            print(address, 'is connected')
            _thread.start_new_thread(self.new_thread, (connection, address,))
            time.sleep(1)

            
    def new_thread(self, connection, address):
        print(address)
        while True:
            out = connection.recv(self.buffer_size).decode()
            print(out, address)
            
            for i in self.clients:
                if not i == connection:
                    _thread.start_new_thread(self.send_thread, (i, out,))
            
server()
