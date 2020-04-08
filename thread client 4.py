import socket
import sys

def main():
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "127.0.0.1"
    port = 8888

    try:
        soc.connect((host, port))
    except:
        print("Connection error")
        sys.exit()

    print("Enter 'quit' to exit")
    
    soc.sendall('ACK'.encode("utf8"))
    back = ''
    while back != 'quit':
        
        back = soc.recv(5120).decode("utf8")
        print(back)
          

        

    soc.send(b'--quit--')

if __name__ == "__main__":
    main()
