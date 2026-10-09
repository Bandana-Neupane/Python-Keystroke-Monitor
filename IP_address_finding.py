import socket

domain=input("Enter website domain:")
ip=socket.gethostbyname(domain)

print(f"(domain) IP address is:{ip}")
