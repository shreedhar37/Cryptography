def autoencrypt(text, key):
    result = ""
   #extract one character from string at a time and encrypt it.
    for i in range(len(text)):
        char = text[i]
        #check for position to apply given key
        if i == 0:
            if (char.isupper()):
            # formula : ciphertext = (plaintext + key ) mod 26 
                result += chr(((ord(char) - 65) + key) % 26 + 65)
            else:
                result += chr(((ord(char) - 97) + key) % 26 + 97)
        elif (char.isupper()):
            if text[i-1].isupper():
                #formula : Ciphertext = (plaintext[i] + plaintext[i-1]) mod 26                
                result += chr(((ord(char) - 65) + (ord(text[i-1]) - 65)) % 26 + 65 )
            else:
                result += chr(((ord(char) - 65) + (ord(text[i-1]) - 97)) % 26 + 65 )        
        else:
            if text[i-1].isupper():
                result += chr(((ord(char) - 97) + (ord(text[i-1]) - 65)) % 26 + 97 )
            else:
                result += chr(((ord(char) - 97) + (ord(text[i-1]) - 97)) % 26 + 97 )                  
    return result

def autodecrypt(text, plain_text, key):
    result = ""
   #extract one character from string at a time and encrypt it.
    for i in range(len(text)):
        char = text[i]
        #check for position to apply given key
        if i == 0:
            if (char.isupper()):
            # formula : ciphertext = (plaintext - key ) mod 26 
                result += chr(((ord(char) - 65) - key) % 26 + 65)
            else:
                result += chr(((ord(char) - 97) - key) % 26 + 97)
        elif (char.isupper()):
            if text[i-1].isupper():
                #formula : Ciphertext = (plaintext[i] - plaintext[i-1]) mod 26
                result += chr(((ord(char) - 65) - (ord(plain_text[i-1]) - 65)) % 26 + 65 )
            else:
                result += chr(((ord(char) - 65) - (ord(plain_text[i-1]) - 97)) % 26 + 65 )        
        else:
            if text[i-1].isupper():
                result += chr(((ord(char) - 97) - (ord(plain_text[i-1]) - 65)) % 26 + 97 )
            else:
                result += chr(((ord(char) - 97) - (ord(plain_text[i-1]) - 97)) % 26 + 97 )                  
    return result

def affineencrypt(text, k1, k2):
    result = ""
   #extract one character from string at a time and encrypt it.
    for i in range(len(text)):
        char = text[i]
        # spaces are ignored in encryption process
        if char == " ":
            result += " "      
        # checks if character is upper case or lower case.
        elif (char.isupper()):
            # formula : ciphertext = ((plaintext * key1 )+key2) mod 26 
            result += chr(((ord(char)-65) * k1 + k2) % 26 + 65)
      
        else:
            result += chr(((ord(char)-97) * k1 + k2) % 26 + 97)
    return result

#below function is used to calculate multiplicative inverse of key.
def inverse(k1):
    for i in range(1, 27):
        if (k1*i) % 26 == 1:
            return i

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

if __name__ == "__main__": 
    while (1):
        choice = int(input("\n1.Monoalphabetic Substitution (Affine Cipher)\n2.Polyaplhabetic Substitution (Autokey Cipher)\n3.Exit\nSelect your choice: "))
        if choice == 1:
            plain_text = input("\nEnter the plaintext: ")
            key1, key2 = [int(x) for x in input("Enter key pair sepearated by comma like(5, 2):  ").split(', ')]
            choice = int(input("\n1.Encryption\n2.Decryption\nEnter your choice: "))
            if choice == 1:
                print("\nEncryption: "+affineencrypt(plain_text, key1, key2))
            else:
                print("Decryption: "+affinedecrypt(plain_text, inverse(key1), key2))
        elif choice == 2:
            plain_text = input("Enter your message: ")
            plain_text = plain_text.replace(" ","")
            key = int(input("Enter the key: ")) 
            choice = int(input("\n1.Encryption\n2.Decryption\nEnter your choice: "))
            if choice == 1:
                print("\nEncryption (Cipher text): " +autoencrypt(plain_text, key))
            else:
                print("Decryption (Plain text): " +autodecrypt(autoencrypt(plain_text, key), plain_text, key))
        else:
            exit(0)

            

        
        

