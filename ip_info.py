import socket
import requests
import sys
import time
import dns.resolver
from colorama import Fore, init

init(autoreset=True)

def print_banner():
    print(f"""
{Fore.RED} 
██▓ ██▓███      ██▓ ███▄    █   █████▒▒█████  
▓██▒▓██░  ██▒   ▓██▒ ██ ▀█   █ ▓██   ▒▒██▒  ██▒
▒██▒▓██░ ██▓▒   ▒██▒▓██  ▀█ ██▒▒████ ░▒██░  ██▒
░██░▒██▄█▓▒ ▒   ░██░▓██▒  ▐▌██▒░▓█▒  ░▒██   ██░
░██░▒██▒ ░  ░   ░██░▒██░   ▓██░░▒█░   ░ ████▓▒░
░▓  ▒▓▒░ ░  ░   ░▓  ░ ▒░   ▒ ▒  ▒ ░   ░ ▒░▒░▒░ 
 ▒ ░░▒ ░         ▒ ░░ ░░   ░ ▒░ ░       ░ ▒ ▒░ 
 ▒ ░░░           ▒ ░   ░   ░ ░  ░ ░   ░ ░ ░ ▒  
 ░               ░           ░            ░ ░  
    """)

def print_usage():
    print(f"""
{Fore.YELLOW}Usage: python3 main.py <domain>
Example: python3 main.py example.com
""")

def get_ip_info(domain):
    try:
        ipv4 = socket.gethostbyname(domain)
        try:
            ipv6_info = socket.getaddrinfo(domain, None, socket.AF_INET6)
            ipv6 = ipv6_info[0][4][0] if ipv6_info else "Not Available"
        except:
            ipv6 = "Not Available"
        return ipv4, ipv6
    except socket.gaierror:
        return "Not Available", "Not Available"

def get_geo_info(ip):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = response.json()
        if data['status'] == 'success':
            return {
                'City': data.get('city', 'Not Available'),
                'Region': data.get('regionName', 'Not Available'),
                'Latitude': data.get('lat', 'Not Available'),
                'Longitude': data.get('lon', 'Not Available'),
                'Time Zone': data.get('timezone', 'Not Available'),
                'ISP': data.get('isp', 'Not Available'),
                'Organization': data.get('org', 'Not Available'),
                'AS': data.get('as', 'Not Available')
            }
        return {"Error": "Unable to fetch geo information"}
    except:
        return {"Error": "Unable to fetch geo information"}

def get_dns_info(domain):
    try:
        ns_records = [str(rdata) for rdata in dns.resolver.resolve(domain, 'NS')]
        return ns_records if ns_records else ["Not Available"]
    except:
        return ["Not Available"]

def main():
    print_banner()
    
    if len(sys.argv) != 2:
        print_usage()
        sys.exit(1)
    
    domain = sys.argv[1]
    print(f"{Fore.RED}\n[Processing...]")
    time.sleep(1)
    
    ipv4, ipv6 = get_ip_info(domain)
    geo_info = get_geo_info(ipv4) if ipv4 != "Not Available" else {}
    dns_info = get_dns_info(domain)
    
    print(f"{Fore.RED}=" * 50)
    print(f"Hasil Pemeriksaan:")
    print(f"{Fore.RED}=" * 50)
    
    print(f"IP Address:")
    print(f"  IPv4: {ipv4}")
    print(f"  IPv6: {ipv6}")
    
    print(f"\nInformasi Geografis:")
    for key, value in geo_info.items():
        print(f"  {key}: {value}")
    
    print(f"\nDNS Information:")
    for i, ns in enumerate(dns_info, 1):
        print(f"  Name Server {i}: {ns}")
    
    print(f"{Fore.RED}=" * 50)
    print(f"Scan Selesai!")
    print(f"{Fore.RED}=" * 50)

if __name__ == "__main__":
    main()
