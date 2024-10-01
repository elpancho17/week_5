#collestion = single "variable" used to store multiple values
# List =[] ordered and changeable. Duplicates OK
# Set = {} unordered and immutable, but Add/Remove OK. No duplicates
# Tuple= () ordered abd unchageable. Duplicates OK. FASTER

fruits= ["apple", "orange", "banana", "coconut", "Pear", "blueberries"]
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

fruits= {"apple", "orange", "banana", "coconut", "Pear", "blueberries"}
#print(dir(fruits)) #prints out the documentaion 
#print(help(fruits))
#print(len(fruits))
#print("apple" in fruits) #says if its true or not 

# fruits.remove("apple") #removes something
# fruits.add("pickles")
# fruits.add("tomatoes") #add something
# fruits.pop() #pops of the first one but it random
# print(fruits)


fruits= ("apple", "orange", "banana", "coconut", "Pear", "blueberries")
#print(dir(fruits)) #prints out the documentaion 
#print(help(fruits))
#print(len(fruits))
#print("apple" in fruits) #says if its true or not 

# print(fruits.index("apple"))
# print(fruits.count("coconut"))

# print(fruits)
# for fruit in fruits:
#     print(fruit)



#print(fruits[::-1])

#for fruit in fruits:
 #   print(fruit)


#cars =["bmw", "maserati", "audi", "mercedes", "ferrari"]
#print(f"theses are a list of {cars}")
#print(f"the first car is {cars[0]}")

#changing the value of the list
#cars[0]= "toyota"
#print(f"the first car is {cars[0]}")

#print(f"the last car is {cars[-1]}")
#cars[-1]= "lamborghini"
#print(F"the last car is {cars[-1]}")

# adding a new value to the list
#cars.append("bugatti")
#print(cars)
#cars.remove("maserati")
#print(cars)

# looping throught the list
#otherwise called iterating throught the list (AKA interating)
#for car in cars:
    #print(len(car))
    #print(car)
    #carRequest= input("add a new car please: ")
    #cars.append(carRequest)
    #print(cars)
    #print(len(cars))
    #print(cars.upper())
    #print(cars)
    #if len(cars) > 10:
        #break



#challenge
# create a list of friends
# make sure the intital list is none
# friends=[]
# #add a new friend to the list, add at least 5 friends.
# friendAdd= input("add a new friend please: ")
# friends.append(friendAdd)
# print(len(friends))
# print(friends)
# friendAdd= input("add a new friend please: ")
# friends.append(friendAdd)
# print(len(friends))
# print(friends)
# friendAdd= input("add a new friend please: ")
# friends.append(friendAdd)
# print(len(friends))
# print(friends)
# friendAdd= input("add a new friend please: ")
# friends.append(friendAdd)
# print(len(friends))
# print(friends)
# friendAdd= input("add a new friend please: ")
# friends.append(friendAdd)
# print(len(friends))
# print(friends)
# friends.remove("cory")
# friends.insert(2,"maxwell")
# print(friends)
# print("Cloud" in friends)


#dictionary= a collection of {key:value} pairs ordered and changeable. No duplicates
capitals= {"USA": "Washington D.C",
           "Inda": "New Delhi",
           "China": "Beijing",
           "Russia": "Moscow"}

# print(dir(capitals))
# print(help(capitals))
# print(capitals.get("USA"))
#print(capitals.get("Japan"))

# if capitals.get("Japan"):
#     print("that capital exist")
# else:
#     print("that capital doesn't exist")

# capitals.update({"Germany": "Berlin"})
# capitals.pop("China")
# capitals.clear()

# keys = capitals.keys()
# for key in capitals.keys():
#     print(key)

# values = capitals.values()
# for value in capitals.values():
#     print(value)

# items = capitals.items()
# for key, value in capitals.items():
#     print(f"{key}: {value}")

# print(capitals)

#Courtasy of Maxwell