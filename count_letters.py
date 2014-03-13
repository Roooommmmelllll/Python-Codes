def countLetters():
   sentence = input("Please write a sentence: ")
   letter = input("What letter do you want to count?: ")
   length = len(sentence)
   count = 0
   for i in range(0,length):
      if letter == sentence[i]:
         count+=1
   if count == 0:
      print(sentence)
      print("No,", letter, "doesn't show up in that sentence.")
   else:
      print(sentence)
      print("Yes,", letter, "was there were", count, "times.")

def countLettersWhile():
   sentence = input("Please write a sentence: ")
   letter = input("What letter do you want to count?: ")
   length = len(sentence)
   count = 0
   start = 0
   while start < length:
      if letter == sentence[start]:
         count+=1
         start += 1
      else:
         start += 1
   if count == 0:
      print(sentence)
      print("No,", letter, "doesn't show up in that sentence.")
   else:
      print(sentence)
      print("Yes,", letter, "was there were", count, "times.")
