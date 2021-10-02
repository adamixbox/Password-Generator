import random

Letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a" ]
Words = ["Cat", "Dog", "Mouse", "Pet", "House", "Home", "Road", "Shop", "Store", "Supermarket", "Lamppost", "Streetlight", "Hello", "How", "Warrior", "Friend", "Husband", "Wedding", "Wife", "Generator", "Computer", "Laptop", "Fan", "Blade", "Knight", "Mother", "Father", "Awesome", "Amazing", "Mood", "Traffic", "Lights", "Streetlamps", "Motor", "Motorvehicle", "Transport", "Vehicle", "Car", "Like", "Train", "a"]
SCharacters = ["!", "|", "*", "_", "a"]
LettersC = []

i = 0

def secure():
    for i in range(15):
        f = random.randint(1,26)
        if (f % 2) == 0:
            LettersC.append(Letters[random.randint(1,26)].upper())
        else:
            LettersC.append(Letters[random.randint(1,26)].lower())
    for i in range(3):
        LettersC.append(random.randint(1,9))
    for i in range(2):
        LettersC.append(SCharacters[random.randint(1, 3)])

def noteable():
    for i in range(3):
        LettersC.append(Words[random.randint(1, 39)])
        LettersC.append(random.randint(1,9))

print("Hello, there!")
print("Welcome to this password generator; before we get started, would you rather a:")
print("Secure Password "+"or "+"Noteable Password?")
input = input("")

if input.lower() == "secure" or input.lower() == "secure password":
    secure()
    print("".join(str(e) for e in LettersC))
elif input.lower() == "noteable" or input.lower() == "noteable password":
    noteable()
    print("".join(str(e) for e in LettersC))
else:
    print("You have not entered a valid answer, please try again.")
