def main():
   begSalary = int(input("Please input the starting salary for a teacher: "))
   years = int(input("Enter the years that a teacher would work for to see their salaries per year: "))
   salaries = []
   for i in range(years):
      if i == 0:
         salaries.append(begSalary)
      else:
         salaries.append(salaries[i-1]*1.02)
   print("YEARS WORKED\tSALARY")
   for i in range(years):
      print("   ",(i+1),"\t\t","%.2f"%salaries[i])
main()
