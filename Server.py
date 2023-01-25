import socket

def main():
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.bind(("192.168.6.128", 8080))
  s.listen(1)
  
  while True:
    csock, addr = s.accept()
    print ("Got a connection from %s" % str(addr))
    
    tempCel = fahrenheit_celsius (float(csock.recv(1024).decode()))
    tempCel = round(tempCel, 2)
    tempCel + str(tempCel)
    csock.sendall (tempCel.encode())

def fahrenheit_celsius(tempFah):
  tempCel = (tempFah - 32) * (5/9)
  return tempCel
  
main()
