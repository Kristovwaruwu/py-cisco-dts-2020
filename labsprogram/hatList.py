hatList = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

# Step 1: write a line of code that prompts the user
newList = int(input("Enter any number : "))

# to replace the middle number with an integer number entered by the user.
hatList[3] = newList
print("Add new List", hatList)

# Step 2: write a line of code here that removes the last element from the list.
del hatList[-1]
print("After deleting : ", hatList)

# Step 3: write a line of code here that prints the length of the existing list.
print("Length of hatList : ",len(hatList))


print("The Current List :", hatList)