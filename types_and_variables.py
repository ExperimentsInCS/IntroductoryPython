pet_name = input("What is your pet's name: ")
pet_age = int(input("What is your pet's age: "))
pet_cost = float(input('How much was the adoption fee? '))

#print(pet_name + "'s age is " + str(pet_age) + '.')
print(f"{pet_name}'s age is {pet_age}, and was adopted for ${pet_cost:0.2f}.")