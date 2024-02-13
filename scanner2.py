#!/bin/python3

import socket

def print_banner():
    banner = """
    ######################################
    #      ChatGPT Port Scanner          #
    ######################################
    """
    print(banner)

def scan_ports(target, start_port, end_port):
    print_banner()
    print(f"Scanning ports on {target}...")

    open_ports = []

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((target, port))

        if result == 0:
            open_ports.append(port)
            sock.close()

    if open_ports:
        print("\nOpen ports:")
        for port in open_ports:
            print(f"Port {port} is open")
    else:
        print("\nNo open ports found.")

if __name__ == "__main__":
    target_ip = input("Enter the target IP address: ")
    start_port = int(input("Enter the starting port: "))
    end_port = int(input("Enter the ending port: "))

    scan_ports(target_ip, start_port, end_port)
