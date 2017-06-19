print("Quiz Time By Connor B")

print("~~~~~~~~~~~~~~~~~~~~")

print("What is the newest version of Android?")
print("1. KitKat")
print("2. Nougat")
print("3. Marshmellow")
print("4. Lolipop")
android_anwser = input("Anwser in #: ")
if android_anwser == "2":
    print("Correct!")
else:
    print("Incorrect.")

right_anwser = 0
if android_anwser == "2":
    right_anwser += 1

print("~~~~~~~~~~~~~~~~~~~~")

print("If Bill Gates has 7 billion dollars and spends ten thousand dollars a day, how long in year until he runs out of money? Round off the decimals.")
no_money = input("How many years? ")
if no_money == "1918":
    print("Correct!")
else:
    print("Incorrect.")
    
if no_money == "1918":
    right_anwser += 1
    
print("~~~~~~~~~~~~~~~~~~~~")

print("Who is the Prime Minister of Canada?")
print("1. Donald Trump")
print("2. Stephen Harper")
print("3. Justin Trudeau")
print("4. Barack Obama")
canada_pm = input("Canadian's Prime Minister is: ")
if canada_pm == "3":
    print("Correct!")
else:
    print("Incorrect")

if canada_pm == "3":
    right_anwser += 1

print("~~~~~~~~~~~~~~~~~~~~")

print("What is 3*(5-3)?")
math1_awnser = input("=? ")
if math1_awnser == "6":
    print("Correct!")
else:
    print("Incorrect.")
    
if math1_awnser == "6":
    right_anwser += 1

print("~~~~~~~~~~~~~~~~~~~~")

print("What is 3*5-3?")
math2_awnser = input("=? ")
if math2_awnser == "12":
    print("Correct!")
else:
    print("Incorrect.")

if math2_awnser == "12":
    right_anwser += 1
    
print("~~~~~~~~~~~~~~~~~~~~")

print("Who created \"Valve\"?")
valve_awnser = input("The creator of Valve is: ")
if valve_awnser.lower() == "gabe newell":
    print("Correct!")
else:
    print("Incorrect.")
    
if valve_awnser.lower() == "gabe newell":
    right_anwser += 1
    
print("~~~~~~~~~~~~~~~~~~~~")

total = right_anwser / 6 * 100

print("Congratulations, you got", right_anwser, "answers correct.")
print("That is a score of", total, "percent.")

