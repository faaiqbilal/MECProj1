import socket
import sys

host = "185.233.18.22"
port =  15555
addr = (host, port)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(addr)