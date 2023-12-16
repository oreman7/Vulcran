import curses
import socket
import ipinfo
import requests
import nmap
import webbrowser
import random

def print_banner(stdscr):
    stdscr.clear()
    stdscr.refresh()
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(6, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(7, curses.COLOR_WHITE, curses.COLOR_BLACK)

    stdscr.attron(curses.color_pair(random.randint(1, 7)) | curses.A_BOLD)
    banner = """
     
 ██▒   █▓ █    ██  ██▓     ▄████▄   ██▀███   ▄▄▄      
▓██░   █▒ ██  ▓██▒▓██▒    ▒██▀ ▀█  ▓██ ▒ ██▒▒████▄    
 ▓██  █▒░▓██  ▒██░▒██░    ▒▓█    ▄ ▓██ ░▄█ ▒▒██  ▀█▄  
  ▒██ █░░▓▓█  ░██░▒██░    ▒▓▓▄ ▄██▒▒██▀▀█▄  ░██▄▄▄▄██ 
   ▒▀█░  ▒▒█████▓ ░██████▒▒ ▓███▀ ░░██▓ ▒██▒ ▓█   ▓██▒
   ░ ▐░  ░▒▓▒ ▒ ▒ ░ ▒░▓  ░░ ░▒ ▒  ░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░
   ░ ░░  ░░▒░ ░ ░ ░ ░ ▒  ░  ░  ▒     ░▒ ░ ▒░  ▒   ▒▒ ░
     ░░   ░░░ ░ ░   ░ ░   ░          ░░   ░   ░   ▒   
      ░     ░         ░  ░░ ░         ░           ░  ░
     ░                    ░                           

    """
    stdscr.addstr(2, 2, banner)
    stdscr.attroff(curses.color_pair(random.randint(1, 7)) | curses.A_BOLD)
    stdscr.refresh()

def port_scan(target_host):
    import socket

def port_scan(target_host, start_port, end_port):
    try:
        target_ip = socket.gethostbyname(target_host)
        print(f"Scanning ports {start_port} to {end_port} on {target_host} ({target_ip})...")

        for port in range(start_port, end_port + 1):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)  # Adjust timeout as needed
            result = sock.connect_ex((target_ip, port))
            if result == 0:
                print(f"Port {port}: Open")
            else:
                print(f"Port {port}: Closed")
            sock.close()
    except socket.error as e:
        print(f"Error: {e}")

    pass

def subnet_scan():
    import ipaddress
import subprocess

def subnet_scan(subnet):
    try:
        network = ipaddress.ip_network(subnet)
        print(f"Scanning subnet: {subnet}...")

        for host in network.hosts():
            host = str(host)
            
            result = subprocess.call(['ping', '-c', '1', host])
            if result == 0:
                print(f"Host {host}: Alive")
            else:
                print(f"Host {host}: Not reachable")
    except ValueError as e:
        print(f"Error: {e}")

    pass

def ip_geolocation(ip):
    import ipinfo

def ip_geolocation(ip):
    try:
        access_token = 'YOUR_IPINFO_API_TOKEN'  
        handler = ipinfo.getHandler(access_token)
        details = handler.getDetails(ip)

        print(f"IP: {ip}")
        print(f"City: {details.city}")
        print(f"Region: {details.region}")
        print(f"Country: {details.country_name}")
    except ipinfo.exceptions.IPInfoError as e:
        print(f"Error: {e}")

    pass

def dos_attack(target_host):
    # Implement DoS attack lo
    pass

def vulnerability_scan(target_host):
    import nmap

def vulnerability_scan(target_host):
    try:
        scanner = nmap.PortScanner()
        print(f"Scanning for vulnerabilities on {target_host}...")

        scanner.scan(target_host, arguments='-sV')  

        for host in scanner.all_hosts():
            print(f"Host: {host}")
            for proto in scanner[host].all_protocols():
                print(f"Protocol: {proto}")
                ports = scanner[host][proto].keys()
                for port in ports:
                    state = scanner[host][proto][port]['state']
                    service = scanner[host][proto][port]['name']
                    print(f"Port: {port}\tState: {state}\tService: {service}")
    except nmap.PortScannerError as e:
        print(f"Nmap error: {e}")

    pass

def kitty_gif():
    import webbrowser
import random

def display_kitty_gif():
    # URLs of kitty GIFs
    kitty_gifs = [
        "https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif",
        "https://media.giphy.com/media/WYEWpk4lRPDq0/giphy.gif",
        "https://media.giphy.com/media/jRt5zOvpEh7Yk/giphy.gif",
        # Add more kitty GIF URLs here
    ]

    # Select a random kitty GIF URL
    random_kitty_gif = random.choice(kitty_gifs)

    # Open the random kitty GIF in the default web browser
    webbrowser.open(random_kitty_gif)

# Example usage:
display_kitty_gif()

    pass

def additional_feature_1():
    # Implement additional feature 1 logic here
    pass

def additional_feature_2():
    # Implement additional feature 2 logic here
    pass

def main(stdscr):
    curses.curs_set(0)  # Hide cursor

    print_banner(stdscr)

    options = [
        "Port Scanning",
        "Subnet Scanning",
        "IP Geolocation",
        "DoS",
        "Vulnerability Scanner",
        "Cute Silly Cat",
        "Additional Feature 1",
        "Additional Feature 2",
        
    ]

    while True:
        stdscr.addstr(10, 2, "Select an option:", curses.A_BOLD)
        for idx, opt in enumerate(options):
            stdscr.attron(curses.color_pair(random.randint(1, 7)))
            stdscr.addstr(12 + idx, 4, f"{idx + 1}. {opt}")
            stdscr.attroff(curses.color_pair(random.randint(1, 7)))
        stdscr.addstr(len(options) + 14, 2, "Press Q to quit.")
        stdscr.refresh()

        key = stdscr.getch()
        if key == ord('q') or key == ord('Q'):
            break
        elif key == ord('1'):
            target_host = input("Enter target IP/host for port scanning: ")
            port_scan(target_host)
        elif key == ord('2'):
            subnet_scan()
        elif key == ord('3'):
            target_ip = input("Enter IP for geolocation: ")
            ip_geolocation(target_ip)
        elif key == ord('4'):
            target_host = input("Enter target IP/host for DoS attack: ")
            dos_attack(target_host)
        elif key == ord('5'):
            target_host = input("Enter target IP/host for vulnerability scan: ")
            vulnerability_scan(target_host)
        elif key == ord('6'):
            kitty_gif()
        elif key == ord('7'):
            additional_feature_1()
        elif key == ord('8'):
            additional_feature_2()
        

curses.wrapper(main)
