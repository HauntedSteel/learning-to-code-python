randlist = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u",'v','w','x','y','z', '1','2','3','4','5','6','7','8','9','0','!','@','#','$','%','^','&','*','(',")",'`',"~",'|',"<",">","/","?"]
import random

#Gets length
while True:
  try:
    z = int(input("What is the length of your desired password? (minimum 8): "))
  except:
    print("Please enter in an integer.")
  if z < 8:
    print("*MINIMUM 8")
    continue
  break

#Keywords
keywords = []
print("What keywords do you want to be inserted in your password?") 
while True:
  x = input("(Enter Q to stop entries): ")
  if x == "Q":
    break
  else:
    keywords.append(x)

#Ensures not too many keywords
deduct = 0
for counter in keywords:
  deduct += len(counter)
if deduct > z:
  print("You have entered too many keywords!")

#Random character generation, x times, where x is length of password - combined length of keywords.
password = []
z -= deduct
for counter in range(z):
  generatedLetter = randlist[random.randint(0,len(randlist)-1)]
  password.append(generatedLetter)

#Inserting keywords 
for counter in keywords:
  bruh = random.randint(0,len(password))
  password.insert(bruh,counter)
password = "".join(password)
print("Your password is: ", password)
