#Exercise1
temperatures = [22, 24, 21, 55, 25, 20, 40]  

total = 0
for t in temperatures:
    total = total + t

average = total / 7  
print("Average temperature:", average)

print("Days above or below average:")
day = 1
for t in temperatures:
    if t > average:
        print("Day", day, "is above average.")
    elif t < average:
        print("Day", day, "is below average.")
    else:
        print("Day", day, "is average.")
    day = day + 1

print("\n")

#Exercies 2
name1 = "Santi"
name2 = "Diego"
name3 = "Ana"
name4 = "Cam"

grade1 = 85
grade2 = 10
grade3 = 40
grade4 = 95

print(name1, "got", grade1)
print(name2, "got", grade2)
print(name3, "got", grade3)
print(name4, "got", grade4)

if grade1 >= 50:
    print(name1, "passed")
else:
    print(name1, "failed")

if grade2 >= 50:
    print(name2, "passed")
else:
    print(name2, "failed")

if grade3 >= 50:
    print(name3, "passed")
else:
    print(name3, "failed")

if grade4 >= 50:
    print(name4, "passed")
else:
    print(name4, "failed")
total = grade1 + grade2 + grade3 + grade4
average = total / 4
print("Average grade is", average)

#Exercies 3
item1 = "Milk"
item2 = "Bread"
item3 = "Eggs"

answer1 = input("Did you buy " + item1 + "? (yes or no): ")
if answer1 == "yes":
    print(item1, "is bought.")
else:
    print(item1, "has not been purchased yet.")

answer2 = input("Did you buy " + item2 + "? (yes or no): ")
if answer2 == "yes":
    print(item2, "is bought.")
else:
    print(item2, "has not been purchased yet.")

answer3 = input("Did you buy " + item3 + "? (yes or no): ")
if answer3 == "yes":
    print(item3, "is bought.")
else:
    print(item3, "has not been purchased yet.")

    #exercies 4
# Exercise 4: Numbers - Very Simple

print("Exercise 4: Numbers")

# Just a few numbers
num1 = 5
num2 = 3
num3 = 8

if num1 <= num2 and num1 <= num3:
    smallest = num1
    if num2 <= num3:
        middle = num2
        biggest = num3
    else:
        middle = num3
        biggest = num2
elif num2 <= num1 and num2 <= num3:
    smallest = num2
    if num1 <= num3:
        middle = num1
        biggest = num3
    else:
        middle = num3
        biggest = num1
else:
    smallest = num3
    if num1 <= num2:
        middle = num1
        biggest = num2
    else:
        middle = num2
        biggest = num1
print("Numbers in order:", smallest, middle, biggest)

#Exercies 6
user1 = "Majo"
user2 = "Sofia"
user3 = "Andrea"

new_user = input("Enter a new username: ")

if new_user == user1 or new_user == user2 or new_user == user3:
    print("That name is already taken. Try a different one.")
else:
    print("Username is available! You can use it.")
