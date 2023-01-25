import socket

def main():
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect(("192.168.6.128", 8080))
    
  tempFah = input ("Enter temperature in Fahrenheit: ")
  s.send (tempFah.encode())
  tempFah = s.recv(1024).decode()
  print ("Temperature in Celsius: %s" % tempCel)
    
main()
