#collestion = single "variable" used to store multiple values
# List =[] ordered and changeable. Duplicates OK
# Set = {} unordered and immutable, but Add/Remove OK. No duplicates
# Tuple= () ordered abd unchageable. Duplicates OK. FASTER

#fruits= ["apple", "orange", "banana", "coconut", "Pear", "blueberries"]
#print(dir(fruits)) #prints out the documentaion 
#print(help(fruits))
#print(len(fruits))
#print("apple" in fruits) #says if its true or not 


#fruits[1]="pineapple"# i can resign values using this 
#fruits.append("pineapple") #move variables
#fruits.remove("apple") #removes value
#fruits.insert(0, "pineapple") #sets variables at cetain values
#fruits.sort() #sorts 
#fruits.reverse()
#fruits.clear()


#print(fruits[::-1])

#for fruit in fruits:
 #   print(fruit)


cars =["bmw", "maserati", "audi", "mercedes", "ferrari"]
print(f"theses are a list of {cars}")
print(f"the first car is {cars[0]}")

#changing the value of the list
cars[0]= "toyota"
print(f"the first car is {cars[0]}")

print(f"the last car is {cars[-1]}")
cars[-1]= "lamborghini"
print(F"the last car is {cars[-1]}")

# adding a new value to the list
cars.append("bugatti")
print(cars)
cars.remove("maserati")
print(cars)

# looping throught the list
#otherwise called iterating throught the list (AKA interating)
for car in cars:
    #print(len(car))
    #print(car)
    carRequest= input("add a new car please: ")
    cars.append(carRequest)
    print(cars)
    print(len(cars))
    print(cars.upper())
    print(cars)
    if len(cars) > 10:
        break