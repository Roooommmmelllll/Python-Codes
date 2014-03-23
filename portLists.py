
def main():
   ports = [0,0,0,0]
   
   for i in range(4):
      ports[i] += int(input("Please enter a port number: "))
   for i in range(64,129):
      for j in range(4):
         print("192.168.94."+str(i)+"."+str(ports[j]))

main()
