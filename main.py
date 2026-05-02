import random
import string

while True:
    pas_length = int(input("Enter the length of the password required: "))
    
    if pas_length < 11:
        print("Length of the password must be greater than 11 characters!!")
        continue
    else:
        break

length = 0
options = (string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation)
while length < pas_length :
    
    password = random.choice(options)
    print(password,end="")
    length += 1
  
       

        
