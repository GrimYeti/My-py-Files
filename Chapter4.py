for i in range(5):
    print("I will not chew gum in class.")
    
print("~~~~~~~~~~~~~~~~~~")

for i in range(10):
    print(i)
    
print("~~~~~~~~~~~~~~~~~~~~~~~~")

for i in range(10):
    print(i + 1)
    
print("~~~~~~~~~~~~~~~~~~~~~~~")

for i in range(2,12,2):
    print(i)
    
print("~~~~~~~~~~~~~~~~~~~~~~~~")

for i in range(10, 0, -1):
    print(i)
    
print("~~~~~~~~~~~~~~~~~~~~~~~~~")

for i in [2,6,4,2,4,6,7,4]:
    print(i)
    
print("~~~~~~~~~~~~~~~~~~")

for i in range(3):
    print("a")
    for j in range(3):
        print("b")
 
print("~~~~~~~~~~~~~~~~~~~~~~~~")

total = 0
for i in range(5):
    new_number = int(input("Enter a number: " ))
    total += new_number
print("The total is: ", total)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

a = 0
for i in range(10):
    a = a + 1
print(a)
 
# What is the value of a?
a = 0
for i in range(10):
    a = a + 1
for j in range(10):
    a = a + 1
print(a)
 
# What is the value of a?
a = 0
for i in range(10):
    a = a + 1
    for j in range(10):
        a = a + 1
print(a)