blocks = int(input("Enter the number of blocks: "))

# Write your code here.
x = 0
penambahan = 1
while (x < blocks):
    x += penambahan
    if (x > blocks):
        break
    height = penambahan
    penambahan += 1	

print("The height of the pyramid:", height)