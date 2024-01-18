import socket
import time

def main():
    host = '127.0.0.1'
    port = 5000
    message = b'Hello Server'

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    for _ in range(1000):
        client_socket.sendto(message, (host, port))
        time.sleep(0.01)

if __name__ == '__main__':
    main()
