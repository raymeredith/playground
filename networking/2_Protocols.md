# Protocols and Port Numbers

## Application Layer Protocols (Layer 7)

### Transferring Data - HTTP/HTTPS

- HTTP/HTTPS used to transfer website data
- Client/Server model
    - Nearly all application layer protocols use client/server
    - Transferring a hyptertext (HTML) file
    - Client: Uses a web browser to interpret HTML
    - Server: Uses website server software like Apache, NGINX, etc.

- Every Layer 7 protocol has an associated layer 4 Transport Layer protocol
    - Application Layer (7)
        - **HTTP**
        - **HTTPS**
    - Transport Layer (4)
        - Port: 80
        - Port: 443
    - Ports easily identifies traffic at Layer 4, so that systems know what Layer 7 protocol to use

### File Transfer - FTP, sFTP, TFTP

- Transfer files from client to server or vice versa
- **FTP** - File Transfer Protocol
    - Ports: 20 and 21
        - One port is used for authentication while the other is used for the transfer of information
    - > ftp://xx.xxx.xx.xxx
    - Typically want to use FTP clients like PuTTY, FileZilla, etc. in order to transfer files to and from
- **sFTP** - Secure File Transfer Protocol
    - Encrypted traffic
    - Port: 22
        - Also the port for SSH, FTP inside an SSH session
- **TFTP** - Trivial File Transfer Protocol
    - Meant for tiny files between 2 devices, or simple setups to transfer quickly without authentication or firewall issues
    - Port: 69
- **SMB** - Server Message Block
    - Network file share
    - Port: 445
    - Mapped drive
    - > \\\server\someFolder

### Email

- 3 protocols: POP3 (client), IMAP (client), SMTP (mail server)
    - **POP3** - Post Office Protocol
        - Transfer email from server to client
        - Ports: 110/995 (unencrypted/encrypted)
    - **IMAP** - Internet Message Access Protocol
        - Transfer email from server to client
        - Ports: 143/993 (unencrypted/encrypted)
    - **SMTP** - Simple Mail Transfer Protocol
        - Sends email from client to server to send out to the recipient
        - Ports: 25/465 (unencrypted/encrypted)
    - All of these protocols operate in encrypted or unencrypted modes!

### Authentication Protocols

- **LDAP** - Lightweight Direcotry Access Protocol (also LDAPs)
    - Ports: 389/636
    - Should be using LDAPs in all modern implementations

### Network Services

- **DHCP** - Dynamic Host Configuration Protocol
    - DHCP running on home network, typically within the wireless AP
    - Automatically hands out IP addresses to any device that's connected
    - Workstation sends message to DHCP server, server sends network config information back
- **DNS** - Domain Name System
    - Allows us to use simple names to communicate with devices on the internet
    - Client sends message to DNS server asking what the IP of google.com is, DNS server responds with IP address, client can then reach out to google's IP directly
    - > nslookup google.com
    - or
    - > nslookup  
      > \> server 1.1.1.1  
      > \> google.com
- **NTP** - Network Time Protocol
    - Automatically configure all the times on clients to be exactly the same
    - NTP will be built into the OS
    - NTP servers are often run by the government
    - Coordinated Universal Time (UTC)
        - Allows us to accomodate time zones, line is set with Greenwich, England (prime meridian, GMT)
        - Daylight savings time adds complications

### Network Management

- **Telnet**
    - Cleartext
    - Port: 23
- **Secure Shell** (SSH)
    - Port: 22
- These are used in network administration, where the network administrator's workstation will be the client using these protocols to communicate with various network devices, like servers, routers, firewalls, etc.
- **SNMP** - Simple Network Management Protocol
    - Collects information about other clients on the network, "walk the tree"
        - Port status
        - Interface up/down
        - Temperatures, usage, etc.
    - Network admin can see metrics of the performance of devices on the network
    - SNMP Trap from a client device, add to database, send an alert to a network admin
- **RDP** - Remote Desktop Protocol
    - Get access to the desktop of a server, using the Remote Desktop application, shares the screen onto workstation
    - Port: 3389

### Audio/Visual Protocols

- **H.323**
    - Ports: 1720/1721
    - A/V communication, typically used for video conferencing
- **SIP** - Session Initiation Protocol
    - VOIP
    - Ports: 5060/5061
    - Connection between a phone and a server
