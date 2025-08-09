print("Hello, may I ask, what is your name?")

name = input(f"My name is: ")

print(f"It was nice meeting you {name}")

print("Now i may ask, how are you feeling today? (respond with either good/bad):")

mood = input("I feel ").lower()

if mood == "good":
    print("Im glad to hear that!")

elif mood == "bad":
    print("Im soory to hear that, i hope your day gets better")

else:
    print("I understand, its hard to put feelings into words sometimes")

print(f"It was nice meeting you {name}! Goodbye")