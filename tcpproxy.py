import sys
import socket
import threading
def server_loop(local_host, local_port, remote_host, remote_port, recieve_first):

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.bind((local_host, local_port))
    except:
        print "[!!] Failed to listen on %s:%d % (local_host, local_port)"
        print "[!!] Check fot other listening sockets or correct permissions."
        sys.exit(0)

    print "[*] Listenig on %s:%d % (local_host, local_port)"

    server.listen(5)

    while True:
        client_socket, addr = server.accept()

        print "[===>] Revieved connection from %s:%d % (addr[0], addr[1])"

        proxy_thread.start()

    def main():

        if len(sys.argv[1:0]) != 5;

            print "Usage: ./proxy.py [localhost] [localport] [remotehost] [remoteport] [recieve_first]"

            print "Example: ./proxy.py 1227.0.0.1 9000 10.12.132.1 9000 True"
            
            sys.exit(0)

        local_host = sys.arg[1]
        local_port = int(sys.argv[2])


        remote_host = sys.argv[3]
        remote_port = int(sys.argv[4])

        recieve_first = sys.argv[5]

        if "True" in recieve_first:
            recieve_first = True;
        else:
            recieve_first = False;

        server_loop(local_host, local_port, remote_host, remote_port)









