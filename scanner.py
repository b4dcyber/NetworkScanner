import subprocess

def run_nmap(target):
    try:
        result = subprocess.check_output(['nmap', '-sV', target], stderr=subprocess.STDOUT, text=True)
        print(result)
    except subprocess.CalledProcessError as e:
        print(f"[!] Error: {e.output}")

if __name__ == "__main__":
    target_ip = input("Enter target IP or domain Created By Kashif Ahmed: ")
    run_nmap(target_ip)
