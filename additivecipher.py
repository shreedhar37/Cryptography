def additiveencrypt(text, k):
    result = ""
   #extract one character from string at a time and encrypt it.
    for i in range(len(text)):
        char = text[i]
        # spaces are ignored in encryption process     
        # checks if character is upper case or lower case.
        if (char.isupper()):
            # formula : ciphertext = (plaintext + key) mod 26 
            result += chr(((ord(char) - 65) + k) % 26 + 65)
      
        else:
            result += chr(((ord(char) - 97) + k) % 26 + 97)
    return result

def additivedecrypt(text,k):
    result = ""
   #extract one character from string at a time and encrypt it.
    for i in range(len(text)):
        char = text[i]
        # spaces are ignored in encryption process      
        # checks if character is upper case or lower case.
        if (char.isupper()):
            # formula : ciphertext = (plaintext - key) mod 26 
            result += chr(((ord(char) - 65) - k) % 26 + 65)
      
        else:
            result += chr(((ord(char) - 97) - k) % 26 + 97)
    return result
if __name__ == "__main__": 
    plain_text = input("Enter the plaintext: ")
    plain_text = plain_text.replace(" ","")
    key = int(input("Enter the key (range 0-25): "))
    print("\nEncryption: "+additiveencrypt(plain_text, key))
    print("Decryption: "+additivedecrypt(additiveencrypt(plain_text, key), key))
