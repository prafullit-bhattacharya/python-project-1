import random#use to import random numbers
import string# use to import sets of characters, such as lowercase and uppercase letters, digits, and punctuation.
allcharacters=string.ascii_letters+string.punctuation+string.digits #American standard code for information interchange: a computer code for representing alphanumeric characters eg:number from 0 to 9 and specials symbols ,#,$,*,@
length=int(input("Enter the length of the password"))
password = ''.join(random.choices(allcharacters, k=length))
print(f"your password is:{password}")
