print("~~~~~~~~~~~~~~~~~~~~")
print("Ceaser Cipher")
print("~~~~~~~~~~~~~~~~~~~~")


biggest_key = 26


def getMode():
        while True:
                print("Encrypt a message (A) \nDecrypt a message (B) \nQuit Cipher (C)\n")
                mode = input().lower()
                if mode in 'a b'.split():
                        return mode
                else:
                        print("Encrypt a message (A) \nDecrypt a message (B) \nQuit Cipher (C)\n")

                        
                        
def getMessage():
        print("Type a message to be traslated")
        return input()
    

def getKey():
        key = 0
        while True:
                print("Enter encryption key (1-26)")
                key = int(input())
                if (key >= 1 and key <= biggest_key):
                        return key
                
def getTranslatedMessage(mode, message, key):
        if mode[0] == 'b':
                key = -key
                translated = ''
                
                for symbol in message:
                        if symbol.isalpha():
                                num = ord(symbol)
                                num += key
                                
                                if symbol.isupper():
                                        if num > ord('Z'):
                                                num -= 26
                                        elif num < ord('A'):
                                                num += 26
                                
                                elif symbol.islower():
                                        if num > ord('z'):
                                                num -= 26
                                        elif num < ord('a'):
                                                num += 26
                                        
                        translated += chr(num)
        else:
                translated = ''
                                
                for symbol in message:
                        if symbol.isalpha():
                                num = ord(symbol)
                                num += key
                                                
                                if symbol.isupper():
                                        if num > ord('Z'):
                                                num += 26
                                        elif num < ord('A'):
                                                num -= 26
                                                
                                elif symbol.islower():
                                        if num > ord('z'):
                                                num += 26
                                        elif num < ord('a'):
                                                num -= 26
                                                        
                                translated += chr(num)                
        
                        #translated += symbol
                        
        return translated                



#if play_game.lower() == "b":
    #import sys
    #sys.exit("Game Over")
#if play_game.lower() == "c":
    #import sys
    #sys.exit("Game Over")    
            
mode = getMode()
message = getMessage()
key = getKey()
print("~~~~~~~~~~~~~~~~~~~~")

print('Your translated text is:')
print(getTranslatedMessage(mode, message, key))