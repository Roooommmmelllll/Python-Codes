#calculator program
#user will input a string with an equation, and the
#program will compute the answer, and print it out

def findOperator(equation):
   for i in range (0,len(equation)):
      if equation[i] == "+":
         operator = "+"
      elif equation[i] == "-":
         operator = "-"
      elif equation[i] == "*":
         operator = "*"
      elif equation[i] == "/":
         operator = "/"
   return operator

def findOperatorLoc(equation):
   for i in range (0,len(equation)):
      if equation[i] == "+":
         operator = i
      elif equation[i] == "-":
         operator = i
      elif equation[i] == "*":
         operator = i
      elif equation[i] == "/":
         operator = i
   return operator

def doMath(operator, num1, num2):
   operator = operator
   num1 = float(num1)
   num2 = float(num2)
   if operator == "+":
      answer = num1+num2
   elif operator == "-":
      answer = num1-num2
   elif operator == "*":
      answer = num1*num2
   elif operator == "/":
      if num2 == 0:
         print("error! Dividing by zero destroys the Matrix.")
         return "undefined"
      else:
         answer = num1/num2
   return answer

def checkAnswer(answer):
   if answer%1 != 0:
      answer = float(answer)
      answer = "%.2f"%answer
   return answer

def printMe(equation, answer):
   print(equation, "=", answer)

def main():
   equation = input("Please input an equation (Example: 123/123): ")
   operator = findOperator(equation)
   operatorLoc = findOperatorLoc(equation)
   num1 = equation[0:operatorLoc]
   num2 = equation[operatorLoc+1:len(equation)]
   answer = doMath(operator, num1, num2)
   if answer == "undefined":
      print("undefined")
   else:
      answer = checkAnswer(answer)
      printMe(equation, answer)
   
main()
