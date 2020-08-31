import nmap
import sys 

if len(sys.argv) < 4:
    print("Usage: python3 ",__file__," [IP] [PORT1 [PORT2]]")
    sys.exit()

ip = sys.argv[1]
port1 = int(sys.argv[2])
port2 = int(sys.argv[3])

scanner = nmap.PortScanner()
for port in range(port1,port2):
    result = scanner.scan(ip,str(port))
    result = result['scan'][ip]['tcp'][port]['state']   
    print("Port " + str(port) + ": " + result )
