import socket
import threading                                                       
host_port =  int(input("Enter host_port_no: "))

def sender():
    ip = input("Enter reciever_ip :")
    port = int(input("Enter rec_port_no:"))
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
       data = input("\nSend message:").encode()
       s.sendto(data, (ip, port) )


def reciever():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    host_ip = ""
    sock.bind( (host_ip , host_port) )
    while True:
       data = sock.recvfrom(1024)

       Text_data = data[0]
       msg = Text_data.decode()
       print("\nRecieve message:", msg)

t1 = threading.Thread(target=sender)
t2 = threading.Thread(target=reciever)

t1.start()
t2.start()
