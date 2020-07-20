def encrypt(text, k1, k2):
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

def decrypt(enc, kinv, k2):
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

plain_text = input("Enter the plaintext: ")
k1, k2 = [int(x) for x in input("Enter the two keys sepearated by ,: ".split(', '))]
kinv = inverse(k1)
enc = encrypt(plain_text, k1, k2)
print ("Encryption (Cipher text): " + encrypt(plain_text, k1, k2))
print("Decryption (Plain text): " + decrypt(enc, kinv, k2))
