import pyfiglet
import socket

ascii_banner = pyfiglet.figlet_format("RX SCANNER")
print(ascii_banner)

# Daftar port yang ingin Anda periksa
common_ports = [80, 22, 21, 443]

# Mendefinisikan target (misalnya, alamat IP atau nama host)
target = input("Masukkan alamat IP atau nama host: ")

# Add Banner
print("-" * 50)
print("Scanning Target: " + target)
print("-" * 50)

try:
    for port in common_ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        # Menghubungkan ke port tertentu
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is open")
        else:
            print(f"Port {port} is closed")
        s.close()

except KeyboardInterrupt:
    print("\nExiting Program")
except socket.gaierror:
    print("\nHostname Could Not Be Resolved")
except socket.error:
    print("\nServer not responding")

