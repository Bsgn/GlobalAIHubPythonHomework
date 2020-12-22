# first_name = input("First Name : ")
# last_name = input("Last Name: ")
# age = int(input("Age : "))
# date_of_birth = int(input("Date of Birth (Year) : "))

user = list()

user.append(input("First Name : "))
user.append(input("Last Name : "))
user.append(int(input("Age : ")))
user.append(int(input("Date of Birth (Year) : ")))

for i in user:
    print(i)

if 0 <= user[2] < 18:
    print("You can't go out because it's too dangerous")
elif user[2] >= 18:
    print("You can go out to the street")
else:
    print("That's impossible. You have a negatif age.")
    