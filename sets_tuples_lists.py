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


#print(fruits[::-1])

for fruit in fruits:
    print(fruit)