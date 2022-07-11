# Declaring the lists
menu = ["salad", "mashed potatoes", "juice"]
ounces = [8, 16, 24, 32]
food_quality = [1, 3, 5, 8, 10]
print("Welcome to our restaurant.")
print("Could you give us the menu?")
print("Yes, of course")
print("Are you ready to order?")
print("Yes, we are")
order = input()
print("Okay, what quality of food do you want?")
quality = int(input())
print("How much ounces of the dish will you have?")
number = int(input())
if order in menu:
    # Checking if there is the required dish 
    if quality in food_quality:
    	# Checking if there is the required quality  
        if number in ounces:
        	# Checking if there is the required mass of the dish
            print("Great! I'll be right back")
# In case the statements are not true
else:
    print("I'm afraid we cannot serve you")