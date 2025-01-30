#   a212_cipher.py
#   Rotation Cipher

MAX_KEY_SIZE = 26 

def getMode():
  while True:
   return 'd'


def getMessage():
  print('Enter your message:')
  return input()

def getKey():
  while True:
    for i in range(0,27):
      key = i
      if (key >= 1 and key <= MAX_KEY_SIZE):
        return key

def getTranslatedMessage(mode, message, key):
  if mode[0] == 'd':
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
      translated += symbol

  return translated

mode = getMode()
message = getMessage()

if mode[0] != 'b':
  key = getKey()


print('Your translated text is:')
if mode[0] != 'b':
  print(getTranslatedMessage(mode, message, key))
else:
  for key in range(1, MAX_KEY_SIZE + 1):
    print(key, getTranslatedMessage('decrypt', message, key))
