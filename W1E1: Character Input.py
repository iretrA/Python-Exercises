# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old

# asks for your age
name = input("Enter your name: ")
age = int(input("Enter your age: "))
current_year = int(input("Enter the current year: "))

years_left = 100 - age
new_year = years_left + current_year

# prints years you have left until 100
print(f"You have {str(years_left)} years left until you turn 100")
print(f"You will turn 100 on {str(new_year)}")
