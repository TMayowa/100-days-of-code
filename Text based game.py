print('''
                   .---.
                  (_---_)
                 (_/6 6\_)
                  (  v  )
                   `\ /'
                .-'': ;``-.
               /   \,Y./   \
              /     (:)___  \
             :   .-'XXX`-.`\_;
              `.__.-XXX-.__.'\_
               /  / XXX \  \   `\_
              /      XXX    \     `\
             /        XXX    \     _`\___
    jgs     /                 \  (`--"""-')
           /                   \ (=-=-=-=-)
           `--...___   ___...--' (________)''')
print("Welcome to Grandma's house.")
print("Your mission is to eat and relax.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

print("Welcome to Grandma's house \n")
print("reply with a yes or no \n")
choice1 = input("Do you want to eat some cookies? \n").lower()
if choice1 == "no":
  print("It's time to go home")
else:
  choice2 = input("Do you want some ice cream with the cookies? \n").lower()
  if choice2 == "no":
    print("It's time to go home")
  else:
    choice3 = input("Do you want to sleep? \n").lower()
    if choice3 == "no":
      print("It's time to go home")
    else:
      print("You can sleep in the guest room \n Thank you for spending time with Grandma")
        

