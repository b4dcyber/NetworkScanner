import nmap

def scan(target, ports="1-1024"):
    scanner = nmap.PortScanner()
    print(f"[+] Scanning {target} on ports {ports}...")
    scanner.scan(target, ports)
    
    for host in scanner.all_hosts():
        print(f"\n[+] Host: {host}")
        print(f"    State: {scanner[host].state()}")
        for proto in scanner[host].all_protocols():
            ports = scanner[host][proto].keys()
            for port in sorted(ports):
                state = scanner[host][proto][port]['state']
                print(f"    Port {port}/{proto}: {state}")

if __name__ == "__main__":
    target = input("Enter target IP or hostname Created By Kashif Ahmed: ")
    scan(target)
