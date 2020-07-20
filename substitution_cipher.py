def additiveencrypt(text, k):
    result = ""
   #extract one character from string at a time and encrypt it.
    for i in range(len(text)):
        char = text[i]
        # spaces are ignored in encryption process
        if char == " ":
            result += " "      
        # checks if character is upper case or lower case.
        elif (char.isupper()):
            # formula : ciphertext = (plaintext + key) mod 26 
            result += chr(((ord(char) - 65) + k) % 26 + 65)
      
        else:
            result += chr(((ord(char) - 97) + k) % 26 + 97)
    return result

def additivedecrypt(text, k):
    result = ""
   #extract one character from string at a time and encrypt it.
    for i in range(len(text)):
        char = text[i]
        # spaces are ignored in encryption process
        if char == " ":
            result += " "      
        # checks if character is upper case or lower case.
        elif (char.isupper()):
            # formula : ciphertext = (plaintext - key) mod 26 
            result += chr(((ord(char) - 65) - k) % 26 + 65)
      
        else:
            result += chr(((ord(char) - 97) - k) % 26 + 97)
    return result

def mulencrypt(text, k):
    result = ""
   #extract one character from string at a time and encrypt it.
    for i in range(len(text)):
        char = text[i]
        # spaces are ignored in encryption process
        if char == " ":
            result += " "      
        # checks if character is upper case or lower case.
        elif (char.isupper()):
            # formula : ciphertext = (plaintext * key ) mod 26 
            result += chr(((ord(char) - 65) * k) % 26 + 65)
      
        else:
            result += chr(((ord(char) - 97) * k) % 26 + 97)
    return result

#below function is used to calculate multiplicative inverse of key.
def inverse(s):
    for i in range(1, 27):
        if (s*i) % 26 == 1:
            return i

def muldecrypt(enc,kinv):
    result = ""
    for i in range(len(enc)):
        char = enc[i]
        if char == " ":
            result += " "
        elif (char.isupper()):
            # formula: plaintext = (ciphertext * key⁻¹) mod 26
            result += chr(((ord(char) - 65) * kinv) % 26 + 65)
        else:
            result += chr(((ord(char) - 97) * kinv) % 26 + 97 )
    return result  

def affineencrypt(text, k1, k2):
    result = ""
   #extract one character from string at a time and encrypt it.
    for i in range(len(text)):
        char = text[i]
        # spaces are ignored in encryption process
        if char==" ":
            result += " "      
        # checks if character is upper case or lower case.
        elif (char.isupper()):
            # formula : ciphertext = ((plaintext * key1 )+key2) mod 26 
            result += chr(((ord(char) - 65) * k1 + k2) % 26 + 65)
      
        else:
            result += chr(((ord(char) - 97) * k1 + k2) % 26 + 97)
    return result

def affinedecrypt(enc, kinv, k2):
    result = ""
    for i in range(len(enc)):
        char = enc[i]
        if char == " ":
            result += " "
        elif (char.isupper()):
            # formula: plaintext = ((ciphertext-key2) * key⁻¹) mod 26
            result += chr((((ord(char) - 65)-k2) * kinv) % 26 + 65)
        else:
            result += chr((((ord(char) - 97)-k2) * kinv) % 26 + 97 )
    return result            

while(1):
    print("\n1.Additive Cipher\n2.Multiplicative Cipher\n3.Affine Cipher\n4.Exit")
    n = int(input("Enter your choice: "))
    if n == 1:
        plain_text = input("\nEnter the plaintext: ")   
        key = int(input("Enter the key: "))
        choice = int(input("\n1.Encryption\n2.Decryption\nEnter your choice: "))
        if choice == 1:
            print("\nEncryption: "+additiveencrypt(plain_text, key))
        else:
            print("Decryption: "+additivedecrypt(additiveencrypt(plain_text, key), key)) 
        
    elif n == 2:
        plain_text = input("\nEnter the plaintext: ") 
        key = int(input("Enter the key: "))
        choice = int(input("\n1.Encryption\n2.Decryption\nEnter your choice: "))
        if choice == 1:
            print("\nEncryption: "+mulencrypt(plain_text, key))
        else:
            print("Decryption: "+muldecrypt(mulencrypt(plain_text, key), inverse(key)))

        
    elif n == 3:
        plain_text = input("\nEnter the plaintext: ")
        key1, key2 = [int(x) for x in input("Enter key pair sepearated by comma:  ").split(', ')]
        choice = int(input("\n1.Encryption\n2.Decryption\nEnter your choice: "))
        if choice == 1:
            print("\nEncryption: "+affineencrypt(plain_text, key1, key2))
        else:
            print("Decryption: "+affinedecrypt(plain_text, inverse(key1), key2))
    
    else:
        exit(0)