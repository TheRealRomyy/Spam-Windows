# Import all we need
import random
import uuid
import time
import os

# Clear the cmd and set the color to green
os.system("cls")
os.system("color a")

# Verification
print("Do you want to activate the spammer ? \n[y/n]")
response = input().lower()

# Spam
if response == "y":
    while True:
        # Send uuid with random spaces
        toSay = ""
        spaces = random.randint(1,30)
        for i in range(spaces):
            toSay += " "
        toSay += str(uuid.uuid1())
        print(toSay)
# If response is "n" say Goodbye then leave
elif response == "n":
    print("Goodbye !")
    time.sleep(1)
    exit()
# If response is not "y" or not "n" exit
else:
    exit()
