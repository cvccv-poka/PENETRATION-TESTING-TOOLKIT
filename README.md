# PENETRATION-TESTING-TOOLKIT

*COMPANY*: CODTECH IT SOLUTIONS 

*NAME* : VIVEK KUMBHAKAR

*INTERN ID* :CT04DF361

*DOMAIN* : CYBERSECURITY AND ETHICAL HACKING

*DURATION* : 4 WEEKS

*MENTOR* : NEELA SANTOSH

##Project Description
The field of penetration testing requires a diverse set of tools to identify and exploit vulnerabilities across various systems and networks. This project, the Penetration Testing Toolkit, serves as a foundational step towards building a comprehensive suite of security assessment tools. It encapsulates multiple modules designed to perform specific reconnaissance and attack simulations, providing hands-on experience with fundamental penetration testing techniques.

The problem this toolkit addresses is the need for specialized utilities during a security assessment. Instead of relying on numerous disparate tools, a consolidated toolkit allows for a streamlined workflow and provides a deeper understanding of the underlying mechanisms of different attack vectors. For instance, before attempting to log into a service, an attacker or a penetration tester needs to know if the service is running (port scanning) and then, if authenticated access is required, they might attempt to guess credentials (brute-forcing). This toolkit brings these essential capabilities under one roof.

The importance of a penetration testing toolkit extends beyond merely finding vulnerabilities; it's about understanding system weaknesses from an attacker's perspective. It helps in:

Reconnaissance: Discovering open ports and services, which are potential entry points.

Authentication Testing: Identifying weak credentials through systematic guessing attempts.

Skill Development: Providing a practical environment to implement and comprehend common attack methodologies.

Security Posture Improvement: By simulating attacks, organizations can proactively identify and patch weaknesses before malicious actors exploit them.

This project offers a pragmatic introduction to the world of ethical hacking and cybersecurity operations, emphasizing modularity and functional specialization.

Features & Functionality
This Python-based Modular Penetration Testing Toolkit currently includes two core modules:

Port Scanner Module:

Purpose: To identify open ports on a target host, revealing which services might be running and accessible.

Functionality:

Takes a target IP address or hostname and a range of ports (start and end port) as input.

Utilizes raw socket programming to attempt TCP connections to each port within the specified range.

Employs threading to perform scans concurrently, significantly speeding up the scanning process.

Reports all open ports found, indicating potential attack vectors or services to further investigate.

Includes a timeout mechanism to prevent the scanner from hanging on unresponsive ports.

Web Brute-Forcer Module:

Purpose: To discover weak login credentials (usernames and passwords) by systematically trying combinations from a provided wordlist. This is a common technique against login forms.

Functionality:

Functionality:

Takes a target IP address or hostname and a range of ports (start and end port) as input.

Utilizes raw socket programming to attempt TCP connections to each port within the specified range.

Employs threading to perform scans concurrently, significantly speeding up the scanning process.

Reports all open ports found, indicating potential attack vectors or services to further investigate.

Includes a timeout mechanism to prevent the scanner from hanging on unresponsive ports.

Web Brute-Forcer Module:

Purpose: To discover weak login credentials (usernames and passwords) by systematically trying combinations from a provided wordlist. This is a common technique against login forms.

Functionality:

Targets a specific login URL (e.g., a web application's login page).

Requires the names of the HTML input fields for username and password (e.g., username, pass).

Takes a path to a wordlist file containing potential passwords.

Defaults to a common username (e.g., admin) and iterates through the provided password wordlist.

Submits login attempts using HTTP POST requests (or GET, depending on the form method).

Analyzes the web server's response for a specified "success indicator" string (e.g., "Welcome", "Logout", "Dashboard") to determine if a login attempt was successful.

Also employs threading to accelerate the brute-forcing process, allowing multiple password attempts to be made simultaneously.

Reports the first set of valid credentials found.

Technologies Used
Python 3.x: The foundational programming language.

socket Module: A low-level, built-in Python module used by the Port Scanner for direct network communication (TCP connections) to probe ports.

requests Library: An HTTP library for Python, utilized by the Web Brute-Forcer for making HTTP POST/GET requests to web applications during login attempts.

threading Module: A built-in Python module essential for concurrent execution, allowing both the Port Scanner and the Brute-Forcer to perform tasks in parallel (scanning multiple ports or trying multiple passwords simultaneously), drastically improving performance.

sys Module: Used for handling command-line arguments, enabling flexible module selection and input for the toolkit.

collections Module (deque): Used in the Brute-Forcer for efficient management of the password queue.

File I/O: For reading wordlists in the brute-forcer.
Clone the Repository:

Bash

git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name/Task3_PenetrationToolkit
Install Dependencies:

Bash

pip install requests
Prepare Wordlist (for Brute-Forcer):
Create a passwords.txt file (or any other name) in the same directory, with one password per line.

# passwords.txt
password123
admin
123456
...
Run Modules:
IMPORTANT: Only scan and brute-force targets you have explicit permission to test (e.g., your own local machines, test networks, or deliberately vulnerable applications like DVWA/bWAPP). Unauthorized testing is illegal and unethical.

Port Scanner:

Bash

python toolkit.py portscan <target_host_ip_or_hostname> <start_port> <end_port>
# Example: python toolkit.py portscan localhost 1 1000
# Example: python toolkit.py portscan scanme.nmap.org 20 100
Web Brute-Forcer:

Bash

python toolkit.py bruteforce <target_login_url> <username_field_name> <password_field_name> <wordlist_file>
# Example: python toolkit.py bruteforce http://localhost/DVWA/login.php username password passwords.txt
Learning Outcomes & Concepts Demonstrated
This project offers hands-on experience and strengthens understanding of:

Network Fundamentals: Basic TCP/IP communication and port concepts.

Concurrency/Threading: Implementing multithreading to improve tool efficiency and performance.

Service Discovery: The importance of identifying open ports and services in reconnaissance.

Authentication Attacks: Understanding the mechanics of brute-force attacks against login mechanisms.

HTTP Interactions: Making POST/GET requests to interact with web forms.

Authentication Attacks: Understanding the mechanics of brute-force attacks against login mechanisms.

HTTP Interactions: Making POST/GET requests to interact with web forms.

Modular Tool Development: Designing and implementing a toolkit with distinct, reusable components.

Ethical Hacking Methodologies: Practical application of reconnaissance and password guessing techniques.

Error Handling: Robustly managing network and file system errors.

This toolkit serves as a fundamental building block for aspiring penetration testers, providing practical insight into common security assessment techniques.
Modular Tool Development: Designing and implementing a toolkit with distinct, reusable components.

How to Run / Usage

