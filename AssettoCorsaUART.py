from socket import *
from struct import *

serverName='127.0.0.1'
serverPort = 9996
clientSocket = socket(AF_INET,SOCK_DGRAM)
message=pack('iii',1,1,0)

clientSocket.sendto(message, (serverName, serverPort))

messageback, ipAddress=clientSocket.recvfrom(1024)
print ('received')
pktformat='408c'
n = calcsize(pktformat)
print (n)
#n = len(messageback)
#print n

backString = unpack(pktformat, messageback)
print (backString)
#print "fffffff"
message=pack('iii',1,1,1)
clientSocket.sendto(message, (serverName, serverPort))

i=0
for i in range(3):
#while True:
    pktformat='4chfff??????fffhhhhfffffhf4f4f4f4f4f4f4f4f4f4f4f4f4f4fff5f'

    messageback, ipAddress =clientSocket.recvfrom(16384)
    n = calcsize(pktformat)
    print (n)
    n = len(messageback)
    print (n)
    backString = unpack(pktformat, messageback)
    print (backString)
    # i+=1

clientSocket.close()