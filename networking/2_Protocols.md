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
        - *HTTP*
        - *HTTPS*
    - Transport Layer (4)
        - Port 80
        - Port 443
    - Ports easily identifies traffic at Layer 4, so that systems know what Layer 7 protocol to use

### File Transfer - FTP, sFTP, TFTP

- Transfer files from client to server or vice versa
- *FTP* - File Transfer Protocol
    - Ports: 20 and 21
        - One port is used for authentication while the other is used for the transfer of information
    - > ftp://xx.xxx.xx.xxx
    - Typically want to use FTP clients like PuTTY, FileZilla, etc. in order to transfer files to and from
- *sFTP* - Secure File Transfer Protocol
    - Encrypted traffic
    - Port: 22
        - Also the port for SSH, FTP inside an SSH session
- *TFTP* - Trivial File Transfer Protocol
    - Meant for tiny files between 2 devices, or simple setups to transfer quickly without authentication or firewall issues
    - Port: 69
- *SMB* - Server Message Block
    - Network file share
    - Port: 445
    - Mapped drive
    - > \\\server\someFolder

### Email

- 3 protocols: POP3 (client), IMAP (client), SMTP (mail server)
    - *POP3* - Post Office Protocol
        - Transfer email from server to client
        - Ports: 110/995 (unencrypted/encrypted)
    - *IMAP* - Internet Message Access Protocol
        - Transfer email from server to client
        - Ports: 143/993 (unencrypted/encrypted)
    - *SMTP* - Simple Mail Transfer Protocol
        - Sends email from client to server to send out to the recipient
        - Ports: 25/465 (unencrypted/encrypted)
    - All of these protocols operate in encrypted or unencrypted modes!