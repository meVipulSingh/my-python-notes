letter = '''DEAR <|Name>|,
Greetings from abc coding house. I am happy to tell you about your selection 
you are selected!
Have a great day ahead!
Mark
Date: <|Date>|
'''
name = input("Enter your Name\n")
date = input("Enter Date\n")
letter = letter.replace("<|Name>|", name)
letter = letter.replace("<|Date>|",date)
print(letter)