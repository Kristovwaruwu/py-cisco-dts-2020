# step 1
beatles = []
print("Step 1:", beatles, "\n")

# step 2
beatles.append("John Lennon")
beatles.append("Paul McCarney")
beatles.append("George Harrison")
print("Step 2:", beatles, "\n")

# step 3
for member in range(2):
    newMember = input("New Member : ")
    beatles.append(newMember)

print("\nStep 3:", beatles, "\n")

# step 4
del beatles[-2:]
print("Step 4:", beatles, "\n")

# step 5
beatles.insert(0, "Ringgo Star")
print("Step 5:", beatles)


# testing list legth
print("The Fab", len(beatles))