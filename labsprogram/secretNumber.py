secretNumber = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

guessNumber = int(input("Make a guess : "))

while guessNumber != secretNumber:
    print ("Ha ha! You're stuck in my loop!")
    guessNumber = int(input("Make a guess again : "))

print("Well done, muggle! You are free now.")