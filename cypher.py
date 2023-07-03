#A code to take a message and encode by 15.

#a function taking a string and key
def encode(string , key):
    cypher = ''
    for char in string:
        if char == ' ':
            cypher=cypher+char
        elif char.isupper():
            cypher=cypher+chr((ord(char)+ key-65)%26+65) #taking the char turning into a number 65 for uppercase
        else:
            cypher=cypher+chr((ord(char)+ key-97)%26+97) #97 for lowercase 
    return cypher            

# input for the text key is set to 15 and print statements for the encode message and actually message
text = input("enter the text")
key=int(15)
print("the message is :",text)
print("encoded message is :",encode(text,key))   