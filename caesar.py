print('| Caesar Cipher |\n')
print('What you be doing?')
print('1. Encrypt with Caesar Cipher')
print('2. Decrypt with Caesar Cipher')
mode=input()


# Store the encrypted /decrypted form of the message :
translated = ''

#The encryption/decryption key:
keyMessage = 'Please enter the key to :\n'
key = int(input(keyMessage))

#The encryption/decryption message:
messageInput = 'Enter message to be fondled with \n'
message = input(messageInput)

# Every possible that can me encrypted :
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

#find symbol
for symbol in message:
    if symbol in SYMBOLS:
        symIndex = SYMBOLS.find(symbol)

#functionality
        if mode == '1':
            translatedIndex = symIndex + key 
        elif mode == '2':
            translatedIndex = symIndex - key 
#wraparound? 

        if translatedIndex >= len(SYMBOLS):
            translatedIndex = translatedIndex + len(SYMBOLS)
        elif translatedIndex < 0 : 
            translatedIndex = translatedIndex - len(SYMBOLS)

        translated = translated + SYMBOLS[translatedIndex]
    else: 
        translated = translated + symbol

print(translated)
