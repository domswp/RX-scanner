import pyfiglet
import socket

def display_menu():
    print("[1] Melihat IP dari sebuah DNS")
    print("[2] Port Scanning")
    print("[0] Keluar")

def dns_lookup():
    target = input("Masukkan nama host (DNS): ")
    try:
        ip_address = socket.gethostbyname(target)
        print(f"Alamat IP dari {target} adalah {ip_address}")
    except socket.gaierror:
        print("Hostname tidak dapat diresolusi.")

def port_scanning():
    # Daftar port yang ingin Anda periksa
    common_ports = [80, 22, 21, 443]

    # Mendefinisikan target (misalnya, alamat IP atau nama host)
    target = input("Masukkan alamat IP atau nama host: ")

    try:
        # Add Banner
        print("-" * 50)
        print("Scanning Target: " + target)
        print("-" * 50)

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
        print("\nHostname tidak dapat diresolusi.")
    except socket.error:
        print("\nServer tidak merespons.")

if __name__ == "__main__":
    ascii_banner = pyfiglet.figlet_format("RX-SCANNER")
    print(ascii_banner)

    while True:
        display_menu()
        choice = input("Pilih menu [1/2/0]: ")

        if choice == "1":
            dns_lookup()
        elif choice == "2":
            port_scanning()
        elif choice == "0":
            print("Keluar.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih kembali.")

