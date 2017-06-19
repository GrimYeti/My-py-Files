x = "This is a sample string"
#x = "0123456789"
 
print("x=", x)
 
# Accessing a single character
print("x[0]=", x[0])
print("x[1]=", x[1])
 
# Accessing from the right side
print("x[-1]=", x[-1])
 
# Access 0-5
print("x[:6]=", x[:6])
# Access 6
print("x[6:]=", x[6:])
# Access 6-8
print("x[6:9]=", x[6:9])

a = "Hi"
b = "There"
c = "!"
print(a + b)
print(a + b + c)
print(3 * a)
print(a * 3)
print((a * 2) + (b * 2))

a = "Hi There"
print(len(a))
 
b = [3, 4, 5, 6, 76, 4, 3, 3]
print(len(b))

months = "JanFebMarAprMayJunJulAugSepOctNovDec"
 
n = int(input("Enter a month number: "))

my_starting_index = (n-1) * 3


my_months_string = []
for i in range (3):
    my_months_string += months[my_starting_index+i]

print(my_months_string)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


plain_text = "This is a test. ABC abc"
 
encrypted_text = ""
for c in plain_text:
    x = ord(c)
    x = x + 1
    c2 = chr(x)
    encrypted_text = encrypted_text + c2
print(encrypted_text)


encrypted_text = "Uijt!jt!b!uftu/!BCD!bcd"
 
plain_text = ""
for c in encrypted_text:
    x = ord(c)
    x = x - 1
    c2 = chr(x)
    plain_text = plain_text + c2
print(plain_text)

