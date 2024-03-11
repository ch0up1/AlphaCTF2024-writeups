import socket
import string
import random
from extend_mt19937_predictor import ExtendMT19937Predictor
from Crypto.Util.number import bytes_to_long,long_to_bytes
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import re
# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the server's address and port
server_address = ('35.228.220.66', 1200)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(server_address)
response = client_socket.recv(10000000000)
response = response.decode()
response = response.split("\n")
enc = int(response[-2].replace('enc=',''))
numbers = response[0:78]

predictor = ExtendMT19937Predictor()

for n in numbers:
    n = int(n)
    predictor.setrandbits(n, 256)
    
for _ in range(23):
    key = predictor.predict_getrandbits(256)
    
key = key.to_bytes(32, 'little')
iv = b"alpha_gift_for_u"
enc = long_to_bytes(enc)
cipher = AES.new(key, AES.MODE_CBC, iv)
dec = cipher.decrypt(pad(enc,AES.block_size))    
dec = str(dec)
pattern = r'AlphaCTF\{.*\}'
flag = re.search(pattern, dec)

print('The Flag : ',flag.group(0))




        


            
    