import keyword
keywordslist = keyword.kwlist
a = input("Please enter any key word: ")
if a in keywordslist:
        print( ValueError("This is a keyword"))
else:
        print("No keyword is wrong ")