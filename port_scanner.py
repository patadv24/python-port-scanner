"""
Python Port Scanner v1.0

Author: Advait Pathak

Features:
- TCP Port Scanning
- Dynamic Port Range
- Service Identification
- Banner Grabbing
- Input Validation

For educational and authorized testing purposes only.
"""

# LOGIC:
# Input -> Validation -> Loop -> Create Socket -> Set Timeout
# -> Connect -> Check -> Banner Grab -> Print -> Close


import socket

services = {

    20: "FTP Data Transfer",
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    67: "DHCP Server",
    68: "DHCP Client",
    69: "TFTP",
    80: "HTTP",
    110: "POP3",
    123: "NTP",
    135: "MS RPC",
    137: "NetBIOS Name Service",
    138: "NetBIOS Datagram Service",
    139: "NetBIOS Session Service",
    143: "IMAP",
    161: "SNMP",
    179: "BGP",
    389: "LDAP",
    443: "HTTPS",
    445: "SMB",
    465: "SMTPS",
    514: "Syslog",
    587: "SMTP Submission",
    636: "LDAPS",
    993: "IMAPS",
    995: "POP3S",
    1433: "MSSQL",
    1521: "Oracle DB",
    3306: "MySQL",
    3389: "RDP",
    5432: "PostgreSQL",
    5900: "VNC",
    8080: "HTTP Alternate"

}

try:

    # INPUTS
    start_port = int(input("Enter the Starting Port Number: "))
    end_port = int(input("Enter the Ending Port Number: "))

    # LOGICAL VALIDATION
    if (
        0 <= start_port <= 65535 and
        0 <= end_port <= 65535 and
        start_port <= end_port
    ):

        target = input("Enter the Target IP Address: ")

        print(f"\nScanning Target: {target}\n")

        open_ports = 0

        # PORT SCANNING LOOP
        for port in range(start_port, end_port + 1):

            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            # Wait max 0.5 sec for response
            s.settimeout(0.5)

            # Attempt TCP connection
            result = s.connect_ex((target, port))

            # PORT OPEN
            if result == 0:

                service_name = services.get(port, "Unknown Service")

                print(f"\nPort {port} is OPEN ({service_name})")

                # BANNER GRABBING
                try:

                    banner = s.recv(1024)

                    banner = banner.decode(errors="ignore")

                    print(f"Banner: {banner}")

                except Exception:

                    print("Banner: No Banner Available")

                open_ports += 1

            # Close socket and release resources
            s.close()

        print(f"\nTotal Open Ports Found: {open_ports}")

    else:

        print("Invalid Port Range Entered.")

except ValueError:

    print("Invalid Datatype Entered. Please enter only integers.")