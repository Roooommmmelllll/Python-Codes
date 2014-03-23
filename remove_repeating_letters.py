def main():
   print("The program will remove all repeating letters in a given word.")
   word = input("Please enter a word to check for letters.\n")
   wordList = []
   wordList.append(word[0])
   for i in range(len(word)):
      for j in range(len(wordList)):
         if(word[i] == wordList[j]):
            break
         elif(j == (len(wordList)-1) and word[i] != wordList[j]):
            wordList.append(word[i])
   newWord = "".join(wordList)
   print(newWord)
   
main()   
