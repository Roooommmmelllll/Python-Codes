def getPrice(itemName, x):
   for i in range(0,len(x)):
      if x[i][0] == itemName:
         return x[i][2]

def getQuantity(itemName, x):
   for i in range(0,len(x)):
      if x[i][0] == itemName:
         return x[i][1]

def updateQuantity(itemName, x, newQuantity):
   for i in range(0,len(x)):
      if x[i][0] == itemName:
         print("Current quantity is", x[i][1])
         x[i][1] = newQuantity
         print(x[i][1])

def printSummary(x):
   for i in range(0, len(x)):
      itemName = x[i][0]
      quantity = x[i][1]
      price = x[i][2]
      print(itemName, "has", quantity, "items, at a price of", price)

def createInventory():
   x = []
   stop = 1
   while stop == 1:
      itemName = input("Input an item name")
      if itemName == "stop":
         break
      quantity = int(input("Enter a quantity"))
      price = float(input("Enter a priced"))
      x.append([itemName, quantity, price])

   return x
         
def main():
   x = createInventory()
   itemName = input ("What item's price are you looking for?: ")
   price = getPrice(itemName, x)
   print(price)
   itemName = input ("What item's quantity are you looking for?: ")
   quantity = getQuantity(itemName, x)
   print(quantity)
   itemName = input ("What item's quantity do you wish to change?: ")
   newQuantity = int(input("What new quantity do you wish to input?: "))
   updateQuantity(itemName, x, newQuantity)
   printSummary(x)
      
main()
