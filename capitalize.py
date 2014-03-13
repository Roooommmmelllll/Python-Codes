def capitalize():
   text = '''eighty-five-year-old Rear Admiral Grace Murray Hopper who dedicated
her life to the Navy passed away on 1 January 1992. as a pioneer
Computer Programmer and co-inventor of COBOL, she was known as
the Grand Lady of Software, Amazing Grace and Grandma COBOL. she'll be remembered for her now
famous sayings, one of which is: It's easier to ask forgiveness than it is to get permission. it's
only fitting that Grace Brewster Murray was born between two such
memorable events as the Wright Brothers' first successful power-driven
flight in 1903 and Henry Ford's introduction of the Model T in 1908. Taught by her
father at an early age to go after what she wanted, Grace's
life consisted of one success after another, including the significant
contributions she made to the computer age and the Navy.'''
   textlist = text.split('. ')
   textlist2 = []
   
   for i in range(0, len(textlist)):
     textlist2.append((textlist[i])[0].upper())
     textlist2.append(textlist[i][1::])
     
   textlist = []
   counter = 0
   
   while counter < len(textlist2):
      textlist.append(textlist2[counter]+textlist2[counter+1])
      counter += 2
      
   print(". ".join(textlist))
   
capitalize()
